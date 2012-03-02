#!/usr/bin/python
# -*- coding: utf-8 -*-
#author: diego tostes
#http://www.crummy.com/software/BeautifulSoup/documentation.html
import urllib
from xml.dom import minidom
from lxml import etree
from BeautifulSoup import BeautifulStoneSoup
import datetime

ibov_list = ["VALE5",
"OGXP3",
"ITUB4",
"BVMF3",
"BBDC4",
"BBAS3",
"GGBR4",
"PETR3",
"VALE3",
"PDGR3",
"USIM5",
"ITSA4",
"CYRE3",
"MRVE3",
"GFSA3",
"CSNA3",
"HYPE3",
"BRFS3",
"CIEL3",
"AMBV4",
"RDCD3",
"MMXM3",
"RSID3",
"LREN3",
"SANB11",
"LAME4",
"TIMP3",
"NATU3",
"CMIG4",
"PCAR4",
"ALLL3",
"TLPP4",
"FIBR3",
"GOAU4",
"BRAP4",
"JBSS3",
"BRML3",
"CCRO3",
"GOLL4",
"CSAN3",
"BISA3",
"ELPL4",
"MRFG3",
"TNLP4",
"BRKM5",
"ELET3",
"CPLE6",
"ECOD3",
"HGTX3",
"ELET6",
"LIGT3",
"CESP6",
"EMBR3",
"KLBN4",
"LLXL3",
"DTEX3",
"UGPA3",
"CRUZ3",
"TAMM4",
"BTOW3",
"USIM3",
"CPFE3",
"BRTO4",
"SBSP3",
"TNLP3",
"TRPL4",
"TMAR5",
"PETR4",
"RPMG4",
"RPMG3"]


micos_list = ["AGEN11",
"CTPC3",
"IMBI4",
"RPMG4",
"ARLA4",
"DHBI4",
"INET3",
"RSUL4",
"ATBS3",
"DOCA4",
"LARK4",
"SCLO4",
"BGPR3",
"DTCY3",
"LHER4",
"SJOS4",
"BIOM4",
"MAPT3",
"SNST3"
"BUET4",
"ESTR4",
"MILK11",
"SQRM4",
"CAFE4",
"FPXE4",
"MNPR3",
"STLB3",
"CALI3",
"FTRX4",
"NORD4",
"STRP4",
"CBMA4",
"GAFP4",
"OSXB4",
"TEFC11",
"CCHI4",
"GAZO4",
"PMET6",
"TEKA4",
"CELM3",
"GPCP3",
"PQTM4",
"TELB4"
"CMSA4",
"HAGA4",
"PSEG4",
"TENE5",
"CORR4",
"HETA4",
"RANI3",
"TROR4",
"CPFG4",
"HOOT4",
"RCSL4",
"TXRX4",
"CTAP3",
"IGBR3",
"RPMG4",
"UNCI3"
"VOES4"]

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
			dic["last_price"] = process_float_string(info["ultimo"])
			dic["osc"] = process_float_string(info["oscilacao"])
			dic["min2"] = process_float_string(info["minimo"])
			list_2_return.append(dic)
		except:
			pass
        
    return list_2_return
                
if __name__ == "__main__":
    #print get_quote_from_instrument_list(["goll4"])
    pass
