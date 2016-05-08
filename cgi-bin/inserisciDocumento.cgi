use utf8;
use File::stat;

sub doInserimentoDocumento{

	my $page=new CGI;
	# VERIFICA DEI DATI INSERITI

	my $titolo=&trim($page->param('titolo'));
	my $testo=&trim($page->param('testo'));
	my $docSRC;
	my $uploadDir;
	my $docN;
	my $docXML="<doc-completo/>";
	my $docDim;
	if($titolo eq '' or $testo eq ''){
		&documentoNonCorrettoInserimento($titolo,$testo);
	}


		#va fatto il caricamento del file pdf come quello della foto
	if($page->param('documento')){
		
			#$CGI::POST_MAX = 1024 * 5000; # grandezza massima 5MB (1024 * 5000 = 5MB)
			$CGI::DISABLE_UPLOADS = 0; # 1 disabilita uploads, 0 abilita uploads
			 
			#upload immagine
			$uploadDir="../public_html/document";
			my $dt   = DateTime->now;
			my $date = $dt->ymd;
			#imposto il nome della foto da salvare
			$docN ="$titolo-$date.pdf";
			$docSRC="../document/".$docN;

			my $docPath=$uploadDir."/".$docN;
			my $doc_handle=$page->upload('documento');

			open (FH, ">",$docPath);
			while (my $length = sysread($doc_handle, $buffer, 262144)) { #256KB
		        syswrite(FH, $buffer, $length);
		    }
		    close FH;
		    $docDim= stat($docPath)->size;
		    $docDim=int($docDim/1024);
		    $docXML="<doc-completo>$docSRC</doc-completo>";
	}
	else{
		&documentoNonCorrettoInserimento($titolo,$testo);
	}


	
	my $path="../data/documenti.xml";

	my $parser = XML::LibXML->new();
	my $doc = $parser->parse_file($path);
	my $rootDoc= $doc->getDocumentElement;

	my $nuovoDoc="

	<documento>
		<titolo>$titolo</titolo>
		<paragrafo>$testo</paragrafo>
		$docXML
		<dimensione>$docDim</dimensione>
	</documento>

	";

	if($rootDoc){

		my $nodo;
		eval{$nodo=$parser->parse_balanced_chunk($nuovoDoc)} || die &documentoNonCorrettoInserimento($titolo,$testo);
		$rootDoc->appendChild($nodo);
		open(OUT,">$path");
		flock(OUT,2);
		print OUT $doc->toString;
		close(OUT);
	
	}
}



sub documentoNonCorrettoInserimento{
open (FILE, "< ../data/private_html/editorDocumenti.html");
while(!eof(FILE)){
	$string .= <FILE>;
}
  close FILE;

my $errorField="Ci sono errori nell'inserimento dei dati";

$string=~ s/__TITOLO__/$_[0]/;
$string=~ s/__TESTO__/$_[1]/;
$string=~ s/__ACTION__/Inserisci Documento/;
$string=~ s/__VALSELEZIONA__/inserisci/;
$string=~ s/__SUBMITYPE__/Inserisci/g;
$string=~ s/__ACTIVEINS__/ id="active"/;
$string=~ s/__ACTIVEMOD__//;
$string=~ s/__LINKINS__/Inserisci/;
$string=~ s/__LINKMOD__/<a href="amministraSezionePrivata.cgi?Seleziona=modifica" tabindex="1">Modifica<\/a>/;
$string=~ s/__INPUTVECCHIODOCUMENTO__//g;
$string=~ s/__INCASODIERRORE__/$errorField/;
$string=~ s/__ERROREDOC__/Errore nell'inserimento dei dati, inserisci il documento/;

print $string;

exit;

}

sub trim($)
{
	my $string = shift;
	$string =~ s/^\s+//;
	$string =~ s/\s+$//;
	return $string;
}
