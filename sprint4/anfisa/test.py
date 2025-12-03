import sqlite3

con = sqlite3.connect('db.sqlite')

cur = con.cursor()

query_1 = '''
CREATE TABLE IF NOT EXISTS directors(
    id INTEGER PRIMARY KEY,
    full_name TEXT,
    birth_year INTEGER
);
'''
query_2 = '''
CREATE TABLE IF NOT EXISTS video_products(
    id INTEGER PRIMARY KEY,
    title TEXT,
    product_type TEXT,
    release_year INTEGER
);
'''

con.execute(query_1)
con.execute(query_2)

data = [
    (2, 'Крутецкий фильм', '550', 5),
    (3, 'Крутецкий фильм 2', '551', 5)
]

cur.executemany(
    'INSERT INTO video_products VALUES(?, ?, ?, ?);',
    data
)
con.commit()
con.close()