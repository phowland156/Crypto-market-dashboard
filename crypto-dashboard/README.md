# Crypto Market Dashboard

A mobile-friendly crypto dashboard built with **Python** and **Streamlit**. It shows live prices for Bitcoin, Ethereum and Zcash with a Coinbase-style touch chart: trace the price with your finger, pinch to zoom, and the price axis rescales automatically.

## Features

- **Touch chart (Plotly.js):**
  - Drag one finger to trace the price with a dot and a live readout (price, % change, time).
  - Pinch to zoom, use two fingers to pan, double-tap to reset.
  - The price axis autoscales to whatever is visible.
  - On desktop: hover to trace, mouse wheel to zoom, click-drag to pan, double-click to reset.
- **Coins:** Bitcoin, Ethereum and Zcash, selected from tappable logo cards.
- **Time ranges:** 1D, 1W, 1M and 1Y.
- **Live stats:** current price, 24h change, market cap and 24h volume. Data refreshes every 30 seconds.
- **Mobile-first layout:** coin cards stay in one row on phones, and large numbers are shortened (`$1.23T`, `$45.6B`).
- **Data source:** the free [CoinGecko API](https://www.coingecko.com/en/api), with caching to stay within rate limits.

## Getting started

### Requirements

- Python 3.9+
- Streamlit 1.40 or newer
- An internet connection (the chart loads Plotly.js from the Plotly CDN, and prices come from CoinGecko)

### Install and run

```bash
git clone https://github.com/phowland156/Crypto-market-dashboard.git
cd Crypto-market-dashboard

python -m venv venv
# Windows:   venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

pip install -r requirements.txt
streamlit run main.py
```

Run the command from the project folder, because the CSS file is loaded with a relative path. If `streamlit` isn't found, use `python -m streamlit run main.py`.

To try it on your phone, open the "Network URL" that Streamlit prints in the terminal (your phone must be on the same Wi-Fi).

## Project structure

```
main.py                      # app entry point and page layout
api/
  coingecko.py               # CoinGecko requests (cached)
components/
  cards.py                   # coin selector cards
  metrics.py                 # price header and market stats
  charts.py                  # prepares chart data and embeds the touch chart
  touch_chart.html           # Plotly.js chart with the touch gestures
  portfolio.py               # portfolio tracker (not used in the main page yet)
static/css/style.css         # mobile-first styling
utils/
  helpers.py                 # CSS loader and number formatting
requirements.txt
```

## How the touch chart works

Streamlit's built-in `st.plotly_chart` can't do custom gestures, so the chart is Plotly.js embedded with `st.components.v1.html`. `components/charts.py` sends the price data to `components/touch_chart.html`, which draws the line with Plotly and handles touch and mouse input with Pointer Events. The moving dot and readout are drawn on top of the Plotly chart, and the visible range is passed to Plotly as you zoom and pan.

## Known limitations

- The free CoinGecko API is rate limited. If data stops loading, wait a minute and refresh.
- Touching the chart won't scroll the page; scroll from anywhere outside it.
- Prices are for information only, not financial advice.

## Ideas for next steps

- Add more coins.
- Turn on the portfolio tracker.
- Add price alerts.

## License

Add a license of your choice (for example MIT) before sharing publicly.
