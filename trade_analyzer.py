from get_player_stat import get_statistic
import streamlit as st
import pandas as pd
import utils
from new_rate import rater
from charts import get_chart_player
import altair as alt


def app():
    st.title('NBA Trade Analyzer')

    st.markdown("""
    In this page you can analyze trades
    """)

    # Web scraping of NBA player stats
    player_stats_data = get_statistic()
    player_stats = player_stats_data[2].drop(columns=['Pos','Age']).dropna()
    player_names = list(dict.fromkeys(utils.fix_names([name[0] for name in player_stats_data[0] if name != []])))

    team_one_names = st.sidebar.multiselect('Players From Team1:', player_names, default=["Bradley Beal"], )
    team_two_names = st.sidebar.multiselect('Players From Team2:', player_names, default=["Bradley Beal"], )

    days = st.sidebar.selectbox("Statistic Scope:",
                                ["Total Per Game", "7 Days", "14 Days", "30 Days","60 Days"])
    if days == "7 Days":
        player_stats = get_statistic('7')[2]
    elif days == "14 Days":
        player_stats = get_statistic('14')[2]
    elif days == "30 Days":
        player_stats = get_statistic('30')[2]
    elif days == "60 Days":
        player_stats = get_statistic('60')[2]

    with st.spinner('Loading'):
        team_one_df = player_stats.loc[player_stats['Player'].str.contains(team_one_names[0])]
        team_one_rating = float(rater(player_name=team_one_names[0],data=player_stats)[0])

        if len(team_one_names) > 1:
            for player_index in range(1, len(team_one_names)):
                team_one_df = pd.concat(
                    [team_one_df, player_stats.loc[player_stats['Player'].str.contains(team_one_names[player_index])]])
                team_one_rating += float(rater(player_name=team_one_names[player_index],data=player_stats)[0])

        team_two_df = player_stats.loc[player_stats['Player'].str.contains(team_two_names[0])]
        team_two_rating = float(rater(player_name=(team_two_names[0]),data=player_stats)[0])

        if len(team_two_names) > 1:
            for player_index in range(1, len(team_two_names)):
                team_two_df = pd.concat(
                    [team_two_df, player_stats.loc[player_stats['Player'].str.contains(team_two_names[player_index])]])
                team_two_rating += float(rater(player_name=(team_two_names[player_index]),data=player_stats)[0])

        #
        #
        #
        st.header('Comparison between {} to {}'.format(
            str(team_one_names).replace("'", "").replace("[", "").replace("]", "").replace(",", ""),
            str(team_two_names).replace("'", "").replace("[", "").replace("]", "").replace(",", "")))
        st.markdown("""**Team1:**""")
        st.dataframe(team_one_df)

        st.markdown("""**Team2:**""")
        st.dataframe(team_two_df)
        st.markdown("""*Sum for Team1:*""")
        st.dataframe(utils.get_sum_to_trade(team_one_df, len(team_one_names)))
        st.markdown("""*Sum for Team2:*""")
        st.dataframe(utils.get_sum_to_trade(team_two_df, len(team_two_names)))
        #
        st.markdown("""***Team 1 will get:***""")
        st.dataframe(utils.get_dif_trade(utils.get_sum_to_trade(team_one_df, len(team_one_names)),utils.get_sum_to_trade(team_two_df, len(team_two_names))))


        st.markdown("""***Trade Score*:**""")
        st.text("Team1 rating: {}           Team2 rating: {}.".format(team_one_rating, team_two_rating))


        st.header('Rate changes in time between Team1 to Team2')
        st.altair_chart(get_chart_player(team_one_names,team_two_names,team=True), use_container_width=True)
    st.success('Done!')