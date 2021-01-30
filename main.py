import compare_players
import daily_leaders
import welcome
import inj
import trade_analyzer
import streamlit as st
PAGES = {
    "Welcome Page": welcome,
    "Compare Players": compare_players,
    "Trade Analyzer":trade_analyzer,
    "Daily Leaders": daily_leaders,
    "Injuery report": inj,
}
st.sidebar.title('NBA Data Anlayzer')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()