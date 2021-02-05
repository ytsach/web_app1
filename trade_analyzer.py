from get_player_stat import get_statistic
import streamlit as st
import pandas as pd
import utils
from new_rate import rater
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

    team_one_df = player_stats.loc[player_stats['Player'].str.contains(team_one_names[0])]
    team_one_rating = float(rater(player_name=team_one_names[0],data=player_stats))

    if len(team_one_names) > 1:
        for player_index in range(1, len(team_one_names)):
            team_one_df = pd.concat(
                [team_one_df, player_stats.loc[player_stats['Player'].str.contains(team_one_names[player_index])]])
            team_one_rating += float(rater(player_name=team_one_names[player_index],data=player_stats))

    team_two_df = player_stats.loc[player_stats['Player'].str.contains(team_two_names[0])]
    team_two_rating = float(rater(player_name=(team_two_names[0]),data=player_stats))

    if len(team_two_names) > 1:
        for player_index in range(1, len(team_two_names)):
            team_two_df = pd.concat(
                [team_two_df, player_stats.loc[player_stats['Player'].str.contains(team_two_names[player_index])]])
            team_two_rating += float(rater(player_name=(team_two_names[player_index]),data=player_stats))

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

    # data_graph_player_one = [new_rate.rater(player_name=player_one_name[0], data=get_statistic()[2]),
    #                          new_rate.rater(player_name=player_one_name[0], data=get_statistic('60')[2]),
    #                          new_rate.rater(player_name=player_one_name[0], data=get_statistic('30')[2]),
    #                          new_rate.rater(player_name=player_one_name[0], data=get_statistic('14')[2]),
    #                          new_rate.rater(player_name=player_one_name[0], data=get_statistic('7')[2])]
    # data_graph_player_two = [new_rate.rater(player_name=player_two_name[0], data=get_statistic()[2]),
    #                          new_rate.rater(player_name=player_two_name[0], data=get_statistic('60')[2]),
    #                          new_rate.rater(player_name=player_two_name[0], data=get_statistic('30')[2]),
    #                          new_rate.rater(player_name=player_two_name[0], data=get_statistic('14')[2]),
    #                          new_rate.rater(player_name=player_two_name[0], data=get_statistic('7')[2])]
    #
    # df_chart = pd.DataFrame(
    #     {
    #         'Days': [120, 60, 30, 14, 7],
    #         "Team1": team_one_rating,
    #         "Team2": team_two_rating
    #     },
    #     columns=['Days', "Team1", "Team2"]
    # )
    #
    # df_chart = df_chart.melt('Days', var_name='name', value_name='value')
    #
    #
    # chart = alt.Chart(df_chart).mark_line().encode(
    #     x=alt.X(field='Days',type='nominal',sort='x'),
    #     y=alt.Y('value:Q'),
    #     color=alt.Color("name:N")
    # ).properties(title="Stat Chart")
    #
    # st.header('Rate changes in time between Team1 to Team2')
    # st.altair_chart(chart, use_container_width=True)