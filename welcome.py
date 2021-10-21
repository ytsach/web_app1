import streamlit as st
import pandas as pd
import utils
from PIL import Image


def app():
    image = Image.open('i.jpg')
    st.title('Welcome to NBA Data Analyzer2021-2022')

    st.markdown("""
    **Here you can find data and statistics on NBA players**
    
    """)
    st.markdown("""The main goal of this application is to analyze NBA player's statistics for Nba fantasy purposes.
    Have fun and contact me if there are any issues/suggestions.\n
    Tsach

    ytsach@gmail.com""")
    st.image(image, caption='NBA Data Analyzer',
    use_column_width = True)

    st.markdown(""" New season 21-22, Good luck
    
    """)

   
