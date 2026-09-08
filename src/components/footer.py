import streamlit as st

def footer_home():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="display:flex; gap:6px; items-align:center; justify-content:center; margin-top:2rem;">
        <p style='font-weight:bold;color:white;'> Created with ❤️ by <b>@VBatta <b> </p>
            
        </div>
    """, unsafe_allow_html=True)

def footer_dashboard():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="display:flex; gap:6px; items-align:center; justify-content:center; margin-top:2rem;">
        <p style='font-weight:bold;color:black;'> Created with ❤️ by <b>@VBatta <b> </p>
            
        </div>
    """, unsafe_allow_html=True)