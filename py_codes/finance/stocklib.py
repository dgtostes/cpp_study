# -*- coding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup
from ystockquote import * 

url = "http://finance.yahoo.com/q?s=%s&ql=1"

general_ids = [
"yfs_market_time",
"yfs_pp0_^dji",
"yfs_pp0_^ixic",
"yfs_ad_",
"yfs_params_vcr",
]

not_used = [
"yfs_c10_",
"yfs_p20_",
"yfs_t10_",
]

instruments_id = [
"yfs_l10_",
"yfs_g00_",
"yfs_h00_",
"yfs_v00_",
]

def get_y_instrument(instrument, size_flag, stock_flag):
    if stock_flag == "br":
        if size_flag == "u":
            return (instrument+".SA").upper()
        elif size_flag == "l":
            return (instrument+".SA").lower()

    else:
        if size_flag == "u":
            return (instrument).upper()
        elif size_flag == "l":
            return (instrument).lower() 


def get_instrument_data(instrument, stock_flag):
    dic = {}
    dic["instrument"] = instrument
    target_url =  url % get_y_instrument(instrument, "l", stock_flag)
    request = urllib2.Request(target_url)
    response = urllib2.urlopen(request)
    document = response.read()

    #normaliza o documento para que o mesmo seja acessível via objetos
    soup = BeautifulSoup(document)

    

    ids_2_use_list = []#[i for i in general_ids]

    for i in instruments_id:
        ids_2_use_list.append(i+get_y_instrument(instrument, "l", stock_flag))

    minimized_instrument = get_y_instrument(instrument, "l", stock_flag)

    # retorna uma lista com todos os ids do documento
    for ids2 in ids_2_use_list:
        data = str(soup.findAll(id=ids2)).replace("</span>", "").replace("<span id=", "")
        data = data.replace('["', '').replace(']', '')
        data = data.replace('">', "|")
        try:
            if "yfs_l10_"+minimized_instrument in data:
                garbage = data.replace("|", ",").split(",")
                dic['price'] = float(garbage[1])
            

            elif "yfs_g00_"+minimized_instrument in data:
                garbage = data.split("|")
                dic['day_min'] = float(garbage[1])


            elif "yfs_h00_"+minimized_instrument in data:
                garbage = data.split("|")
                dic['day_max'] = float(garbage[1])


            elif "yfs_v00_"+minimized_instrument in data:
                garbage = data.split("|")
                dic['day_vol'] = float(garbage[1].replace(",",""))

        except:
            dic['price'] = float(get_pricce(get_y_instrument("PETR4", 'u', "br")))
            dic['day_min'] - None
            dic['day_max'] = None
            dic['day_vol'] = None

            

    span = soup.findAll("span")
    try:
        dic["min_52_week"] = float(str(span[30]).replace("<span>", "").replace("</span>",""))

    except:
        dic["min_52_week"] = None

    try:
        dic["max_52_week"] = float(str(span[31]).replace("<span>", "").replace("</span>",""))

    except:
        dic["max_52_week"] = None

                 
    return dic


def instrument_analyzer(instrument_data_dic):
    day_max_spread = instrument_data_dic["day_max"] - instrument_data_dic["price"]
    if day_max_spread <= 0:
        ver = ""
    else:
        ver = ""

##    return "%s"\
##          "(%s) "\
##          "- price: %s "\
##          "- day_min: %s "\
##          "- day_max: %s "\
##          "- day_max_spread: %s" % (ver,
##                                    instrument_data_dic["instrument"],
##                                    instrument_data_dic["price"],
##                                    instrument_data_dic["day_min"],
##                                    instrument_data_dic["day_max"],
##                                    day_max_spread)
    return (instrument_data_dic["instrument"],
            instrument_data_dic["price"],
            instrument_data_dic["day_min"],
            instrument_data_dic["day_max"],
            day_max_spread,
            instrument_data_dic["day_vol"])

def lower_than(instrument_data_dic, target_price):
    if instrument_data_dic["price"] <= target_price:
        return True
    else:
        return None
    


if __name__ == "__main__":
    instrument = "TNLP4"
    stock_flag = "br"
    #print get_instrument_data(instrument, stock_flag)
    instrument_analyzer(get_instrument_data(instrument, stock_flag))
    

    
