import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# results = cur.execute('''
# DELETE FROM video_products
# WHERE release_year = 5;
# ''')

data = [
    (2, "Победа", "Фильм", 2009),
    (3, "Алиса в стране чудес", "Фильм", 2011)
]

results = cur.executemany(
    '''
    INSERT INTO IF NOT EXISTS video_products VALUES(?, ?, ?, ?);
    ''',
    data
)

con.commit()
# PRAGMA table_info(ice_cream)
con.close()