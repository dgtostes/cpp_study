from newStockLib import *
import sys
import os
import datetime
import math
import urllib2

class Quotes(object):
	'''
	a class that receives a dic_info and
	a history quote file
	'''
	def __init__(self, dic_info, history_file):
		self.dic_info = dic_info
		self.history_file = history_file
		self.expose = self.__expose_dic()
		self.history_dic = self.__history_dic()
		self.history_line = self.__history_analysis()
		#self.gera_arquivo = self.__gera_arquivo()
		
		
	
	def __expose_dic(self):
		'''
		this method return a string 
		whith quote informations abou the instrument
		'''
		
		if self.__history_analysis():
			slope_quote = self.__history_analysis()['quote']['slope']
			a_tan_deg_quote = self.__history_analysis()['quote']['a_tan_deg']
			slope_vol = self.__history_analysis()['vol']['slope']
			a_tan_deg_vol = self.__history_analysis()['vol']['a_tan_deg']
		else:
			slope_quote = None
			a_tan_deg_quote = None
			slope_vol = None
			a_tan_deg_vol = None
					
		return "intrument: %s open: %.2f max: %.2f min: %.2f"\
			  " last_price: %.2f osc: %.2f slope: %.2f deg: %.2f"\
			  " slope_vol: %.2f deg_vol: %.2f" %  (self.dic_info['instrument'],
													 self.dic_info['open'],
													 self.dic_info['max'],
													 self.dic_info['min'],
													 self.dic_info['last_price'],
													 self.dic_info['osc'],
													 slope_quote,
													 a_tan_deg_quote,
													 slope_vol,
													 a_tan_deg_vol)
	def __history_dic(self):
		today = datetime.date.today()
		today_day = today.day
		today_month = today.month - 1
		today_year = today.year
		
		start = today - datetime.timedelta(days=7)
		start_day = start.day
		start_month = start.month -1
		start_year = start.year
		url_target = "http://ichart.finance.yahoo.com/"\
		             "table.csv?s=%s.SA&a=%s&b=%s&c=%s&d"\
		             "=%s&e=%s&f=%s&g=d&ignore=.csv" % (self.dic_info['instrument'],
														start_month,
				                                        start_day,
														start_year,
														today_month,
														today_day,
														today_year)
		try:
			response = urllib2.urlopen(url_target)
			html_list = (response.read()).split("\n")
			html_list.pop(0)
			html_list.pop(len(html_list)-1)
			history_dic = {}
			history_dic[self.dic_info['instrument']] = {}
			for i in html_list:
				data_list = i.split(',')
				date = process_date_string(data_list[0])
				history_dic[self.dic_info['instrument']][date] = {}		
				open_price = float(data_list[1])
				max_price = float(data_list[2])
				min_price = float(data_list[3])
				close_price = float(data_list[4])
				osc = close_price - open_price
				vol = float(data_list[5].replace(",",""))
				history_dic[self.dic_info['instrument']][date] = {
													 'max_price':max_price,
													 'min_price':min_price,
													 'close_price':close_price,
													 'osc':osc,
													 'vol':vol
													 }
														 
			return history_dic
		except:
			return None

	def __quote_save(self):
		'''
		this method save quote informations
		in the history_file file
		'''
		line = "%s|%s|%.2f|%.2f|%.2f|%.2f|%.2f" % (self.dic_info['date'],
                                                 self.dic_info['instrument'],
                                                 self.dic_info['open'],
                                                 self.dic_info['max'],
                                                 self.dic_info['min'],
                                                 self.dic_info['last_price'],
                                                 self.dic_info['osc'])
		
		write_line(self.history_file,line)
        

	
#	def __history_dic(self):
#		'''
#		this method return a history dictionary
#		from instrument using the history_file data
#		'''		
#		#date|instrument|open|max|min|last_price|osc
#		f = open(self.history_file,'r')
#		i = f.readline()
#		i = f.readline()#did this to skip from the head line
#		
#		history_dic = {}
#		history_dic[self.dic_info['instrument']] = {}
#		while i:
#			line = i.strip()
#			line_list = line.split('|')
#			instrument = line_list[1]
#			if instrument == self.dic_info['instrument']:
#				date = process_date_string(line_list[0])	    
#				open_price = float(line_list[2])
#				max_price = float(line_list[3])
#				min_price = float(line_list[4])
#				close_price = float(line_list[5])
#				osc = float(line_list[6])
#				history_dic[instrument][date] = {'open_price':open_price,
#												 'max_price':max_price,
#												 'min_price':min_price,
#												 'close_price':close_price,
#												 'osc':osc}
#													 
#			i = f.readline()
#		f.close()
#		return history_dic
		
	def __history_analysis(self):
		'''
		this method process the __history_dic
		generate a coordinate of the points of the 
		history quote curve and using the best_line_apx
		function, return informations about the best 
		Straight-Line Equation that that approximates the points
		of the quote curve
		'''
		instrument = self.dic_info['instrument']
		dic = {}
		if self.__history_dic():
			history_dic = self.__history_dic()
			date_list = [i for i in history_dic[instrument]]
			date_list = sorted(date_list)
			coord_list_quote = []
			coord_list_vol = []
			for i in date_list:
				coord_list_quote.append((date_list.index(i),history_dic[instrument][i]['close_price']))
				coord_list_vol.append((date_list.index(i),history_dic[instrument][i]['vol']))
			dic['quote'] = best_line_apx(coord_list_quote)
			dic['vol'] = best_line_apx(coord_list_vol)
			return dic	

		else:
			return None

		
def write_line(file2save, line):
	f = open(file2save, 'a')
	f.write("%s\n" % line)
	f.close()
                                                
def expose_quotes(instrument_l):
	quote_info_list = get_quote_from_instrument_list(instrument_l)
	for dic_info in quote_info_list:
		dic_info(quote_info)


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



if __name__ == "__main__":
	
	history_file = "history_quotes.txt"
	'''
	dic_list = get_quote_from_instrument_list(["PETR4"])
	print dic_list
	for dic_info in dic_list:
		quote = Quotes(dic_info, history_file)
		print quote.__history_dic()
	'''
	
	
	dic_list = get_quote_from_instrument_list(ibov_list+micos_list)
	for dic_info in dic_list:
		if dic_info['open'] > dic_info["last_price"]:
			qty = 2960/dic_info["last_price"]
			qty = int(qty / 100)*100
			if qty > 100:
				quote = Quotes(dic_info, history_file)
				print "\n"
				print quote.expose
				print "da para comprar %s" % qty
				lucro = qty * 0.01
				print "lucro de %.2f por centavo" % lucro
    
#	dic_list = get_quote_from_instrument_list(["PETR4"])
#	for dic_info in dic_list:
#		quote = Quotes(dic_info, history_file)
#		print quote.gera_arquivo