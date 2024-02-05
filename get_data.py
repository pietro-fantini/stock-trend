def get_data(symbol, API_key):
    # import libraries
    import requests
    import pandas as pd


    # call API and get the data
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + symbol + "&outputsize=full&apikey=" + API_key
    r = requests.get(url)
    data = r.json()

    # transform data into dataframe and drop non-data rows
    df = pd.DataFrame(data)
    df = df.drop(df.index[[0,1,2,3,4]])

    # normalize the dataframe
    df = df.join(df['Time Series (Daily)'].apply(pd.Series))

    # transform it to the format mplfinance read
    df = df.drop(["Meta Data", "Time Series (Daily)"], axis=1)
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.sort_index(ascending=True)

    return df