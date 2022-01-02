


# Function 5
def volume(data,userInputValue):
    expectation_res = ""
    try:
        total_rows = data.shape[0]
        PercentChangeValue_list = [] * total_rows
        for i in range(0,total_rows):
            if(i == 0):
                PercentChangeValue_list.append("NaN")
                continue

            else:    
                previousDay_value = data.iat[i-1,5]
                CurrentDay_value = data.iat[i,5]
                PercentChangeValue = ((CurrentDay_value / previousDay_value)*100)-100
                PercentChangeValue_list.append(PercentChangeValue)

        data.insert(6," PercentChangeValue ",PercentChangeValue_list)
        current_value = (data.iat[i,6])
        
        if(current_value < userInputValue):
            expectation_res = ("User input is Higher")
        elif(current_value > userInputValue):
            expectation_res = ("User input is Lower")
        else:
            expectation_res = ("User input is Equal")
 
    except Exception as error:
        logging.error(error.__str__())
 
    return data,expectation_res


# Function 6
def tStatVolume(data,userTimeperiod,userInputValue):
    expectation_res = ""
    try:
        total_rows = data.shape[0]
        list2 = []
        list2.append("NaN")
        
        for i in range (0,total_rows-1):
            
            if(i < userTimeperiod-1):
                list2.append("NaN")
            else:
                list1 = []
                for j in range(0,userTimeperiod):
                    list1.append(data.iat[i-j,5])

                tuple1 = tuple(list1)
                mean_tuple1 = mean(tuple1)
                sd = stdev(tuple1)
                sem = sd / sqrt(userTimeperiod)
                hypo_mean = (data.iat[i+1,5])
                tStat = (mean_tuple1-hypo_mean)/sem
                list2.append(tStat)
        
        data.insert(6," tStatVolume ",list2)

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




# Function 9
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




  elif(params['SLOPE'][0] !="'SLOPE'"):
            action = params['SLOPE'][0]
            _input = loadInput(action)
            data = dataDownload(_input)
            time_period  = int(_input.get("time_period"))
            userValueType  = _input.get("userValueType")
            userInputValue = float(_input.get("userInputValue"))
            userInputAngle = float(_input.get("userInputAngle"))
            res_data,expectation_res = slope(data,time_period,userValueType,userInputValue,userInputAngle)
            logging.info(tabulate(res_data, headers = 'keys', tablefmt = 'fancy_grid'))    
            logging.info(expectation_res)

        elif(params['AROONUP'][0] !="'AROONUP'"):
            action = params['AROONUP'][0]
            _input = loadInput(action)
            data = dataDownload(_input)
            time_period  = int(_input.get("time_period"))
            userValueType  = _input.get("userValueType")
            userInputValue = float(_input.get("userInputValue"))
            res_data,expectation_res = aroon(data,time_period,userValueType,userInputValue)
            logging.info(tabulate(res_data, headers = 'keys', tablefmt = 'fancy_grid'))    
            logging.info(expectation_res)    
        
        elif(params['AROONDOWN'][0] != "'AROONDOWN'"):
            action = params['AROONDOWN'][0]
            _input = loadInput(action)
            data = dataDownload(_input)
            time_period  = int(_input.get("time_period"))
            userValueType  = _input.get("userValueType")
            userInputValue = float(_input.get("userInputValue"))
            res_data,expectation_res = aroon(data,time_period,userValueType,userInputValue)
            logging.info(tabulate(res_data, headers = 'keys', tablefmt = 'fancy_grid'))    
            logging.info(expectation_res)

        elif(params['VOLUME'][0] !="'VOLUME'"):
            action = params['VOLUME'][0]
            _input = loadInput(action)
            data = dataDownload(_input)
            userInputValue = float(_input.get("userInputValue"))
            res_data,expectation_res = volume(data,userInputValue)
            logging.info(tabulate(res_data, headers = 'keys', tablefmt = 'fancy_grid'))    
            logging.info(expectation_res)    

        elif(params['tStatVolume'][0] !="'tStatVolume'"):
            action = params['tStatVolume'][0]
            _input = loadInput(action)
            data = dataDownload(_input)
            time_period  = int(_input.get("time_period"))
            userInputValue = float(_input.get("userInputValue"))
            res_data,expectation_res = tStatVolume(data,time_period,userInputValue)
            logging.info(tabulate(res_data, headers = 'keys', tablefmt = 'fancy_grid'))    
            logging.info(expectation_res)

        elif(params['tStatOpenClose'][0] !="'tStatOpenClose'"):
            action = params['tStatOpenClose'][0]
            _input = loadInput(action)
            data = dataDownload(_input)
            time_period  = int(_input.get("time_period"))
            userInputValue = float(_input.get("userInputValue"))
            res_data,expectation_res = tStatOpenClose(data,time_period,userInputValue)
            logging.info(tabulate(res_data, headers = 'keys', tablefmt = 'fancy_grid'))    
            logging.info(expectation_res)   

        elif(params['tStatTrueFalse'][0] !="'tStatTrueFalse'"):
            action = params['tStatTrueFalse'][0]
            _input = loadInput(action)
            data = dataDownload(_input)
            time_period  = int(_input.get("time_period"))
            prev_time_period = int(_input.get("prev_time_period"))
            criticalValue  = float(_input.get("criticalValue"))
            userInputValue = float(_input.get("userInputValue"))
            res_data,expectation_res = tStatTrueFalse(data,time_period,prev_time_period,criticalValue,userInputValue)
            logging.info(tabulate(res_data, headers = 'keys', tablefmt = 'fancy_grid'))    
            logging.info(expectation_res)

        elif(params['SAR'][0] !="'SAR'"):
            action = params['SAR'][0]
            _input = loadInput(action)
            data = dataDownload(_input)
            res_data,expectation_res = SAR(data)
            logging.info(tabulate(res_data, headers = 'keys', tablefmt = 'fancy_grid'))    
            logging.info(expectation_res)    

        elif(params['BBANDS'][0] !="'BBANDS'"):
            action = params['BBANDS'][0]
            _input = loadInput(action)
            data = dataDownload(_input)
            time_period  = int(_input.get("time_period"))
            userInputValue = float(_input.get("userInputValue"))
            res_data,expectation_res = BBANDS(data,time_period,userInputValue)
            logging.info(tabulate(res_data, headers = 'keys', tablefmt = 'fancy_grid'))    
            logging.info(expectation_res)
            
