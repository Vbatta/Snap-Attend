import streamlit as st

def header_home():

    logo_url = "https://raw.githubusercontent.com/Vbatta/DDoS-Attack/refs/heads/main/ChatGPT%20Image%20Sep%2012%2C%202026%2C%2008_38_23%20PM.png"

    st.markdown(f"""
        <div style="display:flex; flex-direction:row; align-items:center; justify-content:center; margin-bottom:20px;margin-top:0px;gap:25px">
            <img src="{logo_url}" style="height:160px;>" />
            <h1 style="text-align:center; color:#E0E3FF;" >SNAP <br/>ATTEND </h1>
        </div>
    """, unsafe_allow_html=True)

def header_dashboard():

    logo_url = "https://raw.githubusercontent.com/Vbatta/DDoS-Attack/refs/heads/main/ChatGPT%20Image%20Sep%2012%2C%202026%2C%2008_38_23%20PM.png"

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center;gap:10px; margin-bottom:20px;margin-top:0px">
            <img src="{logo_url}" style="height:160px; width:130px" />
            <h2 style="text-align:center; color:#909090;line-height:1.2;">SNAP <br/>ATTEND </h2>
        </div>
    """, unsafe_allow_html=True)