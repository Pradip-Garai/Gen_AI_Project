from Config.database_connection import conn
from Config.database_connection import cursor

def login(email,password):
    sql = "SELECT * FROM users WHERE EMAIL = %s AND PASSWORD = %s"
    value = (email,password)

    cursor.execute(sql, value)
    row = cursor.fetchone()

    if row:
      return row['NAME'] 
    else:
       return False

    cursor.close()
    conn.close()

def signup(name,email,password):
  sql = "INSERT INTO USERS (NAME,EMAIL,PASSWORD) VALUES (%s, %s, %s)"
  values = (name,email,password)

  cursor.execute(sql, values)
  conn.commit() 

