use Time::Local;
use utf8;
require Encode;

sub doCaricaFormModifica{
	
#ottengo il file HTML da modificare
open (FILE, "< ../data/private_html/formModifica.html");
while(!eof(FILE)){
	$form .= <FILE>;
}
close FILE;

#estraggo gli articoli che ci sono e ne mostro data e luogo in cui sono stati effettuati per far selezionare quale cambiare
my $path="../data/articoli.xml";
my $parser = new XML::LibXML;
my $doc_tree = $parser->parse_file($path);
my $root = $doc_tree->documentElement();
my $xpc = XML::LibXML::XPathContext->new($root);
$xpc->registerNs('ts', 'http://www.articoli.com');
my @articoli=$xpc->find('//ts:articolo')->get_nodelist();
my $checkboxarticoli;
my $appo;
my $tabindex=5;

foreach $articolo (@articoli)
{
	my $data=Encode::encode('utf8',$articolo->getElementsByTagName("data")->get_node(1)->string_value);
	my $luogo=Encode::encode('utf8',$articolo->getElementsByTagName("luogo")->get_node(1)->string_value);
	
	$appo="
		<p><label><input type=\"radio\" name=\"modifica_articolo\" class=\"stile-radio\" tabindex=\"$tabindex\"
		 value=\"".$data."/".$luogo."\"/>" 
		 .$data." @ ".$luogo."</label></p>
	";
	$tabindex+=1;
	$checkboxarticoli .= $appo;
}

$form=~ s/__DATI__/$checkboxarticoli/;
$form=~ s/__TIPO__/Articolo/g;
$form=~ s/__VALOREMODIFICA__/CaricaEditorArticolo/;
$form=~ s/__SELECTART__/selected/;
$form=~ s/__SELECTDOC__//;

print $form;
exit;

}



sub doCaricaEditorModifica{
#ottengo il file HTML da modificare
open (FILE, "<","../data/private_html/editorArticoli.html");
while(!eof(FILE)){
	$editor .= <FILE>;
}
close FILE;


$editor=~ s/__SELECTART__/selected/g;
$editor=~ s/__SELECTDOC__//g;
$editor=~ s/__REINSERISCIFOTO__//;
$editor=~ s/__INCASODIERRORE__//;
$editor=~ s/__INPUTFOTOVECCHIA__/<label>Vecchia foto: <input type="text" name="vecchiaFoto" value="__VECCHIAFOTO__" readonly\/><\/label>/g;
$editor=~ s/__VECCHIOALTFOTO__/<label>Vecchia alternativa foto: <input type="text" name="vecchioAlt" value="__VECCHIOALT__" readonly\/><\/label>/g;
$editor=~ s/__ACTION__/Salva Articolo/;
$editor=~ s/__VALOREMODIFICA__/SalvaArticolo/;
$editor=~ s/__VALSELEZIONA__/modifica/;
$editor=~ s/__SUBMITYPE__/Modifica/g;
$editor=~ s/__ACTIVEINS__//;
$editor=~ s/__ACTIVEMOD__/ id="active"/;
$editor=~ s/__LINKINS__/<a href="amministraSezionePrivata.cgi?Seleziona=inserisci" tabindex="1">Inserisci<\/a>/;
$editor=~ s/__LINKMOD__/Modifica/;

my $page=CGI->new();
#estraggo i valori dalla query string per poi cercare l'articolo voluto
if($page->param('modifica_articolo')){
	@valori=split("/", $page->param("modifica_articolo"));
}
if($page->param('vecchiaData')){
	@valori=split("-", $page->param("vecchiaData"));	
}

my $path="../data/articoli.xml";
my $parser = new XML::LibXML;
my $doc_tree = $parser->parse_file($path);

my $root = $doc_tree->documentElement();
my $xpc = XML::LibXML::XPathContext->new($root);

$xpc->registerNs('ts', 'http://www.articoli.com');
my @articoli=$xpc->find('//ts:articolo')->get_nodelist();

foreach my $node (@articoli) {
	my $data=Encode::encode('utf8',$node->getElementsByTagName("data")->get_node(1)->string_value);
	my $luogo=Encode::encode('utf8',$node->getElementsByTagName("luogo")->get_node(1)->string_value);
	if($data eq $valori[0] && $luogo eq $valori[1]){
		my $titolo=Encode::encode('utf8',$node->getElementsByTagName("titolo")->get_node(1)->string_value);
		my $imgsrc=Encode::encode('utf8',$node->getElementsByTagName("img")->get_node(1)->getAttribute("src"));
		my $img;
		foreach $el (split('/',$imgsrc)){
			$img=$el;
		}
		my $imgalt=Encode::encode('utf8',$node->getElementsByTagName("img")->get_node(1)->getAttribute("alt"));
		my $paragrafo=Encode::encode('utf8',$node->getElementsByTagName("paragrafo")->item(0)->toString);
		$paragrafo=~ s/\<paragrafo\>//;
		$paragrafo=~ s/\<\/paragrafo\>//;
		$editor=~ s/__LUOGO__/$luogo/g;
		$editor=~ s/__VECCHIOLUOGO__/$luogo/g;
		$editor=~ s/__DATA__/$data/;
		$editor=~ s/__VECCHIADATA__/$data/;
		$editor=~ s/__TITOLO__/$titolo/;
		$editor=~ s/__TESTO__/$paragrafo/;
		$editor=~ s/__FOTO__/$img/g;
		$editor=~ s/__VECCHIAFOTO__/$img/g;
		$editor=~ s/__ALT__//;
		$editor=~ s/__VECCHIOALT__/$imgalt/;
	}

}
print $editor;
exit;
}



sub doSalvaArticolo{
my $page=new CGI;
# VERIFICA DEI DATI INSERITI

	# estraggo i vecchi dati che ho salvato nei campi hidden per trovare l'articolo giusto nell'xml
	my $datavecchia=$page->param('vecchiaData');
	my $vecchioluogo=$page->param('vecchioLuogo');
	my @data;
	my $dataDaSalvare;
	
	if($page->param('datepicker')=~ m/\d{4}\/\d{2}\/\d{2}/){
		@data=split("/",$page->param('datepicker'));
		$dataDaSalvare=$data[0]."-".$data[1]."-".$data[2];
	}
	else{
		@data=split("-",$page->param('datepicker'));
		$dataDaSalvare=	$page->param('datepicker');
	}

	my $titolo=&trim($page->param('titolo'));
	my $luogo=&trim($page->param('luogo'));
	my $testo=&trim($page->param('testo'));
	my $fotoNome=$page->param('foto');
	my $vecchiaFoto=$page->param('vecchiaFoto');
	my $altVecchio=&trim($page->param('vecchioAlt'));
	my $altFoto=&trim($page->param('altfoto'));
	my $uploadDir="../public_html/img/gare";
	my $fotoSRC="../img/gare/";
	my $fotoXML="<img/>";

	eval{timelocal(0,0,0,$data[2],$data[1]-1,$data[0]);} || 
				die (&articoloNonCorrettoModifica($luogo,$dataDaSalvare,$titolo,$testo,$altFoto,$datavecchia,$vecchioluogo,$fotoNome,$vecchiaFoto,$vecchioAlt));

	if($titolo eq '' or $luogo eq '' or $testo eq ''){
		&articoloNonCorrettoModifica($luogo,$dataDaSalvare,$titolo,$testo,$altFoto,$datavecchia,$vecchioluogo,$fotoNome,$vecchiaFoto,$vecchioAlt);
	}


	if($page->param('foto')){
		if($page->param('altfoto')){
			#$CGI::POST_MAX = 1024 * 5000; # grandezza massima 5MB (1024 * 5000 = 5MB)
			$CGI::DISABLE_UPLOADS = 0; # 1 disabilita uploads, 0 abilita uploads

			#imposto il nome della foto da salvare
			$fotoN ="$luogo-$dataDaSalvare";
			$fotoN=~ s/ /-/g;
			$fotoSRC.=$fotoN;

			my $fotoPath=$uploadDir."/".$fotoN;
			my $foto_handle=$page->upload('foto');

			open (FH, ">",$fotoPath);
			while (my $length = sysread($foto_handle, $buffer, 262144)) { #256KB
		        syswrite(FH, $buffer, $length);
		    }
		    close FH;
		    $fotoXML="<img src=\"".$fotoSRC."\" alt=\"".$altFoto."\"/>";
		}
		else{
			&articoloNonCorrettoModifica($luogo,$dataDaSalvare,$titolo,$testo,$altFoto,$datavecchia,$vecchioluogo,$fotoNome,$vecchiaFoto,$vecchioAlt);
		}
	}
	else{
		if($page->param("vecchiaFoto") and $page->param('vecchioAlt')){
			$fotoSRC.=$page->param("vecchiaFoto");
			$altFoto=$page->param('vecchioAlt');
			$fotoXML="<img src=\"".$fotoSRC."\" alt=\"".$altFoto."\"/>";	
		}
	}


	my $path="../data/articoli.xml";
	my $parser = new XML::LibXML;
	my $doc_tree = $parser->parse_file($path);
	my $root = $doc_tree->documentElement();
	my $xpc = XML::LibXML::XPathContext->new($root);
	$xpc->registerNs('ts', 'http://www.articoli.com');
	my $query="//ts:articolo[ts:luogo=\"$vecchioluogo\" and ts:data=\"$datavecchia\"]";
	my @articoli=$xpc->find($query)->get_nodelist();

	my $nuovoArticolo="

	<articolo>
		<luogo>".$luogo."</luogo>
		<data>".$dataDaSalvare."</data>
		<titolo>".$titolo."</titolo>".$fotoXML."
		<paragrafo>".$testo."</paragrafo>
	</articolo>

	";

	my $nodo;
	eval{$nodo=$parser->parse_balanced_chunk($nuovoArticolo)}|| die 
				&articoloNonCorrettoModifica($luogo,$dataDaSalvare,$titolo,$testo,$altFoto,$datavecchia,$vecchioluogo,$fotoNome,$vecchioAlt);

	foreach my $node(@articoli){
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


sub articoloNonCorrettoModifica{

open (FILE, "<","../data/private_html/editorArticoli.html");
while(!eof(FILE)){
	$editor .= <FILE>;
}
close FILE;

my $errorField="Ci sono errori nell'inserimento dei dati, controlla tag apertura e chiusura, la data che sia scritta in maniera corretta 
			YYYY-MM-DD(prima l'anno, poi mese,poi giorno)";
$editor=~ s/__REINSERISCIFOTO__/Errore nell'inserimento dei dati, reinserisci la foto e controlla l'alt se corretto/;
$editor=~ s/__INPUTFOTOVECCHIA__/<label>Vecchia foto: <input type="text" name="vecchiaFoto" value="__VECCHIAFOTO__" readonly\/><\/label>/g;
$editor=~ s/__VECCHIOALTFOTO__/<label>Vecchia alternativa foto: <input type="text" name="vecchioAlt" value="__VECCHIOALT__" readonly\/><\/label>/g;
$editor=~ s/__VECCHIOALT__/$_[8]/g;
$editor=~ s/__ACTION__/Salva Articolo/;
$editor=~ s/__VALOREMODIFICA__/SalvaArticolo/;
$editor=~ s/__VALSELEZIONA__/modifica/;
$editor=~ s/__SUBMITYPE__/Modifica/g;
$editor=~ s/__ACTIVEINS__//;
$editor=~ s/__ACTIVEMOD__/ id="active"/;
$editor=~ s/__LINKINS__/<a href="amministraSezionePrivata.cgi?Seleziona=inserisci" tabindex="1">Inserisci<\/a>/;
$editor=~ s/__LINKMOD__/Modifica/;
$editor=~ s/__LUOGO__/$_[0]/g;
$editor=~ s/__VECCHIOLUOGO__/$_[6]/g;
$editor=~ s/__DATA__/$_[1]/;
$editor=~ s/__VECCHIADATA__/$_[5]/;
$editor=~ s/__TITOLO__/$_[2]/;
$editor=~ s/__TESTO__/$_[3]/;
$editor=~ s/__FOTO__/$_[7]/g;
$editor=~ s/__VECCHIAFOTO__/$_[8]/g;
$editor=~ s/__ALT__/$_[4]/;
$editor=~ s/__INCASODIERRORE__/$errorField/;


print $editor;
exit;

}


sub trim($)
{
	my $string = shift;
	$string =~ s/^\s+//;
	$string =~ s/\s+$//;
	return $string;
}
