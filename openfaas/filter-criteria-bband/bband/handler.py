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

# Function 10
def BBANDS(data,userTimeperiod,userInputValue):
    expectation_res = ""
    try:
        upperband, middleband, lowerband = talib.BBANDS(data['Close'], timeperiod=userTimeperiod, nbdevup=2, nbdevdn=2, matype=0)
        bollinger_Bandwidth = (upperband - lowerband)/middleband
        Function10 = (bollinger_Bandwidth / talib.EMA(data['Close'], timeperiod=userTimeperiod))*100
        data['Bandwidth'] = bollinger_Bandwidth
        data['EMA'] = talib.EMA(data['Close'], timeperiod=userTimeperiod)
        data['Function10'] = Function10

        total_rows = data.shape[0]
        current_value = (data.iat[total_rows-1,7])

        if(current_value > userInputValue):
            expectation_res = ("Current Value is Higher than User Input")
        elif(current_value < userInputValue):
            expectation_res = ("Current Value is Lower than User Input")
        else:
            expectation_res = ("Current Value is Equal to User Input")

    except Exception as error:
        logging.error(error.__str__())
 
    return data,expectation_res

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
        action= params['BBAND'][0]

     
        if(action != "BBAND"):
            _input = loadInput(action)
            data = dataDownload(_input)
            userTimeperiod= int(_input.get("time_period"))
            userInputValue=  float(_input.get("userInputValue"))
            res_data,expectation_res = BBANDS(data,userTimeperiod,userInputValue)
            logging.info(tabulate(res_data, headers = 'keys', tablefmt = 'fancy_grid'))    
            logging.info(expectation_res)     

        else:
            expectation_res = "Wrong Input"
        
           
        

    except Exception as error:
        logging.error(error.__str__())
    
    




