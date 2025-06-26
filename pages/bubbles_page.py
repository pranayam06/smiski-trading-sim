import streamlit as st
from newmarket import *  
from streamlit_autorefresh import st_autorefresh 
from portfolio import *
import pandas as pd 
st.set_page_config(layout="wide")

st.markdown("""
    <style>
        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        .stat-card {
            background-color: #ffffff;
            padding: 12px 18px;
            margin: 6px 0;
            border-radius: 12px;
            border: 1px solid #e0e0e0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        .stat-card strong {
            color: #444;
        }
    </style>
""", unsafe_allow_html=True)

for k, v in st.session_state.items():
    st.session_state[k] = v

st_autorefresh(interval=1500, key="market_refresh")   
safe_start_market()
st.title("Blowing Bubbles")
st.toggle("Market Open?", key="market_open") 
update_market_safe()


image_col, _, stats_col = st.columns([3, 0.5, 3]) 

with image_col: 
    image_path = "images/blowing-bubbles.png" 
    st.image(image_path, use_container_width=True, caption="Blowing Bubbles")

with stats_col:
    st.subheader("Your Position")

    stats = {
        "Buying Power": f"${get_budget():.2f}",
        "Count": get_stock_count("Bubbles"),
        "Average Cost": f"${get_average('Bubbles'):.2f}",
        "Total Count": get_total()
    }

    for label, value in stats.items():
        st.markdown(
            f'<div class="stat-card"><strong>{label}:</strong> {value}</div>',
            unsafe_allow_html=True
        )

chart_col, _, mstats_col = st.columns([4, 0.5, 2])

with chart_col:
    st.subheader("Live Market")
    st.session_state.df['time'] = pd.to_datetime(st.session_state.df['time'])
    st.line_chart(
        st.session_state.df.set_index('time')[['delta']],
        color="#2F5D50",
    )

with mstats_col:
    st.subheader("Market Statistics")

    stats = {
        "Open": "$11.50",
        "High": f"${get_market_high('Bubbles'):.2f}",
        "Low":  f"${get_market_low('Bubbles'):.2f}",
        "Current": f"${get_price('Bubbles'):.2f}",
    }

    for label, value in stats.items():
        st.markdown(
            f'<div class="stat-card"><strong>{label}:</strong> {value}</div>',
            unsafe_allow_html=True
        )


price_col, buy_col = st.columns([2,1]) 

with price_col:
    price = get_price("Bubbles")

    st.markdown(f"""
        <div style="
            background-color: #f9f7f4;
            border: 2px solid #A8CBB1; 
            margin: 2px
            padding: 1em;
            font-size: 28px;
            font-weight: 600;
            color: #333333;
            border-radius: 16px;
            text-align: center;
            box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.05); 
        "> 
            Current Price:
            ${price:.2f} USD
        </div>
    """, unsafe_allow_html=True)

# Buy button
with buy_col: 
    if(st.session_state.get("market_open")):
        if st.button("Go to Buy Page"):
            st.session_state.selected_price = get_price("Bubbles")
            st.session_state.underlying_typ = "Bubbles"
            st.switch_page("pages/buy.py")
        if st.button("Go to Sell Page"):
            st.session_state.selected_price = get_price("Bubbles")
            st.session_state.underlying_typ = "Bubbles"
            st.switch_page("pages/sell.py") 

    else: 
        st.text("Market Closed: No transactions")


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
