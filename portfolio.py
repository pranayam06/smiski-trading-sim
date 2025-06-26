from collections import deque  
import streamlit as st
for k, v in st.session_state.items():
    st.session_state[k] = v

portfolio = {
    "cash": 100.00, 
    "total count": 0,
    "smiskis": {
        "Bubbles": deque(),
        "Relaxing": deque()
    }, 
    "average cost": {
        "Bubbles": 0,
        "Relaxing": 0
    } 
}

 
def get_budget(): 
  return portfolio['cash']

def set_budget(new_cash): 
  portfolio["cash"] = new_cash

def get_stock_count(strType):
   return len(portfolio['smiskis'][strType])

def enq_stocks(smiski_typ, count, price):
   for _ in range(count):
      portfolio["smiskis"][smiski_typ].append(price)  
   portfolio["average cost"][smiski_typ] = sum(portfolio["smiskis"][smiski_typ])  
   portfolio["total count"] += count

def get_average(smiski_type):
   return portfolio["average cost"][smiski_type]

def deq_stocks(smiski_typ, count, price):
   res = 0
   for _ in range(count):
      res += (price - portfolio["smiskis"][smiski_typ].popleft()) 
   portfolio["average cost"][smiski_typ] = sum(portfolio["smiskis"][smiski_typ]) 
   portfolio["total count"] -= count
   return res

def get_total():
   return portfolio["total count"]