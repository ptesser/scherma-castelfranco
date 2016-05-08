#!/usr/bin/perl -w

use XML::LibXSLT;
use XML::LibXML;
use CGI;
use utf8;
use CGI::Session;
use charnames qw( :full :short );
use CGI::Carp qw(fatalsToBrowser);

do 'articoloCompleto.cgi';

my $page=new CGI;
if($page->param('artCompleto')) {

	&articoloCompleto($page->param('data'), $page->param('luogo'));
}
else {

my $file_xml="../data/articoli.xml";
my $file_xsl="../data/articoli.xsl";

#creo il parser
my $parser = XML::LibXML->new();
#creo l'oggetto per la trasformata
my $xslt = XML::LibXSLT->new();

#parser dei due documenti
my $doc = $parser->parse_file($file_xml);
my $xslt_doc = $parser->parse_file($file_xsl);

#porto in formato testuale il file dell'xsl
my $query = $xslt_doc->toString;

my $n_articoli=5;

if($page->param('articoli')!=0){
	$n_articoli=$page->param('articoli');
}

my $doc_tree = $parser->parse_file($file_xml);
my $root = $doc_tree->documentElement();
my $xpc = XML::LibXML::XPathContext->new($root);
$xpc->registerNs('ts', 'http://www.articoli.com');
my $querycount="count(/ts:testi/ts:articolo)";
my $numero_articoli=$xpc->find($querycount);

if($numero_articoli>$n_articoli){
	$query=~ s/__MOSTRAPIU__/<p id="mostra-piu"><a href="articoli.cgi?articoli=__NART__">Mostra articoli meno recenti<\/a><\/p>/g;
}
else{
	$query=~ s/__MOSTRAPIU__//g;
}

#sostituisco nel file xsl quanti articoli far vedere 
$query=~ s/__ART__/$n_articoli/g;
#sostituisco quanti articoli in più fare vedere 
$n_articoli+=3;
$query=~ s/__NART__/$n_articoli/g;

#$query=~ s/__STILE-IE__/<!--\[if (IE 6)\|(IE 7)\|(IE 8)\]><link rel="stylesheet" href="..\/css\/stileIE.css" type="text\/css"\/><!\[endif\]-->/g;

$xslt_doc = $parser->parse_string($query);

#creazione del foglio di trasformazione, con sostituzione occorrenza
my $stylesheet = $xslt->parse_stylesheet($xslt_doc);

#applicazione del foglio di trasformazione
my $risultato = $stylesheet->transform($doc);
my $risultatoS=$risultato->toString();

$risultatoS=~ s/<paragrafo xmlns:xs="http:\/\/www.w3.org\/2001\/XMLSchema-instance" xmlns="http:\/\/www.articoli.com" xmlns:ts="http:\/\/www.articoli.com">//g;
$risultatoS=~ s/<\/paragrafo>//g;
$risultatoS=~ s/<!DOCTYPE html PUBLIC "-\/\/W3C\/\/DTD XHTML 1.0 Strict\/\/EN" "http:\/\/www.w3.org\/TR\/xhtml1\/DTD\/xhtml1-strict.dtd">//;
$risultatoS=~ s/xmlns="http:\/\/www.w3.org\/1999\/xhtml" lang="it" xml:lang="it"/lang="it"/g;
$risultatoS=~ s/<\?xml version="1.0" encoding="UTF-8" standalone="yes"\?>//g;

print "Content-type: text/html\n\n";
print "<!DOCTYPE html > ";
print $risultatoS;
}