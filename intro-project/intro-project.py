#!/usr/bin/env python3

# To be able to get outside libraries or modules that don't come in by default.
import psycopg # type: ignore
import pyinotify # type: ignore

fileName = "./product.csv"

dbname = "your database name"
username = "your database username"
password = "your database password"
host = "your database host" # normally localhost
port = "your database port"

def monitoring():
    try: 
        with psycopg.connect(
            "dbname=" + dbname + " user=" + username + " password=" + password + " host=" + host + " port=" + port
        ) as connection: 
            with connection.cursor() as my_cursor:
                with open(fileName, 'r') as productFile:
                    for line in productFile.readlines():
                        values = line.split(",")
                        my_cursor.execute(
                            "INSERT INTO product (product_name, price) VALUES (%s, %s)", # Use placeholders to parameterize our query
                            (values[0], values[1])
                        )
                        
                print("products added to database successfully")

    except Exception as e:
        print("Error connecting to my db: ", e)


watching = pyinotify.WatchManager()
watching.add_watch(fileName, pyinotify.IN_CLOSE_WRITE, monitoring)
notifier = pyinotify.Notifier(watching)
notifier.loop()