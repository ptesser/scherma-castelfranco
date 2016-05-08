#!/usr/bin/perl -w

use strict;
use XML::LibXSLT;
use XML::LibXML;
use CGI::Session;
use CGI;
use utf8;
use charnames qw( :full :short );
use CGI::Carp qw(fatalsToBrowser);
use File::Basename;
use Time::Local;
use DateTime;

do 'successo.cgi';
do 'eliminaDocumenti.cgi';
do 'modificaDocumento.cgi';
do 'inserisciDocumento.cgi';
do 'selezionaCosa.cgi';
do 'ordinaElementi.cgi';
do 'eliminaArticolo.cgi';
do 'modificaArticolo.cgi';
do 'inserisciArticolo.cgi';
do 'editor.cgi';
do 'login.cgi';

print "Content-type: text/html\n\n";
my $page=CGI->new();

#controllo lo stato della sessione
my $session = CGI::Session->load();
if($session->is_expired || $session->is_empty){
	print "<META HTTP-EQUIV='Refresh' CONTENT='0; URL=amministra.cgi'>";
}else{

#la sessione esiste e quindi posso far vedere quel che serve all'amministratore


#una volta scelto se inserire modificare o eliminare 
#scelgo se farlo in un articolo o documento e carico le form principali per ogni azione

if($page->param('Seleziona') eq 'inserisci')
{
	if($page->param('cosa') eq "documento"){

		&getEditorDocumento();
		exit;	
	}

	&getEditor();
	exit;	
	
	
}
if($page->param('Seleziona') eq 'modifica')
{
	if($page->param('cosa') eq "documento"){

		&doCaricaFormModificaDocumento();
		exit;	
	}

	&doCaricaFormModifica();
	exit;	

}
if($page->param('Seleziona') eq 'elimina')
{
	if($page->param('cosa') eq "documento"){

		&doCaricaFormEliminaDocumento();
		exit;	
	}

	&doCaricaFormElimina();
	exit;
}


# azioni che coinvologono il salvataggio, la modifica e l'eliminazione dall'xml


#azioni submit derivanti direttamente dalla pressione del submit permettono di inserire nuovi articoli o documenti
if($page->param('submit') eq "Inserisci Articolo"){

	&doInserimento();
	&ordinaElementi();
	&successo("Articolo","inserito","articoli");
	exit;
}

if($page->param('submit') eq "Inserisci Documento"){

	&doInserimentoDocumento();
	&successo("Documento","inserito","documenti");
	exit;
}


#azioni per caricare l'editor con i dati richiesti per la modifica di un articolo e 
#salvataggio dell'articolo modificato
if($page->param('modifica') eq "CaricaEditorArticolo"){

	&doCaricaEditorModifica();
	exit;	
}
if($page->param('modifica') eq "SalvaArticolo"){

	&doSalvaArticolo();
	&ordinaElementi();
	&successo("Articolo","modificato","articoli");
	exit;
}


#stessa cosa di sopra solo che fatto per i documenti
if($page->param('modifica') eq "CaricaEditorDocumento"){

	&doCaricaEditorModificaDocumento();
	exit;	
}
if($page->param('modifica') eq "SalvaDocumento"){

	&doSalvaDocumento();
	&successo("Documento","modificato","documenti");
	exit;
}



#eliminazione dei documenti scelti con il checkbox
if($page->param('elimina') eq 'EliminaDocumenti'){

	&doEliminaDocumenti();
	&successo("Documento/i","eliminato/i","documenti");
	exit;
}

#eliminazione degli articoli scelti con il checkbox
if($page->param('elimina') eq 'EliminaArticoli'){

	&doEliminaArticoli();
	&ordinaElementi();
	&successo("Articolo/i","eliminato/i","articoli");
	exit;
}

&getEditor();
exit;


}
