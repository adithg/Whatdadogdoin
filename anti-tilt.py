import json 
import psycopg2
from psycopg2 import sql 
import datetime as dt 
import mindsdb_sdk


def main():
    connection_params = {
        'database': 'Midas', 
        'user': 'postgres',
        'password' : 'password', 
        'host' : '6.tcp.us-cal-1.ngrok.io',
        'port' : 16376
    }
    
    server = mindsdb_sdk.connect()
    
    def create_crypto_tables():
        try:
            # Establish a connection to the PostgreSQL server
            conn = psycopg2.connect(
                **connection_params
            )

            # Create a cursor
            cursor = conn.cursor()

            # List of cryptocurrencies to create tables for
            cryptocurrencies = ['btc', 'eth', 'xrp', 'doge']

            for crypto in cryptocurrencies:
                # SQL query to create tables
                create_table_query = f'''
                CREATE TABLE IF NOT EXISTS {crypto} (
                    emotions VARCHAR(50),
                    delta FLOAT,
                    timestamp TIMESTAMPTZ PRIMARY KEY,
                    delta FLOAT
                );
                '''
                cursor.execute(create_table_query)
                print(f"Table '{crypto}' created successfully.")

            # Commit the changes
            conn.commit()

            # Close the cursor and connection
            cursor.close()
            conn.close()

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
    

    def filter_emoton_threshold(emotion, threshold_value):
        
        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(
                **connection_params
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
    
    def get_crypto(database_name):
        try:
            # Establish a connection to the PostgreSQL server
            connection = psycopg2.connect(
                **connection_params
            )
            # Create a cursor
            cursor = connection.cursor()

            # SQL query to check for a database by name
            query = sql.SQL("SELECT datname FROM pg_database WHERE datname = %s;")
            cursor.execute(query, (database_name,))

            # Fetch the results
            database = cursor.fetchone()

            if database:
                print(f"Database '{database_name}' exists.")
                return database
            else:
                print(f"Database '{database_name}' does not exist.")
                return None

            # Close the cursor and connection
            cursor.close()
            connection.close()

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL: ", error)
            
        def drop_all_tables():
            try:
                # Establish a connection to the PostgreSQL server
                conn = psycopg2.connect(
                **connection_params
            )

                # Create a cursor
                cursor = conn.cursor()

                # SQL query to retrieve all table names
                get_table_names_query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_type = 'BASE TABLE';"
                cursor.execute(get_table_names_query)
                
                # Fetch all table names
                tables = cursor.fetchall()

                # Drop each table
                for table in tables:
                    drop_table_query = f"DROP TABLE {table[0]} CASCADE;"
                    cursor.execute(drop_table_query)
                    print(f"Dropped table: {table[0]}")

                # Commit the changes
                conn.commit()

                # Close the cursor and connection
                cursor.close()
                conn.close()

            except (Exception, psycopg2.Error) as error:
                print("Error while connecting to PostgreSQL", error)

    create_crypto_tables()
    
    # Replace these values with your PostgreSQL credentials
    database_name_to_find = "Midas"

    # Call the function with the database name you want to find
    get_crypto(database_name_to_find)
    
    
            
main()
