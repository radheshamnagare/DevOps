from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import Date, Float
#from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__= "users"
    user_id=Column(Integer, primary_key=True)
    user_fname=Column(String,nullable=False)
    user_lname=Column(String,nullable=False)
    login_id=Column(String,nullable=False)
    #hashed_password=Column(String,nullable=False)
    password=Column(String,nullable=False)
    email=Column(String,nullable=False)
    contact_no=Column(String)


class Contract(Base):
    __tablename__= "contract_info"
    ticker=Column(String, primary_key=True)
    contract_name=Column(String,nullable=False)
    market_name=Column(String,nullable=False)
    currency=Column(Float,nullable=False)


class Scanner(Base):
    __tablename__= "scanner"
    scanner_id=Column(Integer, primary_key=True)
    scanner_name=Column(String,nullable=False)
    platform_name=Column(String,nullable=False)


class Watchlist(Base):
    __tablename__= "watchlist"
    watchlist_id=Column(Integer, primary_key=True)
    watchlist_name=Column(String,nullable=False)
    

class Templates(Base):
    __tablename__= "templates"
    template_id=Column(Integer, primary_key=True)
    template_title=Column(String,nullable=False)
    description=Column(String,nullable=False)
    types=Column(String,nullable=False)
    content=Column(String,nullable=False)
    created_at=Column(Date,nullable=False)
    updated_at=Column(Date,nullable=False)



class Notifications(Base):
    __tablename__= "notifications"
    notification_id=Column(Integer, primary_key=True)
    template_id = Column(Integer, ForeignKey("templates.template_id"))
    types=Column(String,nullable=False)
    content=Column(String,nullable=False)
    created_at=Column(Date,nullable=False)
    updated_at=Column(Date,nullable=False)

class User_Conditions(Base):
    __tablename__= "user_conditions"
    condition_id= Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey("users.user_id"))
    watchlist_id=Column(Integer,ForeignKey("watchlist.watchlist_id"))
    scanner_id=Column(Integer, ForeignKey("scanner.scanner_id"))
    notification_id=Column(Integer, ForeignKey("notifications.notification_id"))
    conditions= Column(String, nullable=False)

    

"""
class RawData(Base):
    __tablename__= "raw_data"
    curr_date=Column(Date,nullable=False)
    #ticker=Column(String,primary_key=True)
    open=Column(Float,nullable=False)
    high=Column(Float,nullable=False)
    low=Column(Float,nullable=False)
    close=Column(Float,nullable=False)
    volume=Column(Integer,nullable=False)
"""

    


