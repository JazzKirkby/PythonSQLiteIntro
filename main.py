#imports sqlite3
import sqlite3
#creates the store DB
conn = sqlite3.connect('store')
#creates the table called pet
conn.execute("CREATE TABLE 'pet' (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), checkups SMALLINT UNSIGNED, birth DATE, death DATE)")
