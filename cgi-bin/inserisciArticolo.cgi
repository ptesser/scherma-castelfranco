use utf8;

sub doInserimento{

my $page=new CGI;
# VERIFICA DEI DATI INSERITI

#estraggo la data inserita nella form e la converto in formato YYYY-MM-DD
	my @data;
	my $dataDaSalvare;
	my $titolo=&trim($page->param('titolo'));
	my $luogo=&trim($page->param('luogo'));
	my $testo=&trim($page->param('testo'));
	my $altFoto=&trim($page->param('altfoto'));
	my $fotoN;	
	my $uploadDir;
	my $fotoSRC;
	my $fotoXML="<img/>";

	if($page->param('datepicker')=~ m/\d{4}\/\d{2}\/\d{2}/){
		@data=split("/",$page->param('datepicker'));
		$dataDaSalvare=$data[0]."-".$data[1]."-".$data[2];
	}
	else{
		@data=split("-",$page->param('datepicker'));
		$dataDaSalvare=	$page->param('datepicker');
	}

	eval{timelocal(0,0,0,$data[2],$data[1]-1,$data[0]);} || die (&articoloNonCorretto($dataDaSalvare,$titolo,$luogo,$testo,$altFoto));

	if($titolo eq '' or $luogo eq '' or $testo eq ''){
		&articoloNonCorretto($dataDaSalvare,$titolo,$luogo,$testo,$altFoto);
	}

	if($page->param('foto')){
		if($page->param('altfoto')){
			
			#$CGI::POST_MAX = 1024 * 5000; # grandezza massima 5MB (1024 * 5000 = 5MB)
			$CGI::DISABLE_UPLOADS = 0; # 1 disabilita uploads, 0 abilita uploads
			 
			#upload immagine
			$uploadDir="../public_html/img/gare";

			#imposto il nome della foto da salvare
			$fotoN ="$luogo-$dataDaSalvare";
			$fotoN=~ s/ /-/g;
			$fotoSRC="../img/gare/".$fotoN;

			my $fotoPath=$uploadDir."/".$fotoN;
			my $foto_handle=$page->upload('foto');

			open (FH, ">",$fotoPath);
			while (my $length = sysread($foto_handle, $buffer, 262144)) { #256KB
		        syswrite(FH, $buffer, $length);
		    }
		    close FH;
		   	$fotoXML="<img src=\"".$fotoSRC."\" alt=\"".$altFoto."\"/>";
		}
		else
		{
			&articoloNonCorretto($dataDaSalvare,$titolo,$luogo,$testo,$altFoto);
		}
	}
	
	#INSERIMENTO DEI DATI VERIFICATI DENTO articoli.xml
	my $path="../data/articoli.xml";
	my $parser = XML::LibXML->new();
	my $doc = $parser->parse_file($path);
	my $rootDoc= $doc->getDocumentElement;

	my $nuovoArticolo="
	<articolo>
		<luogo>".$luogo."</luogo>
		<data>".$dataDaSalvare."</data>
		<titolo>".$titolo."</titolo>".$fotoXML."
		<paragrafo>".$testo."</paragrafo>
	</articolo>

	";

	if($rootDoc){
		my $nodo;
		eval{$nodo=$parser->parse_balanced_chunk($nuovoArticolo)} || die (&articoloNonCorretto($dataDaSalvare,$titolo,$luogo,$testo,$altFoto));
		$rootDoc->appendChild($nodo);
		open(OUT,">$path");
		flock(OUT,2);
		print OUT $doc->toString;
		close(OUT);
	}

}

#in caso ci siano errori nell'inserimento dell'articolo torno alla pagina segnalando che ci sono errori e rifaccio vedere 
#tutti i dati inseriti precedentemente
sub articoloNonCorretto{
open (FILE, "< ../data/private_html/editorArticoli.html");
while(!eof(FILE)){
	$string .= <FILE>;
}
  close FILE;

my $errorField="Ci sono errori nell'inserimento dei dati, controlla tag apertura e chiusura, la data che sia scritta in maniera corretta 
			YYYY-MM-DD(prima l'anno, poi mese,poi giorno)";
$string=~ s/__REINSERISCIFOTO__/Errore nell'inserimento dei dati, reinserisci la foto e controlla l'alt se corretto/;
$string=~ s/__ALT__/$_[4]/;
$string=~ s/__LUOGO__/$_[2]/;
$string=~ s/__DATA__/$_[0]/;
$string=~ s/__TITOLO__/$_[1]/;
$string=~ s/__TESTO__/$_[3]/;
$string=~ s/__ALT__//;
$string=~ s/__ACTION__/Inserisci Articolo/;
$string=~ s/__VALSELEZIONA__/inserisci/;
$string=~ s/__SUBMITYPE__/Inserisci/g;
$string=~ s/__INPUTFOTOVECCHIA__//g;
$string=~ s/__VECCHIOALTFOTO__//g;
$string=~ s/__ACTIVEINS__/ id="active"/;
$string=~ s/__ACTIVEMOD__//;
$string=~ s/__LINKINS__/Inserisci/;
$string=~ s/__LINKMOD__/<a href="amministraSezionePrivata.cgi?Seleziona=modifica" tabindex="1">Modifica<\/a>/;
$string=~ s/__INCASODIERRORE__/$errorField/;

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