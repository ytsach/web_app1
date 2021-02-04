from get_player_stat import get_statistic
import streamlit as st
import pandas as pd
import utils
import new_rate
import altair as alt



def app():
    st.title('NBA Player Stats Comparison')

    st.markdown("""
    Here you can compare two players with updated statistic per game
    """)

    # Web scraping of NBA player stats
    player_stats_data = get_statistic()
    player_stats = player_stats_data[2].drop(columns=['Pos', 'Age']).dropna()
    player_names = list(dict.fromkeys(utils.fix_names([name[0] for name in player_stats_data[0] if name != []])))

    player_one_name = st.sidebar.multiselect('Player 1:', player_names, default=["Bradley Beal"], )
    player_two_name = st.sidebar.multiselect('Player 2:', player_names, default=["Bradley Beal"], )

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

    data_graph_player_one = pd.DataFrame(
        [new_rate.rater(player_name=player_one_name[0], data=get_statistic()[2]),
         new_rate.rater(player_name=player_one_name[0], data=get_statistic('60')[2]),
         new_rate.rater(player_name=player_one_name[0], data=get_statistic('30')[2]),
         new_rate.rater(player_name=player_one_name[0], data=get_statistic('14')[2]),
         new_rate.rater(player_name=player_one_name[0], data=get_statistic('7')[2])], columns=[player_one_name[0]]).astype(float)
    data_graph_player_two = pd.DataFrame(
        [new_rate.rater(player_name=player_two_name[0], data=get_statistic()[2]),
         new_rate.rater(player_name=player_two_name[0], data=get_statistic('60')[2]),
         new_rate.rater(player_name=player_two_name[0], data=get_statistic('30')[2]),
         new_rate.rater(player_name=player_two_name[0], data=get_statistic('14')[2]),
         new_rate.rater(player_name=player_two_name[0], data=get_statistic('7')[2])],
        columns=[player_two_name[0]]).astype(float)
    data_graph_milus = pd.DataFrame(["120 Days", "60 Days", "30 Days", "14 Days", "7 Days"], columns=['Scope'])

    graph_chart = pd.concat([data_graph_milus, data_graph_player_one, data_graph_player_two], axis=1)


    df_player_one = player_stats.loc[player_stats['Player'].str.contains(player_one_name[0])]
    df_player_two = player_stats.loc[player_stats['Player'].str.contains(player_two_name[0])]
    concat_df = pd.concat([df_player_one, df_player_two]).drop(columns=['Player', 'Tm', 'G', 'GS', 'MP'])

    concat_df_dif = concat_df.apply(pd.to_numeric).diff(periods=-1).reset_index(drop=True).style.applymap(
        utils._color_red_or_green).format("{:.1f}")

    st.header('Comparison between {} to {}'.format(player_one_name[0], player_two_name[0]))
    filtered_player_one = utils.get_relevant_data_compare(df_player_one).reset_index()
    filtered_player_two = utils.get_relevant_data_compare(df_player_two).reset_index()

    st.dataframe(filtered_player_one.compare(filtered_player_two, align_axis=0).rename(
        index={'self': player_one_name[0], 'other': player_two_name[0]}, level=-1))

    st.header('Players Rating')
    st.markdown(
        '**The Player Efficiency Rating (PER) is a per-minute rating developed by ESPN.com columnist John Hollinger.**')
    st.text(
        '{} Rating is {}'.format(player_one_name[0], new_rate.rater(player_name=player_one_name[0], data=player_stats)))
    st.text(
        '{} Rating is {}'.format(player_two_name[0], new_rate.rater(player_name=player_two_name[0], data=player_stats)))

    st.header('Discrete difference between {} to {}'.format(player_one_name[0], player_two_name[0]))
    st.dataframe(utils.get_dif_comp(df_player_one.drop(columns=['FG','FGA','FT','FTA']),df_player_two.drop(columns=['FG','FGA','FT','FTA'])))


    #
    # st.header('Rate change in time between {} to {}'.format(player_one_name[0], player_two_name[0]))
    # st.line_chart(graph_chart.rename(columns={'Scope': 'index'}).set_index('index').reindex())
    # # print(graph_chart)


