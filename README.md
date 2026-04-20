Crypto-Market-Dashboard

A real-time cryptocurrency analytics dashboard built with Python, Streamlit, and Plotly.
The app allows users to track live market data, visualize historical price trends, 
and compare major cryptocurrencies in a clean, Coinbase-style interface


---Live Demo ----
https://crypto-market-dashboard-8jwhemjycacvs6srbn7o3v.streamlit.app/
------------------

Features
-----------
- Interactive price charts (Plotly)
- Time range selector (1 Day, 7 Day, 1 Month, 1 Year)
- Multi-coin support (Bitcoin, Ethereum, Zcash)
- Market metrics (price change, volume, etc.)
- Toggleable chart overlays (average, high/low, current price)
- Coinbase-inspired UI with custom CSS styling
- Auto-refresh market data

Tech Stack
----------
Frontend / UI: Streamlit
Data Visualization: Plotly
Data Source: CoinGecko API
Backend Logic: Python (Pandas)
Styling: Custom CSS

API used
-----------
This project uses the CoinGecko API for real-time and historical crypto data:

Market data endpoint
Historical price charts

No API key required.

Key Features explained
-------------------------
Interactive Chart
  Users can toggle:
    Current price line
    Average price line
    High / Low range
    
Time Selection
  Switch between:
    1 Day
    7 Days
    1 Month
    1 Year
  
Coin Switching
    Instantly switch between major cryptocurrencies with UI cards.

Challenges Solved
--------------------
- Handling real-time data refresh without breaking UI state
- Managing Streamlit session state for persistent UI selection
- Optimizing API calls to avoid redundant fetches
- Creating custom UI components with Streamlit limitations

Future Improvements
----------------------------
- Portfolio tracker (buy/sell simulation)
- Live WebSocket price updates
- More cryptocurrencies
- Dark/light theme toggle
- User authentication + saved portfolios

Project Struct.
----------------
crypto-market-dashboard/
│
├── main.py
├── api/
│   └── coingecko.py
├── components/
│   ├── cards.py
│   ├── charts.py
│   └── metrics.py
├── utils/
│   └── helpers.py
├── static/
│   └── css/
│       └── style.css
├── requirements.txt
└── README.md


Instillation
---------------
# Clone repository
git clone https://github.com/your-username/crypto-market-dashboard.git

# Navigate into project
cd crypto-market-dashboard

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run main.py
