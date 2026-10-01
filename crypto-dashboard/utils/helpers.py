import streamlit as st
from pathlib import Path


def load_css(file_name):
    base_dir = Path(__file__).resolve().parent.parent
    css_path = base_dir / file_name
    with open(css_path, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def format_compact(value):
    """1234567 -> $1.23M, 4.5e12 -> $4.50T (keeps cards readable on small screens)."""
    if value is None:
        return "N/A"
    for limit, suffix in ((1e12, "T"), (1e9, "B"), (1e6, "M"), (1e3, "K")):
        if abs(value) >= limit:
            return f"${value / limit:,.2f}{suffix}"
    return f"${value:,.2f}"
