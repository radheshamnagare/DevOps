
import psycopg2
#from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

con = psycopg2.connect("user=postgres password=''")
#con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);

cursor = con.cursor()

cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'python_db'")
exists = cursor.fetchone()
if not exists:
    cursor.execute('CREATE DATABASE python_db')

#cursor.execute('DROP DATABASE IF EXISTS python_db')
#cursor.execute('CREATE DATABASE python_db')

#name_Database   = "sampleData";

#sqlCreateDatabase = "create database "+name_Database+";"
#ursor.execute(sqlCreateDatabase);
con.close()


from fastapi import FastAPI
from routers import finmarka
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app = FastAPI(title = "Finmarka EndPoints")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(finmarka)

