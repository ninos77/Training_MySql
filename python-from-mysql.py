import os
import datetime
import pymysql

username = os.getenv("C9_USER")

# connect to the database
connection = pymysql.connect(host = "localhost",
                            user = username,
                            password = "",
                            db = "Chinook")

try:
    # Run a query
    with connection.cursor() as cursor:
        row = ("Bob", 21, "2020-05-20 23:02:56")
        cursor.execute("Insert into Friends values(%s, %s, %s);", row)
        connection.commit()
finally:
    # close the connection to the db
    connection.close()

