import requests
import pandas as pd

import streamlit as st

@st.cache_data(ttl=300)
def get_history(coin, days):

    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"

    params = {
        "vs_currency": "usd",
        "days": days
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "prices" not in data:
        print("API response:", data)
        return pd.DataFrame()

    prices = data["prices"]

    df = pd.DataFrame(prices, columns=["time", "price"])
    df["time"] = pd.to_datetime(df["time"], unit="ms")

    return df

    # Coingecko API function to retreive data for zcash
@st.cache_data(ttl=60)
def get_market_data(coin):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "ids": coin}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list) and len(data) > 0:
            return data[0]

    except requests.exceptions.RequestException as e:
        print("API ERROR:", e)

    return None



