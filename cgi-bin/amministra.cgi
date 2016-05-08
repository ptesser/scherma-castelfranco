#!/usr/bin/perl -w

use XML::LibXSLT;
use XML::LibXML;
use CGI::Session;
use CGI;
use utf8;
use charnames qw( :full :short );
use CGI::Carp qw(fatalsToBrowser);

do 'login.cgi';

$page=new CGI;
$currentPage=$page->param("pagina");
#controllo lo stato della sessione
$session = CGI::Session->load();
if($page->param('logout') eq "esci"){
	$session->close();
	$session->delete();
	$session->flush();
}

if($session->is_expired or $session->is_empty){
	$session = new CGI::Session;

	#controllo se la form e' stata gia settata
	if($page->param("submit")){
		$username = $page->param("username");
		$password = $page->param("password");
		if($username eq 'admin' and $password eq 'admin'){
			$session->param('login', 'admin');
			print $session->header(-location=>"amministraSezionePrivata.cgi");
			exit;
		}
		else{
			print "Content-type: text/html\n\n";
			my $pagLogin=&getLogin();
			$pagLogin=~ s/__ERRORE__/<p>Errore inserimento dati amminsitrazione<\/p>/;
			print $pagLogin;
			exit;
		}
	}
	else{

		print "Content-type: text/html\n\n";
		my $pagLogin=&getLogin();
		$pagLogin=~ s/__ERRORE__//;
		print $pagLogin;
		exit;
	}
}
else{
	print $session->header(-location=>"amministraSezionePrivata.cgi");
	exit;
}