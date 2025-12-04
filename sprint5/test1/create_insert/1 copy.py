import sqlite3

con = sqlite3.connect('test1/db.sqlite')
cur = con.cursor()

cur.execute('''
    SELECT tbl_name
    FROM sqlite_master
    WHERE type="table";
''')


for result in cur.fetchall():
    print(result[0])

con.close()
