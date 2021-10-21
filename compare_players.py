from get_player_stat import get_statistic
import streamlit as st
import pandas as pd
import utils
import new_rate
from charts import get_chart_player

def app():
    st.title('NBA Player Stats Comparison')

    st.markdown("""
    Here you can compare two players with updated statistic per game
    """)

    # Web scraping of NBA player stats
    player_stats_data = get_statistic()
    player_stats = player_stats_data[2].drop(columns=['Pos', 'Age']).dropna()
    player_names = list(dict.fromkeys(utils.fix_names([name[0] for name in player_stats_data[0] if name != []])))

    player_one_name = st.sidebar.multiselect('Player 1:', player_names, default=["LeBron James"], )
    player_two_name = st.sidebar.multiselect('Player 2:', player_names, default=["LeBron James"], )

    days = st.sidebar.selectbox("Statistic Scope:",
                                ["Total Per Game", "7 Days", "14 Days", "30 Days", "60 Days"])
    if days == "7 Days":
        player_stats = get_statistic('7')[2]
    elif days == "14 Days":
        player_stats = get_statistic('14')[2]
    elif days == "30 Days":
        player_stats = get_statistic('30')[2]
    elif days == "60 Days":
        player_stats = get_statistic('60')[2]


    with st.spinner('Loading...'):

        df_player_one = player_stats.loc[player_stats['Player'].str.contains(player_one_name[0])]
        df_player_two = player_stats.loc[player_stats['Player'].str.contains(player_two_name[0])]

        st.header('Comparison between {} to {}'.format(player_one_name[0], player_two_name[0]))
        filtered_player_one = utils.get_relevant_data_compare(df_player_one).reset_index()
        filtered_player_two = utils.get_relevant_data_compare(df_player_two).reset_index()

        st.dataframe(filtered_player_one.compare(filtered_player_two, align_axis=0).rename(
            index={'self': player_one_name[0], 'other': player_two_name[0]}, level=-1))

        st.header('Players Rating')
        st.markdown(
            '**The Player Efficiency Rating (PER) is a per-minute rating developed by ESPN.com columnist John Hollinger.**')
        st.text(
            '{} Rating is {}'.format(player_one_name[0], new_rate.rater(player_name=player_one_name[0], data=player_stats)[0]))
        st.text(
            '{} Rating is {}'.format(player_two_name[0], new_rate.rater(player_name=player_two_name[0], data=player_stats)[0]))

        st.header('Discrete difference between {} to {}'.format(player_one_name[0], player_two_name[0]))
        st.dataframe(utils.get_dif_comp(df_player_one.drop(columns=['FG', 'FGA', 'FT', 'FTA']),
                                        df_player_two.drop(columns=['FG', 'FGA', 'FT', 'FTA'])))

        #
        st.header('Rate change in time between {} to {}'.format(player_one_name[0], player_two_name[0]))
        st.altair_chart(get_chart_player(player_one_name[0],player_two_name[0]), use_container_width=True)
    st.success('Done!')
