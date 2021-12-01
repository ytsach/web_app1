from get_inj import get_inj_players
from get_player_stat import get_statistic
from new_rate import rater
import numpy as np
import streamlit as st
import pandas as pd
import utils
def app():
    st.title('Search For Players According Required Statistics')

    st.markdown("""
    Here you can get players names according specific statistics
    this report was taken from https://www.basketball-reference.com/
    """)

    # Web scraping of NBA player stats
    player_stats_data_60 = get_statistic(days='60')




    player_stats60 = player_stats_data_60[2]
    headers = player_stats60.columns.values
    fgm = st.number_input(label="Enter FG%:")
    FTm = st.number_input(label="Enter FT%:")
    threes = st.number_input(label="Enter 3p:")
    ast = st.number_input(label="Enter AST:")
    reb = st.number_input(label="Enter REB:")
    stl = st.number_input(label="Enter STL:")
    blk = st.number_input(label="Enter BLK:")
    pts = st.number_input(label="Enter PTS:")
    tov = st.number_input(label="Enter TOV:")
    fgm = float("0."+str(fgm).replace(".","").replace("0",""))
    FTm = float("0."+str(FTm).replace(".","").replace("0",""))

    list_pram ={"FG%":fgm,"FT%":FTm,"3P":threes,"AST":ast,"TRB":reb,"STL":stl,"BLK":blk,"PTS":pts,"TOV":tov}
    new_dict ={}
    for i,v in list_pram.items():
        if float(v)!=0.0:
            new_dict[i]=v


    player_match= []

    for index, row in player_stats60.iterrows():
        if len(new_dict) >1:
            len_new_dict = len(new_dict)
            counter = 1
            for key in new_dict.keys():
                if key == "TOV":
                    if counter == len_new_dict:
                        if float(row[key]) < float(new_dict[key]):
                            player_match.append(row)
                    else:
                        if float(row[key]) < float(new_dict[key]):
                            counter += 1
                            continue
                        else:
                            break
                else:
                    if key == "FG%" or key == "FT%":
                        if counter == len_new_dict:
                            if float("0"+str(row[key])) > float(new_dict[key]):
                                player_match.append(row)
                        else:
                            if float("0"+str(row[key])) > float(new_dict[key]):
                                counter +=1
                                continue
                            else:
                                break
                    else:
                        if counter == len_new_dict:
                            if float(row[key]) > float(new_dict[key]):
                                player_match.append(row)
                        else:
                            if float(row[key]) > float(new_dict[key]):
                                counter += 1
                                continue
                            else:
                                break
        else:
            for key in new_dict.keys():
                if key == "TOV":
                    if float(row[key]) < float(new_dict[key]):
                        player_match.append(row)
                else:
                    if key == "FG%" or key == "FT%":

                        if float("0"+str(row[key])) > float(new_dict[key]):
                            player_match.append(row)
                    else:
                        if float(row[key]) > float(new_dict[key]):
                            player_match.append(row)





    if len(player_match) == 0:
            st.text('there is no players for this report')

    else:


        st.text('Players With The Statistic That You Required: ')

        st.dataframe(pd.DataFrame(player_match,columns=headers))





