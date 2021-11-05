import compare_players
import daily_leaders
import welcome
import inj
import trade_analyzer
import rater
import player_form
import cat_leaders
import streamlit as st
PAGES = {
    "Welcome Page": welcome,
    "Player Form": player_form,
    "Compare Players": compare_players,
    "Trade Analyzer":trade_analyzer,
    "Daily Leaders": daily_leaders,
    "Injuery report": inj,
    "Player Rater": rater,
    "Category Leaders":cat_leaders
}
st.sidebar.title('NBA Data Analyzer 2021-2022')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()