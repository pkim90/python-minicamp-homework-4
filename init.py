import sqlite3

connection  = sqlite3.connect('database.db')
print ('Opened that shit! Fuck yeah!')

connection.execute('CREATE TABLE favorite_movies(name TEXT, favorite TEXT)')
print ('Made that fuckin table! Fuck yeah!')

connection.close()
