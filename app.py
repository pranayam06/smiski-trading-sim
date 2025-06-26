import streamlit as st 
import pandas as pd
from newmarket import *
from portfolio import *
import time
from streamlit_autorefresh import st_autorefresh 
for k, v in st.session_state.items():
    st.session_state[k] = v 


title_path = "images/415b1e5e-36aa-481c-bd6e-40623dc63c1c.png"


st.image(title_path, width=500)

st.divider()
st_autorefresh(interval=1500, key="market_refresh")   
st.toggle("market open?", key= "market_open") 
update_market_safe()


with st.container():
    st.markdown(f"""
        <div style="
            background-color: #f7f7f9;
            border-radius: 16px;
            padding: 24px;
            margin-top: 16px;
            margin-bottom: 24px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            text-align: center;
        ">
            <h2 style="margin-bottom: 0px;">Your Budget</h2>
            <h1 style="font-size: 2.8rem; color: #2F5D50; margin: 0;">
                ${get_budget():.2f}
            </h1>
        </div>
    """, unsafe_allow_html=True)

st.session_state.df['time'] = pd.to_datetime(st.session_state.df['time']) 


with st.sidebar:
    #sidebar df creater 
    safe_start_market()

    data_df = pd.DataFrame(
        {
            "name": ["Blowing Bubbles"],
            "stock": [get_stock_count('Bubbles')],
            "price_history": [st.session_state.df['delta'].tolist()], 
            "changeOT": [(st.session_state.df['delta'].iloc[-1])/11.5]
        }
    )
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
    st.title("Collectibles")
    st.page_link("pages/bubbles_page.py", label="Blowing Bubbles", icon="🫧", use_container_width=True)  
    st.page_link("pages/bubbles_page.py", label="Paper Airplane", icon="✈️", use_container_width=True)  
    st.page_link("pages/bubbles_page.py", label="Sunbathing", icon="☀️", use_container_width=True)  
    st.divider()

   link_home = st.page_link("app.py", label = "", icon=":material/home:")
