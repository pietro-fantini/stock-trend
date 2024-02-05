def plot(df):
    import mplfinance as mpf
    
    # plot it
    mpf.plot(df, type='candle', style='charles',
            title='Candlestick Chart',
            ylabel='Price',
            volume=True,
            datetime_format='%Y-%M-%D')