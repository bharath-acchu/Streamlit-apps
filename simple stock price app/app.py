# pip install yfinance
# yfinance is basically used to get the reliable, threaded and pythonic way to download historical market data from yahoo finance

import yfinance as yf 
import streamlit as st
import pandas as pd

st.write(
    """
    # Simple Stock Price App
    
   ### 1. Shown are the stock **closing** and **volume of Google!**
    """
    
)


# define the ticker symbol
# ticker module allows you to access ticker data in pythonic way

tickerSymbol = 'GOOGL'

# get the data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# get the historical price sfor this ticker
tickerDf = tickerData.history(period= '1d',start = '2010-8-31',end = '2020-8-23')


st.write(
    """
    ## Closing Price
    """
)
st.line_chart(tickerDf.Close)

st.write(
    """
    ## Volume Price
    """
)
st.line_chart(tickerDf.Volume)



st.write(
    """
   
    
   ### 2. Shown are the stock **closing** and **volume of Apple**
    """
    
)


# define the ticker symbol
# ticker module allows you to access ticker data in pythonic way

tickerSymbol = 'AAPL'

# get the data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# get the historical price sfor this ticker
tickerDf = tickerData.history(period= '1d',start = '2010-8-31',end = '2020-8-23')


st.write(
    """
    ## Closing Price
    """
)
st.line_chart(tickerDf.Close)

st.write(
    """
    ## Volume Price
    """
)
st.line_chart(tickerDf.Volume)

