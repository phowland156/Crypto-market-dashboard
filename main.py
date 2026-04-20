import streamlit as st
from streamlit_autorefresh import st_autorefresh

from api.coingecko import get_history, get_market_data
from components.cards import coin_card
from components.charts import create_price_chart
from components.metrics import render_market_metrics
from utils.helpers import load_css


def main():

    st.set_page_config(layout="centered")

    # -------------------------
    # SESSION STATE
    # -------------------------
    if "selected_coin" not in st.session_state:
        st.session_state.selected_coin = "Bitcoin"

    if "time_label" not in st.session_state:
        st.session_state.time_label = "7 Day"

    if "show_now" not in st.session_state:
        st.session_state.show_now = True

    if "show_avg" not in st.session_state:
        st.session_state.show_avg = True

    if "show_high_low" not in st.session_state:
        st.session_state.show_high_low = False

    load_css("static/css/style.css")

    st.title("Crypto Dashboard")
    st.divider()

    # st_autorefresh(interval=30000)

    # -------------------------
    # COINS
    # -------------------------
    coins = {
        "Bitcoin": {
            "id": "bitcoin",
            "img": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png"
        },
        "Ethereum": {
            "id": "ethereum",
            "img": "https://assets.coingecko.com/coins/images/279/large/ethereum.png"
        },
        "Zcash": {
            "id": "zcash",
            "img": "https://assets.coingecko.com/coins/images/486/large/circle-zcash-color.png"
        }
    }

    # -------------------------
    # COIN ROW
    # -------------------------
    left, c1, c2, c3, c4, right = st.columns([3, 2, 2, 2, 2, 3])
    coin_cols = [c1, c2, c3, c4]

    for (name, data), col in zip(coins.items(), coin_cols):
        selected = st.session_state.selected_coin == name
        coin_card(col, name, data["img"], selected)

    coin_name = st.session_state.selected_coin
    coin = coins.get(coin_name)

    if not coin:
        st.error("Invalid coin selected")
        st.stop()

    coin_id = coin["id"]

    # -------------------------
    # MARKET DATA
    # -------------------------
    with st.spinner("Loading market data..."):
        market_data = get_market_data(coin_id)

    if not market_data:
        st.error("Failed to load market data")
        st.stop()

    change = market_data["price_change_percentage_24h"]

    render_market_metrics(market_data, coin_name)

    st.divider()

    # =====================================================
    # SIDEBAR CONTROLS
    # =====================================================
    st.sidebar.header("Chart Controls")

    # -------------------------
    # TIME OPTIONS (FIXED)
    # -------------------------
    time_options = {
        "1 Day": 1,
        "7 Day": 7,
        "1 Month": 30,
        "1 Year": 365
    }
    
    if st.session_state.time_label not in time_options:
        st.session_state.time_label = "7 Day"

    time_label = st.sidebar.selectbox(
        "Time Range",
        list(time_options.keys()),
        index=list(time_options.keys()).index(st.session_state.time_label)
    )

    st.session_state.time_label = time_label
    time_range = time_options[time_label]

    # -------------------------
    # CHART OPTIONS
    # -------------------------
    st.sidebar.subheader("Chart Options")

    st.session_state.show_now = st.sidebar.toggle(
        "Current Price Line",
        value=st.session_state.show_now
    )

    st.session_state.show_avg = st.sidebar.toggle(
        "Average Line",
        value=st.session_state.show_avg
    )

    st.session_state.show_high_low = st.sidebar.toggle(
        "High / Low",
        value=st.session_state.show_high_low
    )

    # -------------------------
    # CHART DATA
    # -------------------------
    with st.spinner("Loading chart data..."):
        df = get_history(coin_id, time_range)

    if df.empty:
        st.warning("No chart data available right now.")
        st.stop()

    # -------------------------
    # TITLE
    # -------------------------
    st.markdown(f"{coin_name} Price Chart ({time_label})")
    
    st.divider()

    # -------------------------
    # CHART
    # -------------------------
    fig = create_price_chart(
        df,
        coin_name,
        time_label,
        change,
        st.session_state.show_now,
        st.session_state.show_avg,
        st.session_state.show_high_low
    )

    st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()