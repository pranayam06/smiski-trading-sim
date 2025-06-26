from collections import deque  
import streamlit as st
for k, v in st.session_state.items():
    st.session_state[k] = v

if "portfolio" not in st.session_state:
    st.session_state["portfolio"] = {
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

portfolio = st.session_state["portfolio"]
 
def get_budget(): 
  return portfolio['cash']

def set_budget(new_cash): 
  portfolio["cash"] = new_cash

def get_stock_count(strType):
   return len(portfolio['smiskis'][strType])

def enq_stocks(smiski_typ, count, price):
   for _ in range(count):
      portfolio["smiskis"][smiski_typ].append(price)  
   portfolio["total count"] += count
   if not len(portfolio["smiskis"][smiski_typ]) == 0:
      portfolio["average cost"][smiski_typ] = round(sum(portfolio["smiskis"][smiski_typ]) / len(portfolio["smiskis"][smiski_typ]), 2)
   else:
      portfolio["average cost"][smiski_typ] = 0
   
def get_average(smiski_type):
   return portfolio["average cost"][smiski_type]

def deq_stocks(smiski_typ, count, price):
   for _ in range(count):
      portfolio["cash"] += (price)
      portfolio["smiskis"][smiski_typ].popleft()
   portfolio["total count"] -= count 
   if not len(portfolio["smiskis"][smiski_typ]) == 0:
      portfolio["average cost"][smiski_typ] = round(sum(portfolio["smiskis"][smiski_typ]) / len(portfolio["smiskis"][smiski_typ]), 2)
   else:
      portfolio["average cost"][smiski_typ] = 0

def get_total():
   return portfolio["total count"]