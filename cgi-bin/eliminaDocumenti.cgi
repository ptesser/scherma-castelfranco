sub doCaricaFormEliminaDocumento{

#ottengo il file HTML da modificare
	open (FILE, "< ../data/private_html/formElimina.html");
	while(!eof(FILE)){
	$form .= <FILE>;
	}
	close FILE;

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
	$titolo=Encode::encode('utf8',$documento->getElementsByTagName("titolo")->get_node(1)->string_value);
	
	
	$appo="
		<p><label><input type=\"checkbox\" name=\"elimina_doc\" class=\"stile-checkbox\" tabindex=\"$tabindex\"
		 value=\"$titolo\"/>$titolo</label></p>
	";
	$tabindex+=1;
	$checkboxdoc .= $appo;
}

$form=~ s/__DATI__/$checkboxdoc/;
$form=~ s/__TIPO__/Documenti/g;
$form=~ s/__VALOREELIMINA__/EliminaDocumenti/;
$form=~ s/__SELECTART__//;
$form=~ s/__SELECTDOC__/selected/;


print $form;
exit;


}

sub doEliminaDocumenti{

	my $page=CGI->new();

	my @valori=$page->param("elimina_doc");

	foreach  my $valore (@valori){
		
		$query.="ts:titolo=\"".$valore."\" or ";
	
	}

	$query=	substr $query, 0, -3;

	my $path="../data/documenti.xml";
	my $parser = new XML::LibXML;
	my $doc_tree = $parser->parse_file($path);

	my $root = $doc_tree->documentElement();
	my $xpc = XML::LibXML::XPathContext->new($root);

	$xpc->registerNs('ts', 'http://www.documenti.com');
	@documenti=$xpc->find('//ts:documento['.$query.']')->get_nodelist();
	
	foreach my $documento(@documenti){
		$root->removeChild($documento);
	}

	if($root){

		open(OUT,">$path");
		flock(OUT,2);
		print OUT $doc_tree->toString();
		close(OUT);
	}
}