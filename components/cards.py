
import streamlit as st

def coin_card(col, name, img, selected):
    with col:
        clicked = st.button(
            "",
            key=f"coin_{name}",
            use_container_width=True
        )

        if clicked:
            st.session_state.selected_coin = name
            st.rerun()

        st.markdown(f"""
        <div class="coin-card {'coin-selected' if selected else ''}">
            <img src="{img}" class="coin-logo"/>
            <div class="coin-name">{name}</div>
        </div>
        """, unsafe_allow_html=True)