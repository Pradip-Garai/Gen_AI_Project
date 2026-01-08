import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv() 

# For Streamlit Cloud, use environment variables. Default to localhost for local development
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("MY_SQL_PASSWORD")
DB_NAME = os.getenv("DATABASE_NAME")

try:
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor(dictionary=True)
except mysql.connector.Error as e:
    print(f"Database connection error: {e}")
    conn = None
    cursor = None

