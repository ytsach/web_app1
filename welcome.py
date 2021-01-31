import streamlit as st
import pandas as pd
import utils
from PIL import Image


def app():
    image = Image.open('i.jpg')
    st.title('Welcome to NBA Data Analyzer')

    st.markdown("""
    **Here you can find data and statistics on NBA players**
    
    """)
    st.markdown("""The main goal of this application is to analyze NBA player's statistics for Nba fantasy purposes.
    Have fun and contact me if there are any issues/suggestions.\n
    Tsach

    ytsach@gmail.com""")
    st.image(image, caption='NBA Data Analyzer',
    use_column_width = True)

    st.markdown(""" ***Last Release 31.1.21.***\n
    **New Features:**\n
    1. Compare players and Trade analyzer scope 7,14,30 days.\n
    2. Player Rater
    
    """)

   
