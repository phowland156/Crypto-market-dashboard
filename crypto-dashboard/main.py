import streamlit as st
from streamlit_autorefresh import st_autorefresh

from api.coingecko import get_history, get_market_data
from components.cards import coin_card, coin_cards_css
from components.charts import render_price_chart
from components.metrics import render_market_stats, render_price_header
from components.portfolio import render_portfolio
from utils.helpers import load_css
from pathlib import Path
# ...
load_css("static/css/style.css")

COINS = {
    "Bitcoin": {
        "id": "bitcoin",
        "img": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png",
    },
    "Ethereum": {
        "id": "ethereum",
        "img": "https://assets.coingecko.com/coins/images/279/large/ethereum.png",
    },
    "Zcash": {
        "id": "zcash",
        "img": "https://assets.coingecko.com/coins/images/486/large/circle-zcash-color.png",
    },
}

# label -> (days of history, text shown beside the chart change)
TIME_RANGES = {
    "1D": (1, "Past day"),
    "1W": (7, "Past week"),
    "1M": (30, "Past month"),
    "1Y": (365, "Past year"),
}


def main():
    st.set_page_config(
        page_title="Crypto Market Dashboard",
        layout="wide",
        initial_sidebar_state="collapsed",
    )  # MUST BE FIRST STREAMLIT CALL

    if "selected_coin" not in st.session_state:
        st.session_state.selected_coin = "Bitcoin"

    load_css("static/css/style.css")

    st.title("Crypto Market Dashboard")

    st_autorefresh(interval=30000)

    # --- coin picker (3 across, even on a phone) ---
    st.markdown(coin_cards_css(COINS, st.session_state.selected_coin), unsafe_allow_html=True)
    cols = st.columns(len(COINS))
    for col, name in zip(cols, COINS):
        coin_card(col, name)

    coin_name = st.session_state.selected_coin
    coin = COINS.get(coin_name)
    if not coin:
        st.error("Invalid coin selected")
        st.stop()

    with st.spinner("Loading market data..."):
        data = get_market_data(coin["id"])

    if data is None:
        st.markdown("""
        <div class="error-box">
            ⚠️ Unable to load market data<br><br>
            Please wait a moment or try again.
        </div>
        """, unsafe_allow_html=True)
        return

    # --- price header ---
    render_price_header(data, coin_name, coin["img"])

    # The chart sits ABOVE the range buttons on screen, but needs the button value first,
    # so reserve its spot now and fill it after the buttons have been read.
    chart_area = st.container(key="chart_area")

    with st.container(key="range_pills"):
        choice = st.segmented_control(
            "Time range",
            list(TIME_RANGES.keys()),
            default="1D",
            key="time_range",
            label_visibility="collapsed",
        )
    days, range_text = TIME_RANGES[choice or "1D"]

    with chart_area:
        with st.spinner("Loading chart data..."):
            df = get_history(coin["id"], days)

        if df.empty:
            st.warning("No chart data available right now. Try another time range.")
        else:
            render_price_chart(df, range_text)

    render_market_stats(data)


if __name__ == "__main__":
    main()
