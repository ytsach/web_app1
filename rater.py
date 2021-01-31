from get_players_rater import get_player_rating_league
import streamlit as st
from get_player_stat import get_statistic

import pandas as pd
import utils


def app():
    st.title('NBA Player Rater')

    st.markdown("""
    Here you can fine player rating according the formula (PER*min_played)/games_played
    """)
    player_stats_data = get_statistic()
    player_stats = player_stats_data[2].drop(columns=['Pos', 'Age'])
    player_names = [name[0] for name in player_stats_data[0] if name != []]
    # duplicate_players = player_names.groupby('Player').filter(lambda x: len(x) > 2).drop_duplicates(subset='Player')
    player_names = list(dict.fromkeys(player_names))


    player_one_name = st.sidebar.multiselect('Player 1:', player_names, default=["Bradley Beal"], )
    st.header('Player Rating')
    st.dataframe(get_player_rating_league(player_name=player_one_name[0]))


    st.header('Players Rating')
    st.dataframe(get_player_rating_league())
