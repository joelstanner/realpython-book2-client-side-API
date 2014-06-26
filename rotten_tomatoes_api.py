# rotten_tomatoes_api.py


# create a SQLite3 database and table
import sqlite3

with sqlite3.connect("movies.db") as connection:
    c = connection.cursor()
    
    #create a table
    c.execute("""CREATE TABLE top_rentals
              (title TEXT, year INT, rating TEXT, release TEXT, runtime INT,
              critics_review INT, audience_review INT)""")
    
    