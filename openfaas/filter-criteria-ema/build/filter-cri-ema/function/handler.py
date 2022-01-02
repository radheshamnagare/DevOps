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



# Function 1 
def Calc_EMA(data,time_period):
    try:
        real = talib.EMA(data['Close'], timeperiod=time_period)
        data['Calc_EMA'] = real
    except Exception as error:
        logging.error(error.__str__())
    
def Calc_Percent_EMA(data,timeperiod,userInputValue):
    expectation_res = ""
    try:
        Calc_EMA(data,timeperiod)
        total_rows = data.shape[0]
        PercentChangeValue_list = [] * total_rows
        for i in range(0,total_rows):
            if(i<timeperiod-1):
                PercentChangeValue_list.append("NaN")
                continue

            elif(i == total_rows-1):
                PercentChangeValue_list.append("NaN")
                continue

            else:    
                previousDay_value = data.iat[i-1,6]
                CurrentDay_value = data.iat[i,6]
                PercentChangeValue = ((CurrentDay_value - previousDay_value)/previousDay_value)*100
                PercentChangeValue_list.append(PercentChangeValue)

        data.insert(7," PercentChangeValue ",PercentChangeValue_list)
        current_value = (data.iat[i-1,7])
        if(current_value < userInputValue):
            expectation_res = "User input is Higher"
        elif(current_value > userInputValue):
            expectation_res = "User input is Lower"
        else:
            expectation_res = "User input is Equal"

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
        action= params['EMA'][0]

     
        if(action != 'EMA'):
            _input = loadInput(action)
            data = dataDownload(_input)
            time_period,userInputValue = int(_input.get("time_period")),float(_input.get("userInputValue"))
            res_data,expectation_res = Calc_Percent_EMA(data,time_period,userInputValue)
            logging.info(tabulate(res_data, headers = 'keys', tablefmt = 'fancy_grid'))    
            logging.info(expectation_res)    

        else:
            expectation_res = "Wrong Input"
        
           
        

    except Exception as error:
        logging.error(error.__str__())
    
    




