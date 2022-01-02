from datetime import date
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Date

class UserBase(BaseModel):
    user_id: int
    user_fname: str
    user_lname:str
    login_id: str
    password: str
    email: str
    contact_no: str

    class Config:
        orm_mode = True    

class new_user(BaseModel):
    user_fname: str
    user_lname:str
    login_id: str
    password: str
    email: str
    contact_no: str  

    class Config:
        orm_mode = True


################CONTRACT



class ContractBase(BaseModel):
    ticker: str
    contract_name:str
    market_name: str
    currency: float
    
    class Config:
        orm_mode = True    



class new_contract(BaseModel):
    ticker: str
    contract_name:str
    market_name: str
    currency: float
    
    class Config:
        orm_mode = True    


#SCANNER

class ScannerBase(BaseModel):
    scanner_id: int
    scanner_name: str
    platform_name:str
    
    class Config:
        orm_mode = True    


class new_scanner(BaseModel):
    scanner_name: str
    platform_name:str
    
    class Config:
        orm_mode = True    



#WATCHLIST

class WatchlistBase(BaseModel):
    watchlist_id: int
    watchlist_name: str
        
    class Config:
        orm_mode = True    


class new_watchlist(BaseModel):
    watchlist_name: str
        
    class Config:
        orm_mode = True    


#TEMPLATE

class TemplateBase(BaseModel):
    template_id: int
    template_title: str
    description: str
    types: str
    content: str
    created_at: date
    updated_at: date
        
    class Config:
        orm_mode = True    


class new_template(BaseModel):
    template_title: str
    description: str
    types: str
    content: str
    created_at: date
    updated_at: date
        
    class Config:
        orm_mode = True    




#NOTIFICATION

class NotificationBase(BaseModel):
    notification_id: int
    template_id: int
    types: str
    content: str
    created_at: date
    updated_at: date
        
    class Config:
        orm_mode = True    


class new_notification(BaseModel):
    template_id: int
    types: str
    content: str
    created_at: date
    updated_at: date
        
    class Config:
        orm_mode = True 

########  User_conditions

class User_conditionsBase(BaseModel):
    condition_id: int
    user_id: int
    watchlist_id: int
    scanner_id: int
    notification_id: int
    conditions: str

    class Config:
        orm_mode = True


class new_user_condition(BaseModel):
    user_id: int
    watchlist_id: int
    scanner_id: int
    notification_id: int
    conditions: str

    class Config:
        orm_mode = True
        
"""

#RAW_DATA

class RawDataBase(BaseModel):
    curr_date: Date
    ticker: str
    open:float
    high:float
    low:float
    close: float
    volume: int
    
    class Config:
        orm_mode = True    


class new_rawdata(BaseModel):
    curr_date: Date
    ticker: str
    open:float
    high:float
    low:float
    close: float
    volume: int
    
    class Config:
        orm_mode = True    
"""


