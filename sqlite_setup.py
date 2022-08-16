import sqlite3

conn=sqlite3.connect("accounts.db")
c=conn.cursor()

#c.execute("""CREATE TABLE account_list(
#        account_owner TEXT NOT NULL
#) """)
#conn.commit()

c.execute("SELECT * FROM account_list")
print(c.fetchall())
