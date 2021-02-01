from get_players_rater import get_player_rating_league
import streamlit as st
from get_player_stat import get_statistic

import pandas as pd
import utils


def app():
    st.title('NBA Player Rater')

    st.markdown("""
    Here you can find player rating according scope of days.\n
    PER are relevant for all played games.\n
    NBA Analyzer can be change according the scope of time.\n
    the rankings will be change according the NBA Analyzer rate.
    """)
    player_stats_data = get_statistic()
    player_stats = player_stats_data[2].drop(columns=['Pos', 'Age']).dropna()
    player_names = [name[0] for name in player_stats_data[0] if name != []]
    # duplicate_players = player_names.groupby('Player').filter(lambda x: len(x) > 2).drop_duplicates(subset='Player')
    player_names = list(dict.fromkeys(player_names))

    days = st.sidebar.selectbox("Statistic Scope:",
                                ["Total Per Game", "7 Days", "14 Days", "30 Days"])
    if days == "7 Days":
        player_stats = get_statistic('7')[2]
    elif days == "14 Days":
        player_stats = get_statistic('14')[2]
    elif days == "30 Days":
        player_stats = get_statistic('30')[2]

    player_one_name = st.sidebar.multiselect('Player 1:', player_names, default=["Bradley Beal"], )
    st.header('Player Rating')
    st.dataframe(get_player_rating_league(player_name=player_one_name[0],data=player_stats,scope=days))


    st.header('Players Rating')
    st.dataframe(get_player_rating_league(data=player_stats,scope=days))
