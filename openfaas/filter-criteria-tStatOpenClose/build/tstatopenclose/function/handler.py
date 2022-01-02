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

# Function 7
def tStatOpenClose(data,userTimeperiod,userInputValue):
    expectation_res = ""
    try:
        data['Close-Open'] = data['Close'] - data['Open']
        total_rows = data.shape[0]
        list2 = []
        list2.append("NaN")
        for i in range (0,total_rows-1):
            
            if(i < userTimeperiod-1):
                list2.append("NaN")
            else:
                list1 = []
                for j in range(0,userTimeperiod):
                    list1.append(data.iat[i-j,6])

                tuple1 = tuple(list1)
                mean_tuple1 = mean(tuple1)
                sd = stdev(tuple1)
                sem = sd / sqrt(userTimeperiod)
                hypo_mean = (data.iat[i+1,6])
                tStat = (mean_tuple1-hypo_mean)/sem
                list2.append(tStat)
        
        data.insert(7," tStatCloseOpen ",list2)
        
        current_value = (data.iat[total_rows-1,7])
        
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
        action= params['TSTATOPENCLOSE'][0]

     
        if(action != 'TSTATOPENCLOSE'):
            _input = loadInput(action)
            data = dataDownload(_input)
            userTimeperiod=int(_input.get("time_period"))
            userInputValue=float(_input.get("userInputValue"))
            res_data,expectation_res = tStatOpenClose(data,userTimeperiod,userInputValue)
            logging.info(tabulate(res_data, headers = 'keys', tablefmt = 'fancy_grid'))    
            logging.info(expectation_res)     

        else:
            expectation_res = "Wrong Input"
        
           
        

    except Exception as error:
        logging.error(error.__str__())
    
    




