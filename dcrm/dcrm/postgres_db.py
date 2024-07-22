# install postgres in system
# pip install psycopg2 

import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(
        user="mehul",
        password="mehul",
        host="localhost",
        port="5432",
        database="crm_db"
        )
    
    # Create a cursor to perform database operations
    cursor = connection.cursor()
    

except (Exception. Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")