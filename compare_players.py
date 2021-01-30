from get_player_stat import get_statistic
import streamlit as st
import pandas as pd
import utils


def app():
    st.title('NBA Player Stats Comparison')

    st.markdown("""
    Here you can compare two players with updated statistic per game
    """)

    # Web scraping of NBA player stats
    player_stats_data = get_statistic()
    player_stats = player_stats_data[2]
    player_names = [name[0] for name in player_stats_data[0] if name != []]

    player_one_name = st.sidebar.multiselect('Player 1:', player_names,default=["Bradley Beal"],)
    player_two_name = st.sidebar.multiselect('Player 2:', player_names,default=["Bradley Beal"],)

    df_player_one = player_stats.loc[player_stats['Player'] == player_one_name[0]]
    df_player_two = player_stats.loc[player_stats['Player'] == player_two_name[0]]

    concat_df = pd.concat([df_player_one,df_player_two]).drop(columns=['Player','Pos','Age','Tm','G','GS','MP'])
    concat_df_dif = concat_df.apply(pd.to_numeric).diff()


    st.header('Comparison between {} to {}'.format(player_one_name[0],player_two_name[0]))
    filtered_player_one = utils.get_relevant_data_compare(df_player_one).reset_index()
    filtered_player_two = utils.get_relevant_data_compare(df_player_two).reset_index()
    st.dataframe(filtered_player_one.compare(filtered_player_two, align_axis=0).rename(index={'self': player_one_name[0], 'other': player_two_name[0]}, level=-1))

    st.header('Players Rating')
    st.markdown('**The Player Efficiency Rating (PER) is a per-minute rating developed by ESPN.com columnist John Hollinger.**')
    st.text('{} Rating is {}'.format(player_one_name[0],utils.get_player_rating(player_one_name[0])))
    st.text('{} Rating is {}'.format(player_two_name[0],utils.get_player_rating(player_two_name[0])))

    st.header('Discrete difference between {} to {}'.format(player_one_name[0],player_two_name[0]))
    st.dataframe(concat_df_dif)
