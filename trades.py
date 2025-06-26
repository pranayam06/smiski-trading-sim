import streamlit as st
from portfolio import *

for k, v in st.session_state.items():
    st.session_state[k] = v 


def buy_shares(price, count, typ_smiski):
    set_budget(get_budget() - price*count)
    enq_stocks(typ_smiski, count, price)

def sell_shares(price, count, typ_smiski):
    set_budget(get_budget() + deq_stocks(typ_smiski), count, price)
    