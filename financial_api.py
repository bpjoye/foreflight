import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv() 

# api url
url = 'https://www.alphavantage.co/query'

api_key = os.environ.get('ALPHAVANTAGE_KEY')
print(api_key)

# api parameters
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "AAPL",
    "datatype": "json",
    "apikey": api_key
}
try:
    # send api request
    r = requests.get(url, params=params)
    r.raise_for_status()

    # convert to json
    data = r.json()

    # check that data is formatted correctly
    if "Time Series (Daily)" not in data:
        raise KeyError("Data is not formatted correctly!")

    # remove meta data
    trimmed_data = data["Time Series (Daily)"]

    # convert to pandas dataframe
    df = pd.DataFrame.from_dict(trimmed_data, orient='index')

    columns = ['1. open', '2. high', '3. low', '4. close', '5. volume']
    for col in df.columns:
        if col not in columns:
            print(f"Warning, missing column: {col}")

    # print last 10 rows
    print(df.tail(10))


# Error handling
except requests.exceptions.RequestException as e:
    print(f"API request error: {e}")

except KeyError as e:
    print(f"Data format error: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")