import pandas as pd
import streamlit as st
import requests
st.header('Bitcoin Prices')
days = st.slider('No of days',1,365)
currency = st.radio('Currency',('CAD','USD','INR','AUD'))
payload = {'vs_currency': currency, 'days': days, 'interval':'daily'}
req = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart', params=payload)
if req.status_code == 200:
    r = req.json()
df = pd.DataFrame(r['prices'], columns= ['Date',currency])
df['Date'] = pd.to_datetime(df['Date'],unit='ms')
df = df.set_index('Date')
st.line_chart(df[currency])
st.write('Average Price during this time was ', str(df[currency].mean()), currency)