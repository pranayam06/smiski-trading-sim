import streamlit as st 
import pandas as pd 
import random
import datetime
import time
for k, v in st.session_state.items():
    st.session_state[k] = v

csv_path = 'data/bubbles.csv'

if ('market_open' not in st.session_state): 
        st.session_state.market_open = False
if('df' not in st.session_state):
      st.session_state.df = pd.DataFrame(columns=['time', 'price', 'delta']) 


def update_market():
    if not st.session_state.get("market_open", False):
        return 
    else:
         if st.session_state.df.empty: 
              new_row = pd.DataFrame({'time': [datetime.datetime.now()], 'price': [11.5], 'delta': [0]})
              st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)
    change_pct = random.gauss(0, 0.01)  # mean 0%, standard deviation 0.5%
    last_price = (st.session_state.df['price'].iloc[-1] * (1 + change_pct))
    new_row = pd.DataFrame({'time': [datetime.datetime.now()], 'price': [last_price], 'delta': [last_price-11.5]})
    st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)
    st.session_state.df.to_csv(csv_path, index=False) 
    print(last_price)

def update_market_safe():
    if ('market_open' not in st.session_state): 
        st.session_state.market_open = False
    if('df' not in st.session_state):
      st.session_state.df = pd.DataFrame(columns=['time', 'price', 'delta']) 

#df and market open exists guaranteed 
    if (st.session_state.market_open): 
      update_market() 

def safe_start_market():

    if ('market_open' not in st.session_state): 
        st.session_state.market_open = False
    if('df' not in st.session_state):
      st.session_state.df = pd.DataFrame(columns=['time', 'price', 'delta']) 

    if st.session_state.df.empty: 
              new_row = pd.DataFrame({'time': [datetime.datetime.now()], 'price': [11.5], 'delta': [0]})
              st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True) 


def get_price(smiski_typ):
     return st.session_state.df['price'].iloc[-1] 

def get_market_high(smiski_typ):
     return st.session_state.df['price'].max() 

def get_market_low(smiski_typ):
     return st.session_state.df['price'].min() 