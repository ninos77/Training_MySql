import os
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
        sql = "Select * from Artist limit 5;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # close the connection to the db
    connection.close()

