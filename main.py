import compare_players
import daily_leaders
import welcome
import inj
import trade_analyzer
import rater
import player_form
import cat_leaders
import sleepers
import player_stat_year
import search_for_player
import streamlit as st
PAGES = {
    "Welcome Page": welcome,
    "Player Form": player_form,
    "Compare Players": compare_players,
    "Trade Analyzer":trade_analyzer,
    "Daily Leaders": daily_leaders,
    "Injury report": inj,
    "Player Rater": rater,
    "Category Leaders":cat_leaders,
    "Player Statistic According Year":player_stat_year,
    "Sleepers":sleepers,
    "Search For Player":search_for_player
}
st.sidebar.title('NBA Data Analyzer 2022-2023')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()