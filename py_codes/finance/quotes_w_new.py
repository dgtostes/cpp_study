from newStockLib import *
import sys

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


micos_list = ["KELP3",
"BMIN4",
"SNSYS5",
"EUCA4",
"AGEN11",
"MNDL4",
"ECOD3",
"FINAM11",
"OGXP3",
"TOYB4",
"MILK11",
"SULA11",
"DROG3",
"IDNT3",
"AMAR3",
"AMIL3",
"FRAS4",
"CTKA4",
"BTTL4",
"VLID3"
]


def expose_dic(dic_info):
    print "intrument: %s open: %.2f max: %.2f min: %.2f  last_price: %.2f osc: %.2f" % \
                                                (dic_info['instrument'],
                                                 dic_info['open'],
                                                 dic_info['max'],
                                                 dic_info['min'],
                                                 dic_info['last_price'],
                                                 dic_info['osc'])



def expose_quotes(instrument_l):
	quote_info_list = get_quote_from_instrument_list(instrument_l)
	for quote_info in quote_info_list:
		expose_dic(quote_info)


def quote_analysis(instrument_l):
	quote_info_list = get_quote_from_instrument_list(instrument_l)
	dic_osc = {}
        dic_price = {}
	for quote_info in quote_info_list:
		try:
			dic_osc[quote_info['osc']].append(quote_info)
		except:
			dic_osc[quote_info['osc']] = [quote_info]

	order_osc_list = sorted([i for i in dic_osc])
        
	for osc in order_osc_list:
		for dic in dic_osc[osc]:
			expose_dic(dic)
	

						 
def main():
	if len(sys.argv) == 2:
		if sys.argv[1] == 'all':
			expose_quotes(ibov_list+micos_list)
		elif sys.argv[1] == 'ibov':
			expose_quotes(ibov_list)
		elif sys.argv[1] == 'micos':
			expose_quotes(micos_list)

		elif sys.argv[1] == 'analysis':
			print quote_analysis(ibov_list+micos_list)
		else:
			expose_quotes[eval(sys.argv[1])]

	elif len(sys.argv) == 3:
		if sys.argv[1] == 'single':
			expose_quotes([sys.argv[2]])

						 
if __name__ == "__main__":
	main()
