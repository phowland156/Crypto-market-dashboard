import streamlit as st

def format_large_number(num):
    if num is None:
        return "N/A"

    num = float(num)

    if num >= 1_000_000_000_000:
        return f"${num / 1_000_000_000_000:.2f}T"
    elif num >= 1_000_000_000:
        return f"${num / 1_000_000_000:.2f}B"
    elif num >= 1_000_000:
        return f"${num / 1_000_000:.2f}M"
    elif num >= 1_000:
        return f"${num / 1_000:.2f}K"
    else:
        return f"${num:,.0f}"

def render_market_metrics(data,coin_name):

    price = data.get("current_price", 0)
    change = data.get("price_change_percentage_24h")
    market_cap = data.get("market_cap", 0)
    volume = data.get("total_volume", 0)

    # change logic
    if change is None:
        change_text = "N/A"
        change_color = "#9ca3af"
        arrow = ""
        change_class = ""
    elif change > 0:
        change_text = f"+{change:.2f}%"
        change_color = "#16c784"
        arrow = "▲"
        change_class = "metric-positive"
    else:
        change_text = f"{change:.2f}%"
        change_color = "#ea3943"
        arrow = "▼"
        change_class = "metric-negative"

    st.markdown(f"""
    <div class="metric-grid">

    <div class="metric-card">
        <div class="metric-title">{coin_name} Price</div>
        <div class="metric-value">${price:,.2f}</div>
        <div class="metric-change {change_class}">
        {arrow} {change_text}
        </div>
    </div>

    <div class="metric-card">
        <div class="metric-title">24h Change</div>
        <div class="metric-value {change_class}">{change_text}</div>
    </div>


    <div class="metric-card">
        <div class="metric-title">Market Cap</div>
        <div class="metric-value">{format_large_number(market_cap)}</div>
    </div>

    <div class="metric-card">
        <div class="metric-title">Volume</div>
        <div class="metric-value">{format_large_number(volume)}</div>
    </div>


    </div>
    """, unsafe_allow_html=True)