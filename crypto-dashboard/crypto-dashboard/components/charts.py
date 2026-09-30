import json
from functools import lru_cache
from pathlib import Path

import pandas as pd
import streamlit.components.v1 as components

_TEMPLATE = Path(__file__).with_name("touch_chart.html")

UP_COLOR = "#16c784"
DOWN_COLOR = "#ea3943"


@lru_cache(maxsize=1)
def _template() -> str:
    return _TEMPLATE.read_text(encoding="utf-8")


def render_price_chart(df: pd.DataFrame, range_label: str, height: int = 420) -> None:
    """Render a Coinbase-style touch chart (Plotly.js) for a price DataFrame.

    Touch: drag one finger to trace the price with a dot, pinch to zoom,
    two fingers to pan, double-tap to reset.
    Mouse: hover to trace, wheel to zoom, drag to pan, double-click to reset.
    """
    df = df.dropna(subset=["time", "price"]).drop_duplicates("time").sort_values("time")

    # milliseconds since epoch (works whatever datetime resolution pandas uses)
    t_ms = (df["time"] - pd.Timestamp("1970-01-01")) // pd.Timedelta(milliseconds=1)

    prices = df["price"].astype(float).tolist()
    color = UP_COLOR if prices[-1] >= prices[0] else DOWN_COLOR

    payload = {
        "t": [int(v) for v in t_ms],
        "p": prices,
        "color": color,
        "label": range_label,
    }
    data_json = json.dumps(payload).replace("</", "<\\/")

    html = _template().replace("__COLOR__", color).replace("__PAYLOAD__", data_json)
    components.html(html, height=height, scrolling=False)
