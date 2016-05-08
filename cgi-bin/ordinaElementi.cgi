use utf8;

sub ordinaElementi
{
	#creo il parser
	my $parser = XML::LibXML->new();
	#creo l'oggetto per la trasformata
	my $xslt = XML::LibXSLT->new();
	my $path="../data/articoli.xml";
	my $file_xsl="../data/ordina.xsl";
	$doc = $parser->parse_file($path);
	$rootDoc= $doc->getDocumentElement;
	
	#parser dei due documenti
	my $xslt_doc = $parser->parse_file($file_xsl);

	#creazione del foglio di trasformazione
	my $stylesheet = $xslt->parse_stylesheet($xslt_doc);

	#applicazione del foglio di trasformazione
	my $risultato = $stylesheet->transform($doc);
	my @articoli=$risultato->find("//ts:articolo")->get_nodelist();
	my $articoliFinali='';
	foreach $articolo(@articoli){
		$articoliFinali=Encode::encode('utf8',$articolo->toString()).$articoliFinali;
	}
	
	$articoliFinali=~ s/<articolo xmlns:xs="http:\/\/www.w3.org\/2001\/XMLSchema-instance" xmlns="http:\/\/www.articoli.com" xmlns:ts="http:\/\/www.articoli.com">/<articolo>/g;
	my $finalResult="<?xml version=\"1.0\" encoding=\"UTF-8\"?>
					<?xml-stylesheet type=\"text/xsl\" href=\"articoli.xsl\"?>
					<ts:testi xmlns:xs=\"http://www.w3.org/2001/XMLSchema-instance\" 
					xmlns=\"http://www.articoli.com\" xs:schemaLocation=\"http://www.articoli.com articoli.xsd\" 
					xmlns:ts=\"http://www.articoli.com\">".$articoliFinali."</ts:testi>";
	open(OUT,">$path");
	flock(OUT,2);
	print OUT $finalResult;
	close(OUT);
}