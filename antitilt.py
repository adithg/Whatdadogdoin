import json 
import psycopg2
from psycopg2 import sql 
import datetime 
import mindsdb_sdk
import time
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import random



connection_params = {
    'database': 'Midas', 
    'user': 'postgres',
    'password' : 'password', 
    'host' : '6.tcp.us-cal-1.ngrok.io',
    'port' : 16376
}

all_emotions = ['Admiration', 'Adoration','Aesthetic Appreciation','Amusement','Anger','Anxiety','Awe','Awkwardness',
                'Boredom','Calmness','Concentration','Confusion','Contemplation','Contempt','Contentment','Craving',
                'Desire','Determination','Disappointment','Disgust','Distress','Doubt','Ecstasy','Embarrassment',
                'Empathic Pain','Entrancement','Envy','Excitement','Fear','Guilt','Horror','Interest',
                'Joy','Love','Nostalgia','Pain','Pride','Realization','Relief','Romance',
                'Sadness','Satisfaction','Shame','Surprise (negative)','Surprise (positive)','Sympathy','Tiredness','Triumph']

main_table = "Golden_Touch"
#server = mindsdb_sdk.connect(url='https://cloud.mindsdb.com/account', login='adithgang@gmail.com', password='Awesome#0725!')

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

        
        create_table_query = f'''
        CREATE TABLE IF NOT EXISTS {main_table} (
            currency VARCHAR(50),
            emotion VARCHAR(50),
            weight FLOAT,
            time_of_trade timestamp PRIMARY KEY,
            category VARCHAR(200),
            delta VARCHAR(200)
        );
        '''
        cursor.execute(create_table_query)
        print("Table created successfully.")

        # Commit the changes
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)


def filter_table_by_emotion(emotion_name, currency):
    try:
        # Establish a connection to the PostgreSQL server
        conn = psycopg2.connect(
            **connection_params
        )

        # Create a cursor
        cursor = conn.cursor()

        # SQL query to fetch records filtered by emotion
        filter_query = f"SELECT * FROM {main_table} WHERE emotion = %s"
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
        
def insert_into_table(currency, emotion, weight, delta, category, time=None):
    try:
        # Establish a connection to the PostgreSQL server
        conn = psycopg2.connect(
            **connection_params
        )

        # Create a cursor
        cursor = conn.cursor()

        if time == None:
            time = datetime.datetime.now()

        # SQL query to insert values into the specified table
        insert_query = f"INSERT INTO {main_table} (currency, emotion, weight, time_of_trade, category, delta) VALUES (%s, %s, %s, %s, %s, %s);"
        cursor.execute(insert_query, (currency, emotion, weight, time.strftime(f'%Y-%m-%d %H:%M:%S.%f'), category, delta))

        # Commit the changes
        conn.commit()
        print(f"Values inserted into the database successfully at {time}.\n")

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
        query = f"SELECT * FROM {main_table};"
        dataframes[curr] = pd.read_sql_query(query, conn, parse_dates=['datetime'])

def create_dummy_data(int_val):
    for curr in currencies:
        for i in range(25):
            emotion = np.random.choice(all_emotions)
            mean = random.random()
            percentage = random.random()
            delta = np.round(random.random(), decimals=2) * int_val
            if mean >= 0.75 and mean <= 1:
                description = f"This trade was characterized by very prominent {emotion}, which was observed {np.round(percentage * 10, decimals=2)}% of the time with a mean expressiveness score of {np.round(mean, decimals=2)}."
            elif mean >= 0.5 and mean < 0.75:
                description = f"{emotion} was fairly noticeable {np.round(percentage * 10, decimals=2)}% of the time elapsed for this trade with a mean expressiveness score of {np.round(mean, decimals=2)}."
            elif mean >= 0.3 and mean < 0.5:
                description = f"Some {emotion} was detected during {np.round(percentage * 10, decimals=2)}% of this trade with a mean expressiveness score of {np.round(mean, decimals=2)}."
            elif mean < 0.3:
                description = "This trade had no significant emotional context."
            insert_into_table(curr, emotion, np.round(mean, decimals=2), delta, description, time=None)
            time.sleep(2)
            
#drop_all_tables()
#create_crypto_tables()
#create_dummy_data(1)
#create_dummy_data(-1)