import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

results = cur.execute('''
    SELECT
        product_type,
        COUNT(*),
        MAX(release_year)
    FROM 
        video_products
    WHERE release_year > 1929
    GROUP BY 
        product_type
    HAVING MAX(release_year) < 2012
    ORDER BY title
    LIMIT 2 OFFSET 0;
''')

# PRAGMA table_info(ice_cream)

for result in results.fetchall():
    print(result)

con.close()
