#!/usr/bin/perl -w

use XML::LibXSLT;
use XML::LibXML;
use CGI;
use utf8;
use CGI::Session;
use charnames qw( :full :short );
use CGI::Carp qw(fatalsToBrowser);

$page=new CGI;

my $file_xml="../data/documenti.xml";
my $file_xsl="../data/documenti.xsl";

#creo il parser
my $parser = XML::LibXML->new();
#creo l'oggetto per la trasformata
my $xslt = XML::LibXSLT->new();

#parser dei due documenti
my $doc = $parser->parse_file($file_xml);
my $xslt_doc = $parser->parse_file($file_xsl);

#porto in formato testuale il file dell'xsl
my $query = $xslt_doc->toString;

my $n_documenti=5;

if($page->param('documenti') != 0){
	$n_documenti=$page->param('documenti');
}
my $doc_tree = $parser->parse_file($file_xml);
my $root = $doc_tree->documentElement();
my $xpc = XML::LibXML::XPathContext->new($root);
$xpc->registerNs('ts', 'http://www.articoli.com');
my $querycount="count(/ts:testi/ts:documenti)";
my $numero_documenti=$xpc->find($querycount);

if($numero_documenti>$n_documenti){
	$query=~ s/__MOSTRAPIU__/<p id="mostra-piu"><a href="documenti.cgi?documenti=__NDOC__">Mostra documenti meno recenti<\/a><\/p>/g;
}
else{
	$query=~ s/__MOSTRAPIU__//g;
}

#sostituisco nel file xsl quanti articoli far vedere 
$query=~ s/__DOC__/$n_documenti/g;
#sostituisco quanti articoli in più fare vedere 
$n_documenti+=3;
$query=~ s/__NDOC__/$n_documenti/g;
$xslt_doc = $parser->parse_string($query);

#creazione del foglio di trasformazione, con sostituzione occorrenza
my $stylesheet = $xslt->parse_stylesheet($xslt_doc);

#applicazione del foglio di trasformazione
my $risultato = $stylesheet->transform($doc);
my $risultatoS=$risultato->toString();
$risultatoS=~ s/<!DOCTYPE html PUBLIC "-\/\/W3C\/\/DTD XHTML 1.0 Strict\/\/EN" "http:\/\/www.w3.org\/TR\/xhtml1\/DTD\/xhtml1-strict.dtd">//;
$risultatoS=~ s/xmlns="http:\/\/www.w3.org\/1999\/xhtml" version="-\/\/W3C\/\/DTD XHTML 1.1\/\/EN" xml:lang="it" lang="it"/lang="it"/g;
$risultatoS=~ s/<\?xml version="1.0" encoding="UTF-8" standalone="yes"\?>//g;


print "Content-type: text/html\n\n";
print "<!DOCTYPE html >";
print $risultatoS;