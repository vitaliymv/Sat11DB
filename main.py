import os
import sqlite3
import pandas as pd
import pandas.errors
from _1nf import _1nf_db

conn = sqlite3.connect("database.db")
cur = conn.cursor()

_1nf_db(cur)
conn.commit()

def show_table(name):
    df = pd.read_sql_query(f"SELECT * FROM {name}", conn)
    if df.empty:
        return
    print(f"====={name}=====")
    print(df)
    print()

tables = ["MMORPG1NF", "Players", "Characters", "Inventory", "Items", "Guilds"]

for t in tables:
    try:
        show_table(t)
    except pandas.errors.DatabaseError:
        pass

conn.close()
os.remove("database.db")