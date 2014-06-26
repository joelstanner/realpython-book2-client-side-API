# GET data from Rotten Tomatoes, parse, and write to database - top_rentals


import json
import requests
import sqlite3

YOUR_OWN_KEY="get_your_own"
url =  requests.get("http://api.rottentomatoes.com/api/public/v1.0/" +
                    "lists/dvds/top_rentals.json?apikey=%s" % (YOUR_OWN_KEY,))

# convert data from feed into binary
binary = url.content

# decode the json feed
output = json.loads(binary)

# grab the list of movies
movies = output["movies"]

with sqlite3.connect('movies.db') as connection:
    c = connection.cursor()
    
    # iterate through each movie and write to the db
    for movie in movies:
        c.execute("INSERT INTO top_rentals VALUES(?,?,?,?,?,?,?)",
                  (movie["title"], movie["year"], movie["mpaa_rating"],
                   movie["release_dates"]["dvd"], movie["runtime"],
                   movie["ratings"]["critics_score"],
                   movie["ratings"]["audience_score"]))
        
    # retrieve data
    c.execute("SELECT * FROM top_rentals ORDER BY title ASC")
    
    # fetchall() gets all the records from the query
    rows = c.fetchall()
    
    # output the rows to the screen, row by row
    for r in rows:
        print r[0], r[1], r[2], r[3], r[4], r[5], r[6]
    
    
    