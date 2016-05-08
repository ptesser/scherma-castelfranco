<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:a="http://www.articoli.com" exclude-result-prefixes="a">
<xsl:output method='html' version='1.0' encoding='UTF-8' indent='yes'
doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"
doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" />

<xsl:template match="/">

<html lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
		<title>Articoli - Scherma Castelfranco Veneto</title>
		<meta name="description" content="Pagina che mostra gli articoli delle gare disputate dal Circolo di Scherma di Castefranco Veneto redatti dal presidente dell'associazione" />
		<meta name="author" content="Chiara Bigarella, Mirko Pavanello, Massimiliano Sartoretto, Paolo Tesser" />
		<meta name="keywords" content="circolo, scherma, articoli, news, notizie, Castelfranco Veneto" />
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

	<body onload="scrollTo()">
		<div id="header"></div>

		<div id="boxTop">Torna Su</div>

		<p class="nascondi">><a href="#breadcrumb">Salta <span lang="fr">menù</span> contenente anche il <span lang="en">link</span> per l'accesso all'area riservata</a></p>

		<div id="nav">
			<div id="nav-1">
				<ul id="sezione-nav-1"><li id="image-menu" title="contiene immagine del menù per il mobile"></li></ul>
				<ul id="panel-nav-1">
					<li id="active" >ARTICOLI</li>
					<li><a href="documenti.cgi" tabindex="1">DOCUMENTI</a></li>
					<li><a href="../storia.html" tabindex="2">STORIA</a></li>
					<li><a href="../staff.html" tabindex="3"><span lang="en">STAFF</span></a></li>
					<li class="last-link"><a href="../corsi.html" tabindex="4">CORSI</a></li>
				</ul>
			</div>
			<div id="nav-2">
				<a href="amministra.cgi" tabindex="5">Area Riservata</a>
			</div>

		</div>

		<div id="breadcrumb">
			<p>Ti trovi in: Articoli</p>
		</div>

		<p class="nascondi"><a href="#sidebar">Salta contenuto e vai alla <span lang="en">sidebar</span> contenente i <span lang="en">link</span> ad altri siti di scherma, agli <span lang="en">sponsor</span> e alla <span lang="en">gallery</span></a></p>

		<div id="lista-articoli" class="nascondi" >
			<ul title="lista degli articoli mostrati nella pagina classificati per luogo e data di svolgimento raggiungibili direttamente accendendo al link">
				<!-- <xsl:variable name="contatore">1</xsl:variable>-->
				<xsl:for-each select="a:testi/a:articolo[position()&#60;&#61;__ART__]">
					<xsl:sort select="a:data" order="descending"/>
					<!-- mi salvo la variabile titolo che poi utilizzerò in href del link della lista -->
					<xsl:variable name="titolo"><xsl:value-of select="a:titolo"/></xsl:variable>
					<xsl:variable name="luogo"><xsl:value-of select="a:luogo"/></xsl:variable>
					<xsl:variable name="data"><xsl:value-of select="a:data"/></xsl:variable>
					<xsl:variable name="luogo-data"><xsl:value-of select="$luogo" /> in data <xsl:value-of select="$data" /></xsl:variable>

					<li><a href="#{$luogo-data}"><xsl:value-of select="$luogo-data" /></a></li>
				</xsl:for-each>
			</ul>
		</div>

		<!--  INIZIO SEZIONE "XSL" DA SISTEMARE -->
		<div id="content">
			<xsl:for-each select="a:testi/a:articolo[position()&#60;&#61;__ART__]">
				<xsl:sort select="a:data" order="descending"/>

					<xsl:variable name="luogo"><xsl:value-of select="a:luogo"/></xsl:variable>
					<xsl:variable name="data"><xsl:value-of select="a:data"/></xsl:variable>
					<xsl:variable name="luogo-data"><xsl:value-of select="$luogo" /> in data <xsl:value-of select="$data" /></xsl:variable>
					<xsl:variable name="url">?artCompleto=on&amp;data=<xsl:value-of select="$data" />&amp;luogo=<xsl:value-of select="$luogo" /></xsl:variable>
					<xsl:variable name="src"><xsl:value-of select="a:img/@src"/></xsl:variable>
					<xsl:variable name="alt"><xsl:value-of select="a:img/@alt"/></xsl:variable>

					<div class="article" id="{$luogo-data}">
						<!--<div class="sezione" id="{$luogo-data}">-->
							<p><xsl:value-of select="a:data"/></p>
							<p><xsl:value-of select="a:luogo"/></p>
							<h1><xsl:value-of select="a:titolo"/></h1>
							<xsl:if test="a:img/@src and a:img/@alt">
								<img src="{$src}" alt="{$alt}" />
							</xsl:if>
						<!--</div>-->
						<p><a href="{$url}"> Vai all'articolo intero</a></p>
						<p class="nascondi-torna"><a href="#content">Torna al primo articolo della pagina </a>o <a href="#nav">torna al <span lang="fr">menù</span> di navigazione</a></p>

						<xsl:if test="__NART__&#62;8">
							<xsl:if test="position()&#61;(__ART__-4)">
								<div id="anchor"></div>
							</xsl:if>
						</xsl:if>
					</div>
			</xsl:for-each>
			__MOSTRAPIU__
		</div>
		<!--  FINE SEZIONE -->

		<p class="nascondi"><a href="#nav">Torna al <span lang="fr">menù</span> di navigazione</a></p>

		<div id="sidebar">
			<div id="sezione-sidebar"><p><span lang="en">LINK</span> ESTERNI</p></div>
			<div id="panel-sidebar">
				<ul title="lista contenente dei link riferenti agli sponsor del circolo">
					<li><span lang="en" class="desc-li">SPONSOR LINK</span>
						<ul>
							<li title="link che manda al sito della Fabbian, sponsor del circolo"><a href="http://www.fabbian.com/it" target="_blank">Fabbian</a></li>
							<li title="link che manda al sito della Goppion Caffè, sponsor del circolo"><a href="http://www.goppioncaffe.it" target="_blank">Goppion</a></li>
							<li title="link che manda al sito del Carminari, sponsor del circolo"><a href="http://www.carmimari.com" target="_blank">Carminari</a></li>
							<li title="link che manda al sito della Gnocchi Master, sponsor del circolo"><a href="http://www.gnocchimaster.com" target="_blank">Gnocchi <span lang="en">Master</span></a></li>
						</ul>
					</li>
				</ul>
				<ul title="lista contenente dei link riferenti ad altri siti di scherma">
					<li><span class="desc-li">SCHERMA <span lang="en">LINK</span></span>
						<ul>
							<li title="link che manda al sito della federazione internazionale di scherma"><a href="http://www.fie.ch" target="_blank"><abbr title="Federazione Internazionale Scherma">FIE</abbr></a></li>
							<li title="link che manda al sito della federazione italiana di scherma"><a href="http://www.federscherma.it/index.asp" target="_blank"><span lang="en">Federal Scherma</span></a></li>
							<li title="link che manda al sito della federazione veneta di scherma"><a href="http://www.schermaveneto.it" target="_blank">Scherma Veneto</a></li>
							<li title="link che manda al sito del comune di Castelfranco Veneto"><a href="http://www.comune.castelfrancoveneto.tv.it" target="_blank">Comune Castelfranco Veneto</a></li>
						</ul>
					</li>
				</ul>

				<ul><li title="link che manda alla pagina Google Foto contenente tutte le immagine delle gare disputate dal circolo"><a href="https://plus.google.com/photos/100772179390595520915/albums?banner=pwa" target="_blank"><span lang="en" class="desc-li">GALLERY</span></a></li></ul>
			</div>
		</div>

		<p class="nascondi"><a href="#nav">Torna al <span lang="fr">menù</span> di navigazione</a></p>

		<div id="footer">
			<img class="footerElement" src="../img/struttura/valid-xhtml11.png" alt="immagine che indica che il sito web è valido come xhtml attraverso la verifica del W3C"/>
			<span class="footerElement">- L'intrusa - <span lang="en">All rights reserved</span> - </span>
			<img class="footerElement" src="../img/struttura/vcss-blue.gif" alt="immagine che indica che lo stile applicato al sito web è valido come css attraverso la verifica del W3C"/>
		</div>


</body>
</html>
</xsl:template>
</xsl:stylesheet>