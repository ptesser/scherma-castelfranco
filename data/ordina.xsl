<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:a="http://www.articoli.com" exclude-result-prefixed="a ts">
<xsl:output method="xml" encoding="UTF-8"/>

<xsl:template match="/">
	<xsl:for-each select="//a:articolo">
		<xsl:sort select="a:data" orderd="descending"/>
		<xsl:copy-of select="current()"/>
	</xsl:for-each> 
</xsl:template>
</xsl:stylesheet>
