import streamlit as st

from utils.helpers import format_compact


def _change_parts(change):
    if change is None:
        return "N/A", "", ""
    if change > 0:
        return f"+{change:.2f}%", "▲", "metric-positive"
    return f"{change:.2f}%", "▼", "metric-negative"


def render_price_header(data, coin_name, img):
    """Big price + 24h change, shown above the chart (Coinbase-style)."""
    price = data.get("current_price") or 0
    price_text = f"${price:,.2f}" if price >= 1 else f"${price:,.6f}"
    change_text, arrow, change_class = _change_parts(data.get("price_change_percentage_24h"))

    st.markdown(f"""
    <div class="price-hero">
        <div class="price-hero-name"><img src="{img}" class="hero-logo"/>{coin_name}</div>
        <div class="price-hero-value">{price_text}</div>
        <div class="price-hero-change {change_class}">{arrow} {change_text} <span>24h</span></div>
    </div>
    """, unsafe_allow_html=True)


def render_market_stats(data):
    market_cap = format_compact(data.get("market_cap"))
    volume = format_compact(data.get("total_volume"))

    st.markdown(f"""
    <div class="metric-grid">
        <div class="metric-card">
            <div class="metric-title">Market Cap</div>
            <div class="metric-value">{market_cap}</div>
        </div>
        <div class="metric-card">
            <div class="metric-title">24h Volume</div>
            <div class="metric-value">{volume}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
