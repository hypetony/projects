pip install yfinance

import pandas as pd
import yfinance as yf

# Define variables
ticker_symbol = 'AAPL'  # You can change this to any stock symbol
initial_investment = 1000
years = 10

# Fetch historical stock price data from Yahoo Finance
stock_data = yf.download(ticker_symbol, start='2022-01-01', end='2022-12-31')

# Create a dataframe with year and value columns
df = pd.DataFrame({'Year': range(1, years + 1)})
df['Date'] = pd.to_datetime(df['Year'], format='%Y')
df['Value'] = initial_investment * (1 + stock_data['Adj Close'].pct_change()).add(1).cumprod()

# Print the final value
final_value = df['Value'].iloc[-1]
print(f'The final value after {years} years of investing in {ticker_symbol} is ${final_value:.2f}')
