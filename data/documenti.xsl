<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:d="http://www.documenti.com" exclude-result-prefixes="d">
<xsl:output method='html' version='1.0' encoding='UTF-8' indent='yes'
doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"
doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" />

<xsl:template match="/">
<html xmlns="http://www.w3.org/1999/xhtml" version="-//W3C//DTD XHTML 1.1//EN" xml:lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
		<title>Documenti - Scherma Castelfranco Veneto</title>
		<meta name="description" content="Pagina che mostra i documenti che il Circolo di Scherma di Castefranco Veneto mette a disposizione come il regolamento o la dichiarazione di spese" />
		<meta name="author" content="Chiara Bigarella, Mirko Pavanello, Massimiliano Sartoretto, Paolo Tesser" />
		<meta name="keywords" content="circolo, scherma, documenti, informazioni, , Castelfranco Veneto" />
		<meta name="robots" content="index,follow" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<link rel="stylesheet" href="../css/stile.css " type="text/css"/>
		<xsl:text disable-output-escaping="yes">
			&lt;!--[if (IE 6)|(IE 7)|(IE 8)]&gt;
			&lt;link rel="stylesheet" href="../css/stileIE.css" type="text/css"/&gt;
			&lt;![endif]--&gt;
		</xsl:text>
		<link rel="stylesheet" href="../css/print.css" type="text/css" media="print" />
		<link rel="Shortcut Icon" href="../img/struttura/favicon.ico" type="image/x-icon" />
		<script  type="text/javascript" charset="UTF-8" src="../js/librerie/jquery-1.11.0.min.js" ></script>
		<script  type="text/javascript" charset="UTF-8" src="../js/script.js" ></script>
		<noscript>
			<link rel="stylesheet" href="../css/stilenojava.css" type="text/css"/>
		</noscript>
	</head>

	<body>
		<div id="header"></div>

		<div id="boxTop">Torna su</div>

		<p class="nascondi"><a href="#breadcrumb">Salta <span xml:lang="fr">menù</span> contenente anche il <span xml:lang="en">link</span> per l'accesso all'area riservata</a></p>

		<div id="nav">
			<div id="nav-1">
				<ul id="sezione-nav-1"><li id="image-menu" title="contiene immagine del menù per il mobile"></li></ul>
				<ul id="panel-nav-1">
					<li><a href="articoli.cgi" tabindex="1">ARTICOLO</a></li>
					<li id="active">DOCUMENTI</li>
					<li><a href="../storia.html" tabindex="2">STORIA</a></li>
					<li><a href="../staff.html" tabindex="3"><span xml:lang="en">STAFF</span></a></li>
					<li class="last-link"><a href="../corsi.html" tabindex="4">CORSI</a></li>
				</ul>
			</div>
			<div id="nav-2">
				<a href="amministra.cgi" tabindex="5">Area Riservata</a>
			</div>

		</div>

		<div id="breadcrumb">
			<p>Ti trovi in: Documenti</p>
		</div>

		<p class="nascondi"><a href="#sidebar">Salta contenuto e vai alla <span xml:lang="en">sidebar</span> contenente i <span xml:lang="en">link</span> ad altri siti di scherma, agli <span xml:lang="en">sponsor</span> e alla <span xml:lang="en">gallery</span></a></p>

		<div id="lista-documenti" class="nascondi" >
			<ul title="lista dei documenti mostrati nella pagina classificati per titolo raggiungibili direttamente accendendo al link">
				<xsl:for-each select="d:testi/d:documento[position()&#60;&#61;__DOC__]">
					<!-- mi salvo la variabile titolo che poi utilizzerò in href del link della lista -->
					<xsl:variable name="titolo"><xsl:value-of select="d:titolo"/></xsl:variable>

					<li><a href="#{$titolo}"><xsl:value-of select="$titolo" /></a></li>
				</xsl:for-each>
			</ul>
		</div>


		<!--  INIZIO SEZIONE "XSL" DA SISTEMARE -->
		<div id="content">
			<xsl:for-each select="d:testi/d:documento[position()&#60;&#61;__DOC__]">
				<!-- mi salvo la variabile titolo che poi utilizzerò in id della class document -->
				<xsl:variable name="titolo"><xsl:value-of select="d:titolo"/></xsl:variable>
				<xsl:variable name="doc-completo"><xsl:value-of select="d:doc-completo"/></xsl:variable>
				<div class="document" id="{$titolo}">
					<div class="sezione">
						<h1><xsl:value-of select="d:titolo" /></h1>
					</div>
					<div class="nascondi-articolo">
						<p><xsl:value-of select="d:paragrafo" /></p>
					</div>

					<p><a href="{$doc-completo}">Scarica documento [PDF] (<xsl:value-of select="d:dimensione" /> KB)</a></p> <!-- SISTEMARE -->
					<p class="nascondi-torna"><a href="#content">Torna al primo documento della pagina </a>o <a href="#nav">torna al <span xml:lang="fr">menù</span> di navigazione</a></p>

					<xsl:if test="__NDOC__&#62;5">
						<xsl:if test="position()&#61;(__DOC__-3)">
							<div id="anchor"></div>
						</xsl:if>
					</xsl:if>
				</div>
			</xsl:for-each>

			__MOSTRAPIU__

		</div>
		<!--  FINE SEZIONE -->

		<p class="nascondi"><a href="#nav">Torna al <span xml:lang="fr">menù</span> di navigazione</a></p>

		<div id="sidebar">
			<div id="sezione-sidebar"><p><span xml:lang="en">LINK</span> ESTERNI</p></div>
			<div id="panel-sidebar">
				<ul title="lista contenente dei link riferenti agli sponsor del circolo">
					<li><span xml:lang="en" class="desc-li">SPONSOR LINK</span>
						<ul>
							<li title="link che manda al sito della Fabbian, sponsor del circolo"><a href="http://www.fabbian.com/it" target="_blank">Fabbian</a></li>
							<li title="link che manda al sito della Goppion Caffè, sponsor del circolo"><a href="http://www.goppioncaffe.it" target="_blank">Goppion</a></li>
							<li title="link che manda al sito del Carminari, sponsor del circolo"><a href="http://www.carmimari.com" target="_blank">Carminari</a></li>
							<li title="link che manda al sito della Gnocchi Master, sponsor del circolo"><a href="http://www.gnocchimaster.com" target="_blank">Gnocchi <span xml:lang="en">Master</span></a></li>
						</ul>
					</li>
				</ul>
				<ul title="lista contenente dei link riferenti ad altri siti di scherma">
					<li><span class="desc-li">SCHERMA <span xml:lang="en">LINK</span></span>
						<ul>
							<li title="link che manda al sito della federazione internazionale di scherma"><a href="http://www.fie.ch" target="_blank"><abbr title="Federazione Internazionale Scherma">FIE</abbr></a></li>
							<li title="link che manda al sito della federazione italiana di scherma"><a href="http://www.federscherma.it/index.asp" target="_blank"><span xml:lang="en">Federal Scherma</span></a></li>
							<li title="link che manda al sito della federazione veneta di scherma"><a href="http://www.schermaveneto.it" target="_blank">Scherma Veneto</a></li>
							<li title="link che manda al sito del comune di Castelfranco Veneto"><a href="http://www.comune.castelfrancoveneto.tv.it" target="_blank">Comune Castelfranco Veneto</a></li>
						</ul>
					</li>
				</ul>

				<ul><li title="link che manda alla pagina Google Foto contenente tutte le immagine delle gare disputate dal circolo"><a href="https://plus.google.com/photos/100772179390595520915/albums?banner=pwa" target="_blank"><span xml:lang="en" class="desc-li">GALLERY</span></a></li></ul>
			</div>
		</div>

		<p class="nascondi"><a href="#nav">Torna al <span xml:lang="fr">menù</span> di navigazione</a></p>

		<div id="footer">
			<img class="footerElement" src="../img/struttura/valid-xhtml11.png" alt="immagine che indica che il sito web è valido come xhtml attraverso la verifica del W3C"/>
			<span class="footerElement">- L'intrusa - <span xml:lang="en">All rights reserved</span> - </span>
			<img class="footerElement" src="../img/struttura/vcss-blue.gif" alt="immagine che indica che lo stile applicato al sito web è valido come css attraverso la verifica del W3C"/>
		</div>

</body>
</html>

</xsl:template>
</xsl:stylesheet>