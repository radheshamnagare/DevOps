import os
from urllib import parse
import modin.pandas as pd
import numpy as np
import csv
import json
import time
import talib
from talib import *
import logging
import yfinance as yf
import datetime
from statistics import mean,stdev,variance
from math import sqrt
from datetime import date
from yfinance import ticker
from urllib.parse import parse_qs
from urllib.parse import urlparse
from tabulate import tabulate

#logger config
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

# Function 8
def tStatTrueFalse(data,userTimeperiod,userTimeperiod1,criticalValue,userInputValue):
    expectation_res = ""
    try:
        total_rows = data.shape[0]
        list2 = []
        list2.append("NaN")
        for i in range (0,total_rows-1):
            
            if(i < userTimeperiod1+userTimeperiod-1):
                list2.append("NaN")
            else:
                list1 = []
                for j in range(0,userTimeperiod):
                    list1.append(data.iat[i-j,5])
                list3 = []
                for j in range(0,userTimeperiod1):
                    list3.append(data.iat[(i-userTimeperiod)-j,5])

                tuple1 = tuple(list1)
                tuple3 = tuple(list3)
                mean_tuple1 = mean(tuple1)
                mean_tuple3 = mean(tuple3)

                var1 = variance(tuple1)
                var2 = variance(tuple3)

                if(var2 > var1):
                    value = var2/var1
                    if(value > criticalValue):
                        varianceIs = "Unequal"
                    else:
                        varianceIs = "Equal"
                else:
                    value = var1/var2
                    if(value > criticalValue):
                        varianceIs = "Unequal"
                    else:
                        varianceIs = "Equal"

                if(varianceIs == "Unequal"):
                    tStat = (mean_tuple1 - mean_tuple3) / (sqrt((var1/userTimeperiod)+(var2/userTimeperiod1)))
                    list2.append(tStat)
                else:
                    pooledVariance = (((userTimeperiod - 1) * var1) + ((userTimeperiod1 - 1) * var2)) / (userTimeperiod + userTimeperiod1 - 2)
                    tStat = (mean_tuple1 - mean_tuple3) / (sqrt((pooledVariance/userTimeperiod)+(pooledVariance/userTimeperiod1)))
                    list2.append(tStat)

        data.insert(6," tStatTrueFalse ",list2)

        current_value = (data.iat[total_rows-1,6])
        
        if(current_value < userInputValue):
            expectation_res = ("User input is Higher")
        elif(current_value > userInputValue):
            expectation_res = ("User input is Lower")
        else:
            expectation_res = ("User input is Equal")

    except Exception as error:
        logging.error(error.__str__())
 
    return data,expectation_res




def _dataDownload(ticker,Previous_Date,today,interval):
    data = None
    try:
        data = yf.download(ticker, start= Previous_Date, end=today, progress=False, group_by='tickers',interval=interval)
    except Exception as error:
        logging.error(error.__str__())
    #to return download data    
    return data    


def loadInput(req):
    _input = None
    try:
     _input = json.loads(req)
    except Exception as error:
        logging.error(error.__str__())
    
    return _input

def dataDownload(_input):
    data = None
    try:
        ticker = _input.get("ticker")
        date_range   = int(_input.get("date_range"))
        interval = _input.get("interval")
        today = date.today()
        Previous_Date = date.today() - datetime.timedelta(days=date_range)
        data =  _dataDownload(ticker,Previous_Date,today,interval)  
    except Exception as error :
        logging.error(error.__str__())
    return data    


def handle(req):
   
    action = None
    res_data=None
    expectation_res=" "
    try:
        #parsing query string
        query = os.environ['Http_Query']
        params = parse_qs(query)
        action= params['TSTATTRUEFALSE'][0]

     
        if(action != "TSTATTRUEFALSE"):
            _input = loadInput(action)
            data = dataDownload(_input)
            userTimeperiod = int(_input.get("time_period"))
            userTimeperiod1 = int(_input.get("prev_time_period"))
            criticalValue = float(_input.get("criticalValue"))
            userInputValue = float(_input.get("userInputValue"))
            res_data,expectation_res = tStatTrueFalse(data,userTimeperiod,userTimeperiod1,criticalValue,userInputValue)
            logging.info(tabulate(res_data, headers = 'keys', tablefmt = 'fancy_grid'))    
            logging.info(expectation_res)     

        else:
            expectation_res = "Wrong Input"
        
           
        

    except Exception as error:
        logging.error(error.__str__())
    
    




