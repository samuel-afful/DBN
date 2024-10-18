import sqlite3
import pandas as pd

con = sqlite3.connect("DentalCabinet.db")

#########################
#cur = con.cursor()
#cur.execute("SELECT name from sqlite_master WHERE type='table'")
#print(cur.fetchall())
#########################



query = "SELECT * FROM ProcedureItem"
df = pd.read_sql_query(query,con)

print(df.columns)
print(df)

#print(len(df.Name.unique()))

#cur.execute("SELECT name FROM sqlite_master;")
#tables = cur.fetchall()

#print(tables)
#cur.execute("SELECT * FROM InvoiceItem")
#print(cur.fetchall())
#table = cur.fetchall()
#print(table[0])
#cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
#print(cur.fetchall())

#cur.execute("PRAGMA table_info(PermissionPolicyNavigationPermissionsObject)")
#print(cur.fetchall())
