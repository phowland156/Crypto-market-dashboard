import streamlit as st
import pandas as pd
import plotly.express as px
from api.coingecko import get_market_data


def render_portfolio(coins):

    st.sidebar.subheader("💼 Portfolio Tracker")
    
    prices = {}

    for name in coins.keys():
        coin_id = coins[name]
        data = get_market_data(coin_id)

        if data:
            prices[name] = data["current_price"]
        else:
            prices[name] = 0

    portfolio = {}

    # user inputs
    for name in coins.keys():
        amount = st.sidebar.number_input(
            f"{name} Holdings",
            min_value=0.0,
            step=0.1,
            key=f"holding_{name}"
        )
        portfolio[name] = amount


    # calculate value
    total_value = 0
    portfolio_data = []

    for name, amount in portfolio.items():

        if amount > 0:
            price = prices.get(name, 0)
            value = price * amount

            total_value += value

            portfolio_data.append({
                "coin": name,
                "value": value
            })

    # display results
    st.subheader("Portfolio Overview")

    st.metric("Total Value", f"${total_value:,.2f}")

    # pie chart
    if portfolio_data:
        df = pd.DataFrame(portfolio_data)

        fig = px.pie(
            df,
            names="coin",
            values="value",
            title="Portfolio Allocation"
        )

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="#2E2E2E",
            font=dict(color="white")
        )

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.info("Add holdings in the sidebar to see your portfolio.")