import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: #6C79FF !important;
            }

            .stApp div[data-testid='stColumn']{
                background-color:#E0E3FF !important;
                padding: 1.2rem !important;
                border-radius: 1.5rem !important;
            }
        </style>
       
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #ffb6c1 !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=DM+Serif+Display:ital@0;1&family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Manrope:wght@200..800&family=Outfit:wght@100..900&family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

          # Hide top bar of streamlit 
          /* #MainMenu, footer, header {
                visibility: hidden;
            */

            .block-container{
                padding-top:0rem !important;
                padding-bottom:0rem !important;

            }
          

            h1{
                font-family:'Climate Crisis',sans-serif !important;
                font-size:2.2rem !important;
                line-height:0.8 !important;
                margin-bottom:0 rem !important; 
              # margin-left:7rem !important;
                font-weight:300px;
                color:#E0E3FF;
                text-align:center
            }

            
            h2{
                font-family:'Climate Crisis',sans-serif !important;
                font-size:2rem !important;
                line-height:1.1 !important;
                margin-bottom:0 rem !important; 
                color:#E0E3FF
            }

            h3,h4,p,span{
                font-family:'Outfit',sans-serif;
                font-size:3rem
            }

            button[kind='primary']{
                border-radius:1.5rem !important;
                background: #6C79FF !important;
                color:white !important;
                padding:10px 20px !important
                border:none !important
                transition :transform 0.25s ease-in-out !important
            }

            button[kind='secondary']{
                border-radius:1.5rem !important;
                background: #EB459E !important;
                color:white !important;
                padding:10px 20px !important
                border:none !important
                transition :transform 0.25s ease-in-out !important
            }

            
            button[kind='tertiary']{
                border-radius:1.5rem !important;
                background: #EB459E !important;
                color:white !important;
                padding:10px 20px !important
                border:none !important
                transition :transform 0.25s ease-in-out !important
            }

            button:hover{
                transform:scale(1.05)
            }
        </style>
    """, unsafe_allow_html=True)

   