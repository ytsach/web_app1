from get_daily_leaders import get_daily_leaders
import streamlit as st
import pandas as pd
from datetime import datetime



def app():
    st.title('{} Daily leaders'.format(datetime.today().strftime('%Y-%m-%d')))

    st.markdown("""
    Here you can find the leaders of the day accoriding ESPN rating
    """)
    with st.spinner('Loading'):

        # Web scraping of NBA player stats
        leaders_data = get_daily_leaders()


        # st.header('Chosen Player one is: {}'.format(player_one_name[0]))
        st.dataframe(leaders_data)
    st.spinner('Done!')

   

