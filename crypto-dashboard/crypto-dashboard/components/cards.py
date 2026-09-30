import streamlit as st


def coin_cards_css(coins, selected_name):
    """One <style> block that turns each coin's st.button into a logo card.

    The card IS the Streamlit button (so taps/clicks always work); the logo is drawn
    as the button's background image. Streamlit adds the class `st-key-<key>` to any
    widget that has a key, which is what these selectors hook into.
    """
    rules = []
    for name, info in coins.items():
        selected = name == selected_name
        border = "#16c784" if selected else "rgba(255,255,255,0.08)"
        glow = ("0 0 18px rgba(22,199,132,0.55), 0 0 40px rgba(22,199,132,0.2)"
                if selected else "none")
        rules.append(f"""
        .st-key-coin_{name} button {{
            background-image: url("{info['img']}");
            border-color: {border};
            box-shadow: {glow};
        }}""")
    return "<style>" + "".join(rules) + "</style>"


def coin_card(col, name):
    with col:
        if st.button(name, key=f"coin_{name}"):
            st.session_state.selected_coin = name
            st.rerun()
