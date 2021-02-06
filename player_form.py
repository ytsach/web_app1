from get_inj import get_inj_players
from get_player_stat import get_statistic
import new_rate

import streamlit as st
import pandas as pd
import utils


def app():
    st.title('Player Form According Time')

    st.markdown("""
    In this page you can find Player stats according time.
    this report was taken from https://www.basketball-reference.com/
    """)

    # Web scraping of NBA player stats
    player_stats_data = get_statistic()

    player_names = list(dict.fromkeys(utils.fix_names([name[0] for name in player_stats_data[0] if name != []])))

    player_one_name = st.sidebar.multiselect('Player :', player_names, default=["Bradley Beal"], )
    with st.spinner('Loading...'):
        player_stats7 = get_statistic('7')[2].drop(columns=['FG','FGA','FT','FTA'])
        player_stats14 = get_statistic('14')[2].drop(columns=['FG','FGA','FT','FTA'])
        player_stats21 = get_statistic('21')[2].drop(columns=['FG','FGA','FT','FTA'])
        player_stats30 = get_statistic('30')[2].drop(columns=['FG','FGA','FT','FTA'])
        player_stats45 = get_statistic('45')[2].drop(columns=['FG','FGA','FT','FTA'])
        player_stats60 = get_statistic('60')[2].drop(columns=['FG','FGA','FT','FTA'])

        df_player_one7 = player_stats7.loc[player_stats7['Player'].str.contains(player_one_name[0])]
        df_player_one14 = player_stats14.loc[player_stats14['Player'].str.contains(player_one_name[0])]
        df_player_one21 = player_stats21.loc[player_stats21['Player'].str.contains(player_one_name[0])]
        df_player_one30 = player_stats30.loc[player_stats30['Player'].str.contains(player_one_name[0])]
        df_player_one45 = player_stats45.loc[player_stats45['Player'].str.contains(player_one_name[0])]
        df_player_one60 = player_stats60.loc[player_stats60['Player'].str.contains(player_one_name[0])]

        st.text('{} last 7:'.format(player_one_name[0]))
        st.dataframe(df_player_one7)

        st.text('{} last 14:'.format(player_one_name[0]))
        st.dataframe(df_player_one14)

        st.text('{} last 21:'.format(player_one_name[0]))
        st.dataframe(df_player_one21)

        st.text('{} last 30:'.format(player_one_name[0]))
        st.dataframe(df_player_one30)

        st.text('{} last 45:'.format(player_one_name[0]))
        st.dataframe(df_player_one45)

        st.text('{} last 60:'.format(player_one_name[0]))
        st.dataframe(df_player_one60)
        chart_data=pd.DataFrame([new_rate.rater(player_name=player_one_name[0],data=get_statistic()[2])[1]]).transpose()
        df_new = chart_data.rename(columns={0:player_one_name[0]},index={0:'FGM',1:'FGmiss',2:'FT',3:'FTmiss',4:'3P',5:'REB',6:'AST',7:'STL',8:'BLK',9:'TOV',10:'PTS'})
        st.bar_chart(df_new)
    st.success('Done!...')




    # df_player_one = player_inj_data.loc[player_inj_data['Player'] == player_one_name[0]]
    #
    # st.header('Injurey Report for {}: '.format(player_one_name[0]))
    # st.dataframe(df_player_one)
    #
    # st.header('Full Injurey Report: ')
    # st.dataframe(player_inj_data)



