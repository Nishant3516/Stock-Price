from contextlib import nullcontext
import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

By  Nishant Bansal


""")

option = st.selectbox(
'Whose company stock price you wanna check',
('META', 'TWITTER', 'GOOGLE'))

st.write("Shown are the stock closing price and volume of ", option)

if option=="GOOGLE":
    Symbol = 'GOOGL'

if option=="META":
    Symbol = 'FB'

if option=="TWITTER":
    Symbol = 'TWTR'
#get data on this ticker
Data = yf.Ticker(Symbol)
#get the historical prices for this ticker
Df = Data.history(period="max")
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(Df.Close)
st.line_chart(Df.Volume)
