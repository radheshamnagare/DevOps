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



def SAR(data):
    expectation_res = ""
    try:
        real = talib.SAR(data['High'],data['Low'], acceleration=0, maximum=0)
        data['SAR'] = real

        total_rows = data.shape[0]
        current_close = (data.iat[total_rows-1,3])
        SAR_value = (data.iat[total_rows-1,6])

        if(current_close > SAR_value):
            expectation_res = ("Current Close is Higher than current SAR Value")
        elif(current_close < SAR_value):
            expectation_res = ("Current Close is Lower than current SAR Value")
        else:
            expectation_res = ("Current Close is Equal to current SAR Value")
    
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
        action= params['SAR'][0]

     
        if(action != "SAR"):
            _input = loadInput(action)
            data = dataDownload(_input)
            res_data,expectation_res = SAR(data)
            logging.info(tabulate(res_data, headers = 'keys', tablefmt = 'fancy_grid'))    
            logging.info(expectation_res)     

        else:
            expectation_res = "Wrong Input"
        
           
        

    except Exception as error:
        logging.error(error.__str__())
    
    




