from get_inj import get_inj_players
from get_player_stat import get_statistic
import new_rate

import streamlit as st
import pandas as pd
import utils


def app():
    st.title('Player Form statistic according Year')

    st.markdown("""
    In this page you can find Player stats according time.
    this report was taken from https://www.basketball-reference.com/
    """)

    # Web scraping of NBA player stats
    player_stats_data = get_statistic()
    player_names = list(dict.fromkeys(utils.fix_names([name[0] for name in player_stats_data[0] if name != []])))

    player_one_name = st.sidebar.multiselect('Player :', player_names, default=["LeBron James"], )
    year = st.sidebar.selectbox("Statistic Year:",
                                ["21","20","19","18"])
    with st.spinner('Loading...'):
        player_stat_according_year = get_statistic(year=year)[2].drop(columns=['FG','FGA','FT','FTA'])
        player_stat_according_year22 = get_statistic(year="22")[2].drop(columns=['FG','FGA','FT','FTA'])

        df_player_one_year = player_stat_according_year.loc[player_stat_according_year['Player'].str.contains(player_one_name[0])]
        df_player_one_year22 = player_stat_according_year22.loc[player_stat_according_year22['Player'].str.contains(player_one_name[0])]

        st.markdown("""**{} Statistics for year 2022:**""".format(player_one_name[0]))
        st.dataframe(df_player_one_year22)

        st.markdown("""**{} Statistics for year 20{}:**""".format(player_one_name[0],year))
        st.dataframe(df_player_one_year)

    st.success('Done!...')




    # df_player_one = player_inj_data.loc[player_inj_data['Player'] == player_one_name[0]]
    #
    # st.header('Injurey Report for {}: '.format(player_one_name[0]))
    # st.dataframe(df_player_one)
    #
    # st.header('Full Injurey Report: ')
    # st.dataframe(player_inj_data)



