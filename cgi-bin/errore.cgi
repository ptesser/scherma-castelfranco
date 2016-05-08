#!/usr/bin/perl -w
#ottengo il file HTML da modificare
open (FILE, "<","../data/private_html/errore.html");
flock(FILE,1);
while(!eof(FILE)){
	$pagina .= <FILE>;
}
close FILE;
print $pagina;
exit;