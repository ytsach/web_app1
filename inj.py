from get_inj import get_inj_players
from get_player_stat import get_statistic

import streamlit as st
import pandas as pd
import utils


def app():
    st.title('NBA Injurey updated report')

    st.markdown("""
    In this page you can find updated NBA Injurey report.
    this report was taken from https://www.basketball-reference.com/
    """)

    # Web scraping of NBA player stats
    player_stats_data = get_statistic()
    player_inj_data = get_inj_players()

    player_names = [name[0] for name in player_stats_data[0] if name != []]
    teams_names = [name[3] for name in player_stats_data[0] if name != []]

    player_one_name = st.sidebar.multiselect('Player :', player_names, default=["Bradley Beal"], )
    teams_name_choose = st.sidebar.multiselect('Team :', teams_names, default=["MIA"], )


    df_player_one = player_inj_data.loc[player_inj_data['Player'] == player_one_name[0]]

    st.header('Injurey Report for {}: '.format(player_one_name[0]))
    st.dataframe(df_player_one)

    st.header('Full Injurey Report: ')
    st.dataframe(player_inj_data)



