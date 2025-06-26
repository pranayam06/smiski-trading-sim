import streamlit as st 
from streamlit_autorefresh import st_autorefresh
from trades import * 
from newmarket import *
from portfolio import get_stock_count

st.set_page_config(layout="wide")
for k, v in st.session_state.items():
    st.session_state[k] = v 

st_autorefresh(interval=1500, key="market_refresh")   
st.toggle("market open?", key= "market_open") 
update_market_safe() 
image_dict = {"Bubbles": "images/blowing-bubbles.png"} 

selected_typ = st.session_state.get("underlying_typ")
image_link = image_dict[selected_typ]
st.image(image_link)  
selected_price = st.session_state.get("selected_price")
print(st.session_state.get("selected_price"))
#dropdown for count  
maxCount = get_stock_count(selected_typ) 
if(maxCount > 0):
    count = st.slider("How many do you want to sell?", 0, int(maxCount)) 

    total_price = selected_price * count
    st.text(f"Total Gain: {total_price * 10000 // 100 / 100}")

    if st.button("Sell"): 
        sell_shares(selected_price, count, selected_typ)
        st.switch_page("app.py")
else:
    count = 0
    st.text("No Smiskis Owned")

    if st.button("Home"): 
        st.switch_page("app.py")



# sidebar
with st.sidebar:
    safe_start_market()

    data_df = pd.DataFrame({
        "name": ["Blowing Bubbles"],
        "stock": [get_stock_count('Bubbles')],
        "price_history": [st.session_state.df['delta'].tolist()], 
        "changeOT": [(st.session_state.df['delta'].iloc[-1]) / 11.5]
    })

    st.markdown("### 📋 Bubble Stats")
    st.dataframe(
        data_df,
        column_config={
            "name": "Smiski",
            "stock": "Count",
            "price_history": st.column_config.LineChartColumn(
                "Prices", y_min=0, y_max=5000
            ),
            "changeOT": "Change"
        },
        hide_index=True,
    )

    st.divider()
    st.markdown("### 🧸 Collectibles")
    st.page_link("pages/bubbles_page.py", label="🫧 Blowing Bubbles", use_container_width=True)  
    st.page_link("pages/bubbles_page.py", label="✈️ Paper Airplane", use_container_width=True)  
    st.page_link("pages/bubbles_page.py", label="☀️ Sunbathing", use_container_width=True)  

    st.divider()
    st.page_link("app.py", label="🏠 Home", use_container_width=True)
