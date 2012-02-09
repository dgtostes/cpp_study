from newStockLib import *
import sys
import os
import datetime
import math

class Quotes(object):
	'''
	a class that receives a dic_info and
	a history quote file
	'''
	def __init__(self, dic_info, history_file):
		self.dic_info = dic_info
		self.history_file = history_file
		self.expose = self.__expose_dic()
		
	
	def __expose_dic(self):
		'''
		this method return a string 
		whith quote informations abou the instrument
		'''
		return "intrument: %s open: %.2f max: %.2f min: %.2f"\
			  "  last_price: %.2f osc: %.2f slope: %s deg: %s" %  (self.dic_info['instrument'],
													 self.dic_info['open'],
													 self.dic_info['max'],
													 self.dic_info['min'],
													 self.dic_info['last_price'],
													 self.dic_info['osc'],
													 self.__history_analysis()['slope'],
													 self.__history_analysis()['a_tan_deg'])
 
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
        

	def __history_dic(self):
		'''
		this method return a history dictionary
		from instrument using the history_file data
		'''		
		#date|instrument|open|max|min|last_price|osc
		f = open(self.history_file,'r')
		i = f.readline()
		i = f.readline()#did this to skip from the head line
		history_dic = {}
		history_dic[self.dic_info['instrument']] = {}
		while i:
			line = i.strip()
			line_list = line.split('|')
			instrument = line_list[1]
			if instrument == self.dic_info['instrument']:
				date = process_date_string(line_list[0])	    
				open_price = float(line_list[2])
				max_price = float(line_list[3])
				min_price = float(line_list[4])
				close_price = float(line_list[5])
				osc = float(line_list[6])
				history_dic[instrument][date] = {'open_price':open_price,
												 'max_price':max_price,
												 'min_price':min_price,
												 'close_price':close_price,
												 'osc':osc}
													 
			i = f.readline()
		f.close()
		return history_dic
		
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
		history_dic = self.__history_dic()
		date_list = [i for i in history_dic[instrument]]
		date_list = sorted(date_list)
		coord_list = []
		for i in date_list:
			coord_list.append((date_list.index(i),history_dic[instrument][i]['close_price']))
		return best_line_apx(coord_list)

		
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
	dic_list = get_quote_from_instrument_list(ibov_list+micos_list)
	for dic_info in dic_list:
		quote = Quotes(dic_info, history_file)
		print quote.expose

