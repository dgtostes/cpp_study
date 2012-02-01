#!/usr/bin/python
# -*- coding: utf-8 -*-
#author: diego tostes
#http://www.crummy.com/software/BeautifulSoup/documentation.html
import urllib
from xml.dom import minidom
from lxml import etree
from BeautifulSoup import BeautifulStoneSoup





url = "http://www.bmfbovespa.com.br/cotacoes2000/formCotacoesMobile.asp?codsocemi=%s"
instrument_url = url % "GOLL4"

texto = urllib.urlopen(instrument_url)
soup = BeautifulStoneSoup(texto)
#print BeautifulStoneSoup(texto, selfClosingTags=['papel']).prettify()
infos = soup.findAll('papel')
dic = {}
for info in infos:
    dic['desc'] = info['descricao']
    dic['instrument_code'] = info['codigo']
    dic['is_bov'] = info['ibovespa']
    dic['delay'] = info['delay']
    dic['hour'] = info['hora']
    dic['osc'] = info['oscilacao']
    dic['last_price'] = info['valor_ultimo']
    dic['vol'] = info['quant_neg']
    dic['market'] = info['mercado']

print dic
