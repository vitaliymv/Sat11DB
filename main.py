import os
import sqlite3
import pandas as pd
import pandas.errors
from _1nf import _1nf_db
from _2nf import _2nf_db
from _3nf import _3nf_db
from task import task
import time

conn = sqlite3.connect("database.db")
cur = conn.cursor()

task(cur)
conn.commit()

def show_table(name):
    start_time = time.time()
    df = pd.read_sql_query(f"SELECT * FROM {name}", conn)
    if df.empty:
        return
    print(f"====={name}=====")
    print(df)
    print()
    print(time.time() - start_time)

tables = ["MMORPG1NF", "Players", "Characters", "Inventory", "Items", "Guilds"]

for t in tables:
    try:
        show_table(t)
    except pandas.errors.DatabaseError:
        pass

conn.close()
os.remove("database.db")