use utf8;
require Encode;
use File::stat;

sub doCaricaFormModificaDocumento{
#ottengo il file HTML da modificare
open (FILE, "< ../data/private_html/formModifica.html");
while(!eof(FILE)){
	$form .= <FILE>;
}
close FILE;

#estraggo gli articoli che ci sono e ne mostro data e luogo in cui sono stati effettuati per far selezionare quale cambiare
my $path="../data/documenti.xml";
my $parser = new XML::LibXML;
my $doc_tree = $parser->parse_file($path);
my $root = $doc_tree->documentElement();
my $xpc = XML::LibXML::XPathContext->new($root);
$xpc->registerNs('ts', 'http://www.documenti.com');
my @documenti=$xpc->find('//ts:documento')->get_nodelist();
my $checkboxdoc;
my $appo;
my $tabindex=5;

foreach $documento (@documenti)
{
	my $titolo=Encode::encode('utf8',$documento->getElementsByTagName("titolo")->get_node(1)->string_value);
	
	
	$appo="
		<p><label><input type=\"radio\" name=\"modifica_doc\" class=\"stile-radio\" tabindex=\"$tabindex\"
		 value=\"$titolo\"/><label> $titolo</label></p>
	";
	$tabindex+=1;
	$checkboxdoc .= $appo;
}

$form=~ s/__DATI__/$checkboxdoc/;
$form=~ s/__TIPO__/Documento/g;
$form=~ s/__VALOREMODIFICA__/CaricaEditorDocumento/;
$form=~ s/__SELECTART__//;
$form=~ s/__SELECTDOC__/selected/;


print $form;
exit;
}


sub doCaricaEditorModificaDocumento{

#ottengo il file HTML da modificare
open (FILE, "<","../data/private_html/editorDocumenti.html");
while(!eof(FILE)){
	$editor .= <FILE>;
}
close FILE;

$editor=~ s/__SELECTART__//;
$editor=~ s/__SELECTDOC__/selected/;
$editor=~ s/__ERROREDOC__//;
$editor=~ s/__INPUTVECCHIODOCUMENTO__/ <label>Vecchio documento: <input type="text" name="vecchioDoc" value="__VECCHIODOC__" readonly \/><\/label>/g;
$editor=~ s/__INCASODIERRORE__//;
$editor=~ s/__VALOREMODIFICA__/SalvaDocumento/;
$editor=~ s/__ACTION__/Salva Documento/;
$editor=~ s/__VALSELEZIONA__/modifica/;
$editor=~ s/__SUBMITYPE__/Modifica/g;
$editor=~ s/__ACTIVEINS__//;
$editor=~ s/__ACTIVEMOD__/ id="active"/;
$editor=~ s/__LINKINS__/<a href="amministraSezionePrivata.cgi?Seleziona=inserisci" tabindex="1">Inserisci<\/a>/;
$editor=~ s/__LINKMOD__/Modifica/;


my $page=CGI->new();
#estraggo i valori dalla query string per poi cercare l'articolo voluto
$valore=$page->param("modifica_doc");
my $doc;
my $path="../data/documenti.xml";
my $parser = new XML::LibXML;
my $doc_tree = $parser->parse_file($path);

my $root = $doc_tree->documentElement();
my $xpc = XML::LibXML::XPathContext->new($root);

$xpc->registerNs('ts', 'http://www.documenti.com');
my @documenti=$xpc->find('//ts:documento')->get_nodelist();

foreach my $node (@documenti) {
	my $titolo=Encode::encode('utf8',$node->getElementsByTagName("titolo")->get_node(1)->string_value);
	if($titolo eq $valore){
		$docPath=Encode::encode('utf8',$node->getElementsByTagName("doc-completo")->get_node(1)->string_value);
		foreach $el (split('/',$docPath)){
			$doc=$el;
		}
		$paragrafo= Encode::encode('utf8',$node->getElementsByTagName("paragrafo")->item(0)->toString);
		$paragrafo=~ s/\<paragrafo\>//;
		$paragrafo=~ s/\<\/paragrafo\>//;
		$editor=~ s/__TITOLO__/$titolo/;
		$editor=~ s/__VECCHIOTITOLO__/$titolo/;
		$editor=~ s/__TESTO__/$paragrafo/;
		$editor=~ s/__VECCHIODOC__/$doc/;
	}

}

print $editor;
exit;

}

sub doSalvaDocumento{
my $page=new CGI;
# VERIFICA DEI DATI INSERITI

	# estraggo i vecchi dati che ho salvato nei campi hidden per trovare l'articolo giusto nell'xml
	my $vecchioTitolo=&trim($page->param('vecchioTitolo'));
	my $vecchioD=&trim($page->param('vecchioDoc'));
	my $titolo=&trim($page->param('titolo'));
	my $testo=&trim($page->param('testo'));
	my $docSRC;
	my $uploadDir="../public_html/document/";
	my $docN;
	my $docXML="<doc-completo/>";
	my $docDim;

	if($titolo eq '' or $testo eq ''){
		&documentoNonCorrettoModifica($titolo,$testo,$vecchioTitolo,$vecchioD);
	}

	if($page->param('documento')){
		
			#$CGI::POST_MAX = 1024 * 5000; # grandezza massima 5MB (1024 * 5000 = 5MB)
			$CGI::DISABLE_UPLOADS = 0; # 1 disabilita uploads, 0 abilita uploads
			 
			#upload documento
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
		if($page->param('vecchioDoc')){
			$docSRC="../document/".$page->param('vecchioDoc');
			$docDim= stat($uploadDir."/".$page->param('vecchioDoc'))->size;
			$docDim=int($docDim/1024);
			$docXML="<doc-completo>$docSRC</doc-completo>";
		}
	}
	
	
	my $path="../data/documenti.xml";
	my $parser = new XML::LibXML;
	my $doc_tree = $parser->parse_file($path);

	my $root = $doc_tree->documentElement();
	my $xpc = XML::LibXML::XPathContext->new($root);

	$xpc->registerNs('ts', 'http://www.documenti.com');
	my $query="//ts:documento[ts:titolo=\"$vecchioTitolo\"]";
	my @documenti=$xpc->find($query)->get_nodelist();

	my $nuovoDoc="

	<documento>
		<titolo>$titolo</titolo>
		<paragrafo>$testo</paragrafo>
		$docXML
		<dimensione>$docDim</dimensione>
	</documento>

	";
	
	my $nodo;
	eval{$nodo=$parser->parse_balanced_chunk($nuovoDoc)} || die &documentoNonCorrettoModifica($titolo,$testo,$vecchioTitolo,$vecchioD);
	
	foreach my $node(@documenti){
		$root->removeChild($node);
	}

	if($root){		
		$root->appendChild($nodo);
		open(OUT,">$path");
		flock(OUT,2);
		print OUT $doc_tree->toString();
		close(OUT);
	}
}


sub documentoNonCorrettoModifica{
open (FILE, "< ../data/private_html/editorDocumenti.html");
while(!eof(FILE)){
	$string .= <FILE>;
}
close FILE;

my $errorField="<p class=\"errore\">Ci sono errori nell'inserimento dei dati</p>";
$string=~ s/__SELECTART__//;
$string=~ s/__SELECTDOC__/selected/;
$string=~ s/__INPUTVECCHIODOCUMENTO__/ <label>Vecchio documento: <input type="text" name="vecchioDoc" value="__VECCHIODOC__" readonly \/><\/label>/g;
$string=~ s/__TITOLO__/$_[0]/g;
$string=~ s/__TESTO__/$_[1]/;
$string=~ s/__VECCHIOTITOLO__/$_[2]/g;
$string=~ s/__VECCHIODOC__/$_[3]/;
$string=~ s/__VALOREMODIFICA__/SalvaDocumento/;
$string=~ s/__ACTION__/Salva Documento/;
$string=~ s/__VALSELEZIONA__/modifica/;
$string=~ s/__SUBMITYPE__/Modifica/g;
$string=~ s/__ACTIVEINS__//;
$string=~ s/__ACTIVEMOD__/ id="active"/;
$string=~ s/__LINKINS__/<a href="amministraSezionePrivata.cgi?Seleziona=inserisci" tabindex="1">Inserisci<\/a>/;
$string=~ s/__LINKMOD__/Modifica/;
$string=~ s/__INCASODIERRORE__/$errorField/;
$string=~ s/__ERROREDOC__/Errore nell'inserimento dei dati, inserisci nuovamente il documento/;

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