import get_data as gd
import plot as plt

# choose a Stock Ticker Symbol
symbol = "AMZN"

# your alphavantage API key
API_key = "LIBK478O46U78WON"

# function to get and tranform the data
df = gd.get_data(symbol, API_key)

# save the data
df.to_csv("C:/Users/pietr/Visual Studio/fin comparison/stock_data_" + symbol + ".csv", index=True)

# plot the data
plt.plot(df)