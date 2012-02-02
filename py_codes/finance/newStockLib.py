#!/usr/bin/python
# -*- coding: utf-8 -*-
#author: diego tostes
#http://www.crummy.com/software/BeautifulSoup/documentation.html
import urllib
from xml.dom import minidom
from lxml import etree
from BeautifulSoup import BeautifulStoneSoup

def get_quote_from_instrument(instrument):
    url = "http://www.bmfbovespa.com.br/cotacoes2000/formCotacoesMobile.asp?codsocemi=%s"
    instrument_url = url % instrument
    texto = urllib.urlopen(instrument_url)
    soup = BeautifulStoneSoup(texto)
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

    return dic
    
def get_quote_from_instrument_list(instrument_list):
    list_2_return = []
    param = '|'.join(instrument_list)
    url2 = "http://www.bmfbovespa.com.br/Pregao-Online/ExecutaAcaoAjax.asp?CodigoPapel=%s" % param
    texto = urllib.urlopen(url2)
    soup = BeautifulStoneSoup(texto)
    infos = soup.findAll('papel')
    key_list = {"codigo":"code",
                "nome": "instrument",
                "ibovespa":"is_bovespa",
                "data":"date",
                "abertura":"open",
                "minimo":"min",
                "maximo":"max",
                "medio":"avg",
                "ultimo":"close",
                "oscilacao":"osc",
                "minino":"min2"}
    for info in infos:
        dic = {}
        for key in key_list:
            dic[key_list[key]] = info[key]
        list_2_return.append(dic)
        
    return list_2_return          
        
    
    
if __name__ == "__main__":
    pass
