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


# Function 2
def slope(data,userTimeperiod,userValueType,userInputValue,userInputAngle):
    expectation_res = ""
    try:
        real = talib.LINEARREG_SLOPE(data['Close'], timeperiod=userTimeperiod)
        data['Slope'] = real
        value1 = np.degrees(np.arctan(real))
        data['Degree of Slope'] = value1
        total_rows = data.shape[0]
    
        if(userValueType == 'slopeValue'):
            current_value = (data.iat[total_rows-1,6])
            if(current_value < userInputValue):
                expectation_res = "User input is Higher"
            elif(current_value > userInputValue):
                expectation_res = "User input is Lower"
            else:
                expectation_res = "User input is Equal"
        else:
            current_value = (data.iat[total_rows-1,7])
            if(current_value < userInputAngle):
                expectation_res = ("User input is Higher")
            elif(current_value > userInputAngle):
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
        action= params['SLOPE'][0]

     
        if(action != "SLOPE"):
            _input = loadInput(action)
            data = dataDownload(_input)
            userTimeperiod = int(_input.get("time_period"))
            userValueType = _input.get("userValueType")
            userInputValue = float(_input.get("userInputValue"))
            userInputAngle = float(_input("userInputAngle"))
            res_data,expectation_res = slope(data,userTimeperiod,userValueType,userInputValue,userInputAngle)
            logging.info(tabulate(res_data, headers = 'keys', tablefmt = 'fancy_grid'))    
            logging.info(expectation_res)     

        else:
            expectation_res = "Wrong Input"
        
           
        

    except Exception as error:
        logging.error(error.__str__())
    
    




