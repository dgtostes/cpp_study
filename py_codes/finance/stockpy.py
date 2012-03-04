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
    def __init__(self, instrument):
        self.instrument = instrument
        self.dic_info = self.__get_quote_from_instrument_list()[0]
        self.history_dic = self.__history_dic()
        self.expose = self.__expose_dic()
        self.history_line = self.__history_analysis()


    def __get_quote_from_instrument_list(self):
        instrument_list = [self.instrument]
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


            return dic

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

        return "intrument: %s open: %s max: %s min: %s"\
              " last_price: %s osc: %s slope: %s deg: %s"\
              " slope_vol: %s deg_vol: %s" %  (self.dic_info['instrument'],
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
        if self.history_dic:
            history_dic = self.history_dic
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

    def quote_analysis(self):
        instrument_l = [self.instrument]
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
                self._expose_dic(dic)

def write_line(file2save, line):
    f = open(file2save, 'a')
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
    q = Quotes("PETR4")
    print q.expose
