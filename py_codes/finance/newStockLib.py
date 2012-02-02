#!/usr/bin/python
# -*- coding: utf-8 -*-
#author: diego tostes
#http://www.crummy.com/software/BeautifulSoup/documentation.html
import urllib
from xml.dom import minidom
from lxml import etree
from BeautifulSoup import BeautifulStoneSoup
import datetime

def process_float_string(float_string):
	if "," in float_string:
		float_string = float_string.replace(",",".")
	return float(float_string)
	
def process_bovespa_xml_date_string(bovespa_xml_date_string):
	date_string = bovespa_xml_date_string[0:10]
	try:
		date_list = date_string.split("/")
		day = int(date_list[0])
		month = int(date_list[1])
		year = int(date_list[2])
		return datetime.date(year,month,day)
	except:
		return datetime.date.today()
	
	

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
    for info in infos:
		try:
			dic = {}
			dic["instrument"] = info["codigo"].strip()
			dic["name"] = info["nome"]
			dic["is_bovespa"] = info["ibovespa"]
			dic["date"] = process_bovespa_xml_date_string(info["data"])
			dic["open"] = process_float_string(info["abertura"])
			dic["min"] = process_float_string(info["minimo"])
			dic["max"] = process_float_string(info["maximo"])
			dic["avg"] = process_float_string(info["medio"])
			dic["close"] = process_float_string(info["ultimo"])
			dic["osc"] = process_float_string(info["oscilacao"])
			dic["min2"] = process_float_string(info["minimo"])
			list_2_return.append(dic)
		except:
			pass
        
    return list_2_return
                
if __name__ == "__main__":
    #print get_quote_from_instrument_list(["goll4"])
    pass
