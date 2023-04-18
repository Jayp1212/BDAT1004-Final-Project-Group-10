import requests
from pymongo import MongoClient
import json
import time

# Set up MongoDB Atlas connection
client = MongoClient('mongodb+srv://JayPatel:Jay123@cluster0.xixsv8j.mongodb.net/?retryWrites=true&w=majority')
db = client['stock_database']
collection = db['stock_collection']

# Alpha Vantage API information
api_key = "J8PI3DEDMUCJP5I0"

# Define stock symbols
symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "FB"]

while True:
    for symbol in symbols:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
        # Retrieve data from Alpha Vantage API
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()["Global Quote"]

            # Insert data into MongoDB collection
            collection.insert_one(data)
            print(f"Data for {symbol} inserted into database!")
        else:
            print(f"Error retrieving data for {symbol}: {response.status_code}")
    

# Wait 5 minutes before retrieving new data

time.sleep(300)
