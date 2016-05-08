sub successo{
	open (FILE, "< ../data/private_html/successo.html");
while(!eof(FILE)){
	$string .= <FILE>;
}
  close FILE;

  $string=~ s/__TIPO__/$_[0]/g;
  $string=~ s/__AZIONE__/$_[1]/g;
  $string=~ s/__PAGINA__/$_[2]/g;

print $string;
}