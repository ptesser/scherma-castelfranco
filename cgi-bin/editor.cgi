use utf8;

sub getEditor{
	
#ottengo il file HTML da modificare
open (FILE, "< ../data/private_html/editorArticoli.html");
while(!eof(FILE)){
	$string .= <FILE>;
}
  close FILE;

$string=~ s/__LUOGO__//;
$string=~ s/__SELECTART__/selected/;
$string=~ s/__SELECTDOC__//;
$string=~ s/__DATA__//;
$string=~ s/__TITOLO__//;
$string=~ s/__TESTO__//;
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
$string=~ s/__INCASODIERRORE__//;
$string=~ s/__REINSERISCIFOTO__//;

print $string;
}

sub getEditorDocumento{
open (FILE, "< ../data/private_html/editorDocumenti.html");
while(!eof(FILE)){
	$string .= <FILE>;
}
close FILE;

$string=~ s/__SELECTART__//;
$string=~ s/__SELECTDOC__/selected/;
$string=~ s/__TITOLO__//g;
$string=~ s/__VECCHIOTITOLO__//g;
$string=~ s/__TESTO__//;
$string=~ s/__ACTION__/Inserisci Documento/;
$string=~ s/__VALSELEZIONA__/inserisci/;
$string=~ s/__SUBMITYPE__/Inserisci/g;
$string=~ s/__ACTIVEINS__/ id="active"/;
$string=~ s/__ACTIVEMOD__//;
$string=~ s/__LINKINS__/Inserisci/;
$string=~ s/__LINKMOD__/<a href="amministraSezionePrivata.cgi?Seleziona=modifica" tabindex="1">Modifica<\/a>/;
$string=~ s/__INPUTVECCHIODOCUMENTO__//g;
$string=~ s/__INCASODIERRORE__//;
$string=~ s/__ERROREDOC__//;

print $string;
}