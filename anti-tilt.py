import json 
import psycopg2
from psycopg2 import sql 
import datetime as dt 

def main():
    database = 'example', 
    user = 'postgres',
    password = '', 
    host = 'host',
    port = 'port'
    

    def filter_emoton_threshold(emotion, threshold_value):
        
        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(
                dbname=database, user=user, password=password, host=host
            )

            cursor = connection.cursor()

            # Construct the SQL query using the provided column and threshold value
            query = sql.SQL("SELECT * FROM your_table WHERE {} > %s").format(sql.Identifier(emotion))
            
            # Execute the query with the threshold value as a parameter
            cursor.execute(query, (threshold_value,))

            # Fetch and print the results
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    
            # Close the cursor and connection
            cursor.close()
            connection.close()

        except psycopg2.Error as e:
            print("Error connecting to PostgreSQL:", e)
