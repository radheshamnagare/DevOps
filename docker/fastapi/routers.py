
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import models
from database import SessionLocal, engine
from schemas import ContractBase,NotificationBase, User_conditionsBase, new_notification, ScannerBase, TemplateBase, UserBase, WatchlistBase, new_contract, new_scanner, new_template, new_user, new_user_condition, new_watchlist

models.Base.metadata.create_all(bind=engine)
finmarka = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#########   USER

@finmarka.get("/user/{user_id}", response_model=UserBase)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@finmarka.get("/users/", response_model= List[UserBase])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@finmarka.post("/users/insert/",response_model=new_user)
def add_user(user: new_user, db: Session = Depends(get_db)):
    db_user = crud.create_user(db=db, user=user)
    return {**user.dict() , 'user_id':db_user}

@finmarka.put("/users/update/{user_id}", response_model= new_user)
def user_update(user_id: int ,user: new_user, db: Session=Depends(get_db)):
    db_user = UserBase(user_id=user_id,user_fname=user.user_fname,user_lname=user.user_lname,login_id=user.login_id,password=user.password,email=user.email,contact_no=user.contact_no)
    crud.update_user(db=db,user_id=user_id, user=db_user)
    return{**user.dict(), 'user_id': db_user}

@finmarka.delete("/user/{user_id}",status_code=200)
def delete_user(user_id: int, db: Session=Depends(get_db)):
    crud.remove_user(db=db, user_id=user_id)
   

#############CONTRACT

@finmarka.get("/contract/{ticker}", response_model=ContractBase)
def read_contract(ticker: str, db: Session = Depends(get_db)):
    db_contract = crud.get_contract(db, ticker=ticker)
    if db_contract is None:
        raise HTTPException(status_code=404, detail="Contract not found")
    return db_contract


@finmarka.get("/contracts/", response_model= List[ContractBase])
def read_contracts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    contracts = crud.get_contracts(db, skip=skip, limit=limit)
    return contracts


@finmarka.post("/contracts/insert/",response_model=new_contract)
def add_contract(user: new_contract, db: Session = Depends(get_db)):
    db_contract = crud.create_contract(db=db, user=user)
    return {**user.dict() , 'user_id':db_contract}


@finmarka.put("/contract/update/{ticker}", response_model= new_contract)
def contract_update(ticker: str ,user: new_contract, db: Session=Depends(get_db)):
    db_contract = ContractBase(ticker=ticker,contract_name=user.contract_name,market_name=user.market_name,currency=user.currency)
    crud.update_contract(db=db,ticker=ticker, user=db_contract)
    return{**user.dict(), 'ticker': db_contract}


@finmarka.delete("/contract/{ticker}",status_code=200)
def delete_user(ticker: str, db: Session=Depends(get_db)):
    crud.remove_contract(db=db, ticker=ticker)





############SCANNER

@finmarka.get("/scanner/{scanner_id}", response_model=ScannerBase)
def read_scanner(scanner_id: int, db: Session = Depends(get_db)):
    db_scanner = crud.get_scanner(db, scanner_id=scanner_id)
    if db_scanner is None:
        raise HTTPException(status_code=404, detail="Scanner not found!!!")
    return db_scanner

@finmarka.get("/scanners/", response_model= List[ScannerBase])
def read_scanners(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_scanner = crud.get_scanners(db, skip=skip, limit=limit)
    return db_scanner


@finmarka.post("/scanner/insert/",response_model=new_scanner)
def add_scanner(user: new_scanner, db: Session = Depends(get_db)):
    db_scanner = crud.create_scanner(db=db, user=user)
    return {**user.dict() , 'scanner_id':db_scanner}


@finmarka.put("/scanner/update/{scanner_id}", response_model= new_scanner)
def scanner_update(scanner_id: int ,user: new_scanner, db: Session=Depends(get_db)):
    db_scanner = ScannerBase(scanner_id=scanner_id,scanner_name=user.scanner_name,platform_name=user.platform_name)
    crud.update_scanner(db=db,scanner_id=scanner_id, user=db_scanner)
    return{**user.dict(), 'scanner_id': db_scanner}


@finmarka.delete("/scanner/{scanner_id}",status_code=200)
def delete_scanner(scanner_id: int, db: Session=Depends(get_db)):
    crud.remove_scanner(db=db, scanner_id=scanner_id)




############WATCHLIST

@finmarka.get("/watchlist/{watchlist_id}", response_model=WatchlistBase)
def read_watchlist(watchlist_id: int, db: Session = Depends(get_db)):
    db_watchlist = crud.get_watchlist(db, watchlist_id=watchlist_id)
    if db_watchlist is None:
        raise HTTPException(status_code=404, detail="Watchlist not found!!!")
    return db_watchlist

@finmarka.get("/watchlists/", response_model= List[WatchlistBase])
def read_watchlists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_watchlist = crud.get_watchlists(db, skip=skip, limit=limit)
    return db_watchlist


@finmarka.post("/watchlist/insert/",response_model=new_watchlist)
def add_watchlist(user: new_watchlist, db: Session = Depends(get_db)):
    db_watchlist = crud.create_watchlist(db=db, user=user)
    return {**user.dict() , 'watchlist_id':db_watchlist}


@finmarka.put("/watchlist/update/{watchlist_id}", response_model= new_watchlist)
def watchlist_update(watchlist_id: int ,user: new_watchlist, db: Session=Depends(get_db)):
    db_watchlist = WatchlistBase(watchlist_id=watchlist_id, watchlist_name=user.watchlist_name)
    crud.update_watchlist(db=db,watchlist_id=watchlist_id, user=db_watchlist)
    return{**user.dict(), 'watchlist_id': db_watchlist}


@finmarka.delete("/watchlist/{watchlist_id}",status_code=200)
def delete_watchlist(watchlist_id: int, db: Session=Depends(get_db)):
    crud.remove_watchlist(db=db, watchlist_id=watchlist_id)



############TEMPLATE

@finmarka.get("/template/{template_id}", response_model=TemplateBase)
def read_template(template_id: int, db: Session = Depends(get_db)):
    db_template = crud.get_template(db, template_id=template_id)
    if db_template is None:
        raise HTTPException(status_code=404, detail="Template not found!!!")
    return db_template


@finmarka.get("/templates/", response_model= List[TemplateBase])
def read_templates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_template = crud.get_templates(db, skip=skip, limit=limit)
    return db_template


@finmarka.post("/templates/insert/",response_model=new_template)
def add_template(user: new_template, db: Session = Depends(get_db)):
    db_template = crud.create_template(db=db, user=user)
    return {**user.dict() , 'template_id':db_template}


@finmarka.put("/template/update/{template_id}", response_model= new_template)
def template_update(template_id: int ,user: new_template, db: Session=Depends(get_db)):
    db_template = TemplateBase(template_id=template_id, notification_id=user.notification_id, tempalte_title=user.template_title, description=user.description, types=user.types, content=user.content, created_at=user.created_at, updated_at=user.updated_at)
    crud.update_template(db=db,template_id=template_id, user=db_template)
    return{**user.dict(), 'template_id': db_template}


@finmarka.delete("/template/{template_id}",status_code=200)
def delete_template(template_id: int, db: Session=Depends(get_db)):
    crud.remove_template(db=db, template_id=template_id)





############NOTIFICATIONS

@finmarka.get("/notifications/{notification_id}", response_model=NotificationBase)
def read_notification(notification_id: int, db: Session = Depends(get_db)):
    db_notification = crud.get_notification(db, notification_id=notification_id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return db_notification


@finmarka.get("/notifications/", response_model= List[NotificationBase])
def read_notifications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_notification = crud.get_notifications(db, skip=skip, limit=limit)
    return db_notification


@finmarka.post("/notification/insert/",response_model=new_notification)
def add_notification(user: new_notification, db: Session = Depends(get_db)):
    db_notification = crud.create_notification(db=db, user=user)
    return {**user.dict() , 'notification_id':db_notification}


@finmarka.put("/notification/update/{notification_id}", response_model= new_notification)
def notification_update(notification_id: int ,user: new_notification, db: Session=Depends(get_db)):
    db_notification = NotificationBase(notification_id=notification_id,
    template_id=user.template_id ,
    types=user.types,
    content=user.content,
    created_at=user.created_at,
    updated_at=user.updated_at)
    crud.update_notification(db=db,notification_id=notification_id, user=db_notification)
    return{**user.dict(), 'notification_id': db_notification}


@finmarka.delete("/notification/{notification_id}",status_code=200)
def delete_notification(notification_id: int, db: Session=Depends(get_db)):
    crud.remove_notification(db=db, notification_id=notification_id)


####### USER_CONDITIONS

@finmarka.get("/conditions/{condition_id}", response_model=User_conditionsBase)
def read_conditions(condition_id: int, db: Session = Depends(get_db)):
    db_conditions = crud.get_condition(db, condition_id=condition_id)
    if db_conditions is None:
        raise HTTPException(status_code=404, detail="conditions not found")
    return db_conditions

@finmarka.get("/conditions/", response_model= List[User_conditionsBase])
def read_conditions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_conditions = crud.get_conditions(db, skip=skip, limit=limit)
    return db_conditions

@finmarka.post("/conditions/insert/",response_model=new_user_condition)
def add_condition(user: new_user_condition, db: Session = Depends(get_db)):
    db_conditions = crud.create_conditions(db=db, user=user)
    return {**user.dict() , 'condition_id':db_conditions}


@finmarka.put("/conditions/update/{condition_id}", response_model= new_user_condition)
def condition_update(condition_id: int ,user: new_user_condition, db: Session=Depends(get_db)):
    db_conditions = User_conditionsBase(condition_id=condition_id,
    user_id= user.user_id,
    watchlist_id= user.watchlist_id,
    scanner_id= user.scanner_id,
    notification_id= user.notification_id,
    conditions= user.conditions)
    crud.update_conditions(db=db, condition_id=condition_id, user=db_conditions)
    return{**user.dict(), 'condition_id': db_conditions}


@finmarka.delete("/conditions/{condition_id}",status_code=200)
def delete_conditions(condition_id: int, db: Session=Depends(get_db)):
    crud.remove_conditions(db=db, condition_id=condition_id)






"""
#RAW_DATA

@finmarka.get("/raw_data/", response_model= List[RawDataBase])
def read_rawdata(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rawdata = crud.get_rawdata(db, skip=skip, limit=limit)
    return rawdata


@finmarka.post("/raw_data/",response_model=new_rawdata)
def add_rawdata(user: new_rawdata, db: Session = Depends(get_db)):
    new_rawdata = crud.create_rawdata(db=db, user=user)
    return {**user.dict() , 'user_id':new_rawdata}
"""