import pandas as pd
import requests

# api url
url = 'https://www.alphavantage.co/query'

# api parameters
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "AAPL",
    "datatype": "json",
    "apikey": "U0S1NNAA7C7EZ6B8"
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
    df = pd.DataFrame(trimmed_data)

    columns = ['1. open', '2. high', '3. low', '4. close', '5. volume']
    for col in df:
        if col not in columns:
            print(f"Warning, missing column: {col}")
        
    # transpose data for viewing
    df = df.transpose()

    # print last 10 rows
    print(df.tail(10))


# Error handling
except requests.exceptions.RequestException as e:
    print(f"API request error: {e}")

except KeyError as e:
    print(f"Data format error: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
