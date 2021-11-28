from get_inj import get_inj_players
from get_player_stat import get_statistic
from new_rate import rater
import numpy as np
import streamlit as st
import pandas as pd
import utils


def app():
    st.title('Sleepers Players')

    st.markdown("""
    Here you can see players that in the last x days days their rating was higher then average
    this report was taken from https://www.basketball-reference.com/
    """)

    # Web scraping of NBA player stats
    player_stats_data_60 = get_statistic(days='60')

    player_names = list(dict.fromkeys(utils.fix_names([name[0] for name in player_stats_data_60[0] if name != []])))
    days = st.sidebar.selectbox("days:",
                                ["7", "14", "21", "30"])
    with st.spinner('Loading...'):
        player_stats_days = get_statistic(days=days)[2]


        player_stats60 = player_stats_data_60[2]
        headers = player_stats60.columns.values

        sleepers_df = []

        for player in player_names:
            df_player_one_days = player_stats_days.loc[player_stats_days['Player'].str.contains(player)]
            if df_player_one_days.empty:
                continue
            df_player_one60 = player_stats60.loc[player_stats60['Player'].str.contains(player)]
            df_player_one_days_rating = float(rater(player_name=player, data=df_player_one_days)[0])
            df_player_one_60_rating = float(rater(player_name=player, data=df_player_one60)[0])
            if df_player_one_days_rating == 0 or df_player_one_60_rating ==0:
                continue
            percent = ((df_player_one_days_rating/df_player_one_60_rating) *100)
            if percent > 200 and float(df_player_one_days['MP']) > 18:
                sleepers_df.append(df_player_one_days)



        if len(sleepers_df) == 0:
            st.text('there is no players that their rating improved more than 250% in {} days comparing to 60 days:'.format(days))

        else:
            st.text('Player that their rating improved more than 200% in {} days comparing to 60 days:'.format(days))

            st.dataframe(pd.DataFrame(np.concatenate(sleepers_df),columns=headers))

















        #
        # st.text('{} last 7:'.format(player_one_name[0]))
        # st.dataframe(df_player_one7)
        #
        # st.text('{} last 14:'.format(player_one_name[0]))
        # st.dataframe(df_player_one14)
        #
        # st.text('{} last 21:'.format(player_one_name[0]))
        # st.dataframe(df_player_one21)
        #
        # st.text('{} last 30:'.format(player_one_name[0]))
        # st.dataframe(df_player_one30)
        #
        # st.text('{} last 45:'.format(player_one_name[0]))
        # st.dataframe(df_player_one45)
        #
        # st.text('{} last 60:'.format(player_one_name[0]))
        # st.dataframe(df_player_one60)
        # chart_data=pd.DataFrame([new_rate.rater(player_name=player_one_name[0],data=get_statistic()[2])[1]]).transpose()
        # df_new = chart_data.rename(columns={0:player_one_name[0]},index={0:'FGM',1:'FGmiss',2:'FT',3:'FTmiss',4:'3P',5:'REB',6:'AST',7:'STL',8:'BLK',9:'TOV',10:'PTS'})
        # st.bar_chart(df_new)
    st.success('Done!...')




    # df_player_one = player_inj_data.loc[player_inj_data['Player'] == player_one_name[0]]
    #
    # st.header('Injurey Report for {}: '.format(player_one_name[0]))
    # st.dataframe(df_player_one)
    #
    # st.header('Full Injurey Report: ')
    # st.dataframe(player_inj_data)



