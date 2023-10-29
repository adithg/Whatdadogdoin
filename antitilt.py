import json 
import psycopg2
from psycopg2 import sql 
import datetime 
import mindsdb_sdk
import time
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt



connection_params = {
    'database': 'Midas', 
    'user': 'postgres',
    'password' : 'password', 
    'host' : '6.tcp.us-cal-1.ngrok.io',
    'port' : 16376
}

server = mindsdb_sdk.connect()

dt = datetime

currencies = ['BTCUSDT', 'ETHUSDT', 'XRPUSDT', 'DOGEUSDT']

dataframes  = {currency : None for currency in currencies}


def create_crypto_tables():
    try:
        # Establish a connection to the PostgreSQL server
        conn = psycopg2.connect(
            **connection_params
        )

        # Create a cursor
        cursor = conn.cursor()

        # List of cryptocurrencies to create tables for
        currencies

        for crypto in currencies:
            # SQL query to create tables
            create_table_query = f'''
            CREATE TABLE IF NOT EXISTS {crypto} (
                emotion VARCHAR(50),
                weight FLOAT,
                time_of_trade timestamp PRIMARY KEY,
                category VARCHAR(155)
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


def filter_table_by_emotion(emotion_name, table):
    try:
        # Establish a connection to the PostgreSQL server
        conn = psycopg2.connect(
            **connection_params
        )

        # Create a cursor
        cursor = conn.cursor()

        # SQL query to fetch records filtered by emotion
        filter_query = f"SELECT * FROM {table} WHERE emotion = %s"
        cursor.execute(filter_query, (emotion_name, ))

        # Fetch all records with the specified emotion in the 'emotions' column
        filtered_data = cursor.fetchall()

        # Print or process the filtered data
        if filtered_data:
            print(f"Records with emotion '{emotion_name}':")
            for row in filtered_data:
                print(row)
            return filtered_data
        else:
            print(f"No records found with emotion '{emotion_name}'")

        # Close the cursor and connection
        cursor.close()
        conn.close()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    

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
            
def get_crypto(crypto_name):
    try: 
        conn = psycopg2.connect(
            **connection_params
        )
        
        cursor = conn.cursor()
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        
def insert_into_table(currency, emotion, weight, category):
    try:
        # Establish a connection to the PostgreSQL server
        conn = psycopg2.connect(
            **connection_params
        )

        # Create a cursor
        cursor = conn.cursor()
        
        time = datetime.datetime.now()

        # SQL query to insert values into the specified table
        insert_query = f"INSERT INTO {currency} (emotion, weight, time_of_trade, category) VALUES (%s, %s, %s, %s);"
        cursor.execute(insert_query, (emotion, weight, time.strftime(f'%Y-%m-%d %H:%M:%S.%f'), category))

        # Commit the changes
        conn.commit()
        print("Values inserted into the table successfully.")

        # Close the cursor and connection
        cursor.close()
        conn.close()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        
        
def to_df():
    conn = psycopg2.connect(
        **connection_params
    )
    
    for curr in currencies:
        query = f"SELECT * FROM {curr};"
        dataframes[curr] = pd.read_sql_query(query, conn, parse_dates=['datetime'])

        
drop_all_tables()
create_crypto_tables()

insert_into_table(
    'BTCUSDT',
    'anger',
    .0031,
    'anger is not prominent .31 percent of the time '
    )

time.sleep(2)

insert_into_table(
    'BTCUSDT',
    'anger',
    .12341,
    'anger is very prominent 80% of the time '
    )

filter_table_by_emotion(
    'anger', 'BTCUSDT'
)
