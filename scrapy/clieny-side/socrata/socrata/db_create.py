import sqlite3

conn = sqlite3.connect("project.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE data
               (name TEXT, url TEXT, views TEXT)
               """)