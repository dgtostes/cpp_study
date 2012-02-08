from newStockLib import *
import sys
import os
import datetime
import math


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
    print "intrument: %s open: %.2f max: %.2f min: %.2f"\
          "  last_price: %.2f osc: %.2f slope: %s deg: %s" %  (dic_info['instrument'],
                                                 dic_info['open'],
                                                 dic_info['max'],
                                                 dic_info['min'],
                                                 dic_info['last_price'],
                                                 dic_info['osc'],
                                                 history_analysis(dic_info['instrument'], 
                                                                 'history_quotes.txt')['slope'],
                                                 history_analysis(dic_info['instrument'],
                                                                 'history_quotes.txt')['a_tan_deg']
                                                )
                                                 



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

def qsave(instrument_l, file2save):
    quote_info_list = get_quote_from_instrument_list(instrument_l)
    for dic_info in quote_info_list:
        line = "%s|%s|%.2f|%.2f|%.2f|%.2f|%.2f" % \
                                                (dic_info['date'],
                                                 dic_info['instrument'],
                                                 dic_info['open'],
                                                 dic_info['max'],
                                                 dic_info['min'],
                                                 dic_info['last_price'],
                                                 dic_info['osc'])

        write_line(file2save, line)

def write_line(file_2_write, line):
    f = open(file_2_write, 'a')
    f.write("%s\n" % line)
    f.close()        

def process_date_string(date_string):
    '''
    recieves a date string yyyy-mm-dd and
    return a datetime.date object
    '''
    date_list = date_string.split('-')
    year = int(date_list[0])
    month = int(date_list[1])
    day = int(date_list[2])
    return datetime.date(year, month,day) 


def generate_history_dic(history_file, instruments_list):
    #date|instrument|open|max|min|last_price|osc
    f = open(history_file,'r')
    i = f.readline()
    i = f.readline()#did this to skip from the head line
    history_dic = {}
    for instrument in instruments_list:
        history_dic[instrument.upper()] = {}
    while i:
        line = i.strip()
        line_list = line.split('|')
        date = process_date_string(line_list[0])
	instrument = line_list[1]
        open_price = float(line_list[2])
        max_price = float(line_list[3])
        min_price = float(line_list[4])
        close_price = float(line_list[5])
        osc = float(line_list[6])
	if instrument in instruments_list:
            history_dic[instrument][date] = {'open_price':open_price,
                                             'max_price':max_price,
                                             'min_price':min_price,
                                             'close_price':close_price,
                                             'osc':osc}
	i = f.readline()

    f.close()

    return history_dic

def best_line_apx(points_coor_list):
    '''
    recieves a list of tuples
    that represent points of a curve
    return a tuple the terms of the 
    line that best aprox of the curve 
    points. use the newton min sqt method
    '''

    sum_x=0
    sum_y=0
    sum_xx=0
    sum_xy=0
    n = len(points_coor_list)
    for coord in points_coor_list:
        x = coord[0]
        y = coord[1]
        sum_x=sum_x+x
        sum_y=sum_y+y
        xx=math.pow(x,2)
        sum_xx=sum_xx+xx
        xy=x*y
        sum_xy=sum_xy+xy

    #Calculating the coefficients
    try:
    	a=(-sum_x*sum_xy+sum_xx*sum_y)/(n*sum_xx-sum_x*sum_x)
    except:
        a = None
    try:    
	b=(-sum_x*sum_y+n*sum_xy)/(n*sum_xx-sum_x*sum_x)
    except:
        b = None

    try:
        arc_tan_rad = math.atan(b)
    except:
        arc_tan_rad = None

    try:
        arc_tan_deg = (180.0/3.14)*arc_tan_rad
    except:
        arc_tan_deg = None     
 
    return {'slope':b, 
            'linear_c':a, 
            'a_tan_rad':arc_tan_rad, 
            'a_tan_deg':arc_tan_deg}

    #print "The required straight line is Y=%sX+(%s)"%(b,a)

def history_analysis(instrument_string, history_file):
    instruments_list = [instrument_string]
    history_dic = generate_history_dic(history_file, 
                                       instruments_list)
    date_list = [i for i in history_dic[instrument_string]]
    date_list = sorted(date_list)
    coord_list = []
    for i in date_list:
        coord_list.append((date_list.index(i),
                           history_dic[instrument_string][i]['close_price']))

    return best_line_apx(coord_list)
					 
def main():
        current_dir = os.getcwd()
	if len(sys.argv) == 2:
		if sys.argv[1] == 'all':
			expose_quotes(ibov_list+micos_list)
		elif sys.argv[1] == 'ibov':
			expose_quotes(ibov_list)
		elif sys.argv[1] == 'micos':
			expose_quotes(micos_list)

		elif sys.argv[1] == 'analysis':
			print quote_analysis(ibov_list+micos_list)

                elif sys.argv[1] == 'qsave':
                        qsave(ibov_list+micos_list, current_dir+'/history_quotes.txt')
               
          	else:
			expose_quotes[eval(sys.argv[1])]

	elif len(sys.argv) == 3:
		if sys.argv[1] == 'single':
			expose_quotes([sys.argv[2]])

                elif sys.argv[1] == 'hanalysis':
                        instrument = sys.argv[2].upper()
                        print history_analysis(instrument,
                                                 current_dir+'/history_quotes.txt')
		elif sys.argv[1] == 'hdic':
                        instrument = sys.argv[2].upper()
                         
                        hdic = generate_history_dic(current_dir+'/history_quotes.txt', [instrument])
                        date_list = [i for i in hdic[instrument]]
                        date_list = sorted(date_list)
                        for date in date_list:
                            print "date: %s close: %s" % (date,hdic[instrument][date]['close_price'])
                        print 'arc: %s' % history_analysis(instrument,
                                                                 'history_quotes.txt')['a_tan_deg']
						 
if __name__ == "__main__":
	main()
        #print best_line_apx([(0,0),(1,2),(2,4),(3,6)])
        #print history_analysis('PETR4', 'history_quotes.txt')
