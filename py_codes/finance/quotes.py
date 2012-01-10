from ystockquote import * 
import os
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
"MILK11"]

                         
def generate_info_dict(instrument_list):
    STVH_dic = {}
    for instrument in instrument_list:
            instrument_Y = instrument+".SA"
            dic_p = get_all(instrument_Y)
            try:
                high = float(dic_p["52_week_high"])
            except:
                high = 0

            try:
                low = float(dic_p["52_week_low"])

            except:
                low = 0
                
            today_price = float(dic_p["price"])
            spread = high - low
            todayVhight = today_price - high
            if exclude_instrument(high, today_price):
                    STVH_dic[todayVhight] = {'instrument': instrument,
                                     'high_52': high,
                                     'low_52': low,
                                     'today': today_price}
    
    return STVH_dic
    

def exclude_instrument(high, today):
    if high - today <= 0.16:
        return False
    else:
        return True


def high_V_today(instrument_list):
    STVH_dic = generate_info_dict(instrument_list)
    
    lista_STVH = []
    for i in STVH_dic:
        if i not in lista_STVH:
            lista_STVH.append(i)


    lista_STVH = sorted(lista_STVH)

    for i in lista_STVH:
        if STVH_dic[i]['high_52'] != 0:

            if STVH_dic[i]['today'] < STVH_dic[i]['low_52']:
                check = "!!"

            elif (STVH_dic[i]['today'] > STVH_dic[i]['low_52']) and (STVH_dic[i]['today'] < (STVH_dic[i]['high_52']+STVH_dic[i]['low_52'])/2):
                check = "<"

            elif STVH_dic[i]['today'] > STVH_dic[i]['high_52']:
                check = "   OUT"
            else:
                check = ""
            
            print "%s - STVH (%s) - H: %s - L: %s - Today: %s %s" % (STVH_dic[i]['instrument'],
                                                             i,
                                                            STVH_dic[i]['high_52'],
                                                            STVH_dic[i]['low_52'],
                                                            STVH_dic[i]['today'],
                                                            check)   


portifolio_dic = {"oper1":{"instrument": "GOLL4",
                           "side": "B",
                           "qty": 100,
                           "price": 12.24,
                           "date": "2012-01-05",
                           "stop": {"qty": 100, "price": 13.40}},
                  "oper2":{"instrument": "TNLP4",
                           "side": "B",
                           "qty": 100,
                           "price": 17.90,
                           "date": "2012-01-06",
                           "stop": {"qty": 100, "price": 19.00}}
                  }

def oper_cost_value(qty, price):
    return (qty*price)

def portifolio_info(portifolio_dic):
    
    total_profit_and_loss = 0

    for i in portifolio_dic:
        instrument = portifolio_dic[i]["instrument"]
        side = portifolio_dic[i]["side"]
        qty = float(portifolio_dic[i]["qty"])
        price =  float(portifolio_dic[i]["price"])
        date =  portifolio_dic[i]["date"]
        stop_price =  float(portifolio_dic[i]["stop"]["price"])
        stop_qty =  float(portifolio_dic[i]["stop"]["qty"])
        
        operation_value = oper_cost_value(qty, price)


        #get yahoo quotes
        instrument_Y = instrument+".SA"
        market_dic = get_all(instrument_Y)
        price_today = float(market_dic["price"])
        operation_value_today = qty*price_today

        profit_loss = (operation_value_today - operation_value) - 12
        
        print "\n%s - %s" % (i, instrument)
        print "qty: %s - side: %s - price at (%s): %s" % (qty,
                                                          side,
                                                          date.replace("-", "/"),
                                                          price)
        print "operation : %s" % operation_value
        print "stop price: %.2f" % stop_price
        print "price today: %s" % price_today
        print "operation today: %s" % operation_value_today        
        print "profit / loss: %.2f (%.2f)" % (profit_loss,
                                          profit_loss/operation_value)
        

    total_profit_and_loss = total_profit_and_loss + profit_loss



    print "\n\ntotal profit and loss: %.2f" % total_profit_and_loss


def quote(quote_list):
    for i in quote_list:
        print "%s - %s" % (i,get_price(i+".SA"))

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == 'port':
            portifolio_info(portifolio_dic)
        elif sys.argv[1] == 'tips':
             high_V_today(ibov_list)
        elif sys.argv[1] == 'all':
            high_V_today(ibov_list)
            portifolio_info(portifolio_dic)             
    
        elif sys.argv[1] == 'qmicos':
            quote(micos_list)


    elif len(sys.argv) == 3:
        if sys.argv[2] == 'tips':
            high_V_today(eval(sys.argv[2]))

        elif sys.argv[2] == "quote":
            print sys.argv[2]
            quote(sys.argv[2])

if __name__ == "__main__":
   # high_V_today(micos_list)
   # portifolio_info(portifolio_dic)
   main()
   # high_V_today(micos_list)
    #quote(micos_list)
