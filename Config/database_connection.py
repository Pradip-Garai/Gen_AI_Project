import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv() 

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MY_SQL_PASSWORD"),
    database=os.getenv("DATABASE_NAME")
)

cursor = conn.cursor(dictionary=True)

