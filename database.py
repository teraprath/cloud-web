import sqlite3 as sql
from functions import getDate
import config

database = config.database
con = sql.connect(database, check_same_thread=False)
cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS files (file TEXT, size BLOB, date DATE)")
con.commit()

def insert(file: str, size):
    date = getDate()
    cursor.execute(f"INSERT INTO files VALUES ('{file}', '{size}', '{date}')")
    con.commit()

def delete(file: str):
    cursor.execute(f"DELETE FROM files WHERE file LIKE '{file}'")
    con.commit()

def fetchall():
    cursor.execute("SELECT * FROM files")
    res = cursor.fetchall()
    return res

def where(keyword):
    cursor.execute(f"SELECT * FROM files WHERE file LIKE '%{keyword}%'")
    res = cursor.fetchall()
    return res