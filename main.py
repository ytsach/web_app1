import compare_players
import daily_leaders
import welcome
import inj
import trade_analyzer
import rater
import player_form
import streamlit as st
PAGES = {
    "Welcome Page": welcome,
    "Player Form": player_form,
    "Compare Players": compare_players,
    "Trade Analyzer":trade_analyzer,
    "Daily Leaders": daily_leaders,
    "Injuery report": inj,
    "Player Rater": rater,
}
st.sidebar.title('NBA Data Analyzer')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()