from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
from get_player_stat import get_statistic
from utils import get_player_rating
from rating import get_rating_statistic
from new_rate import rater


@st.cache
def get_player_rating_league(player_name=None, data=get_statistic()[2],scope='Total Per Game'):
    all_data_to_rate = get_rating_statistic(all_data=True).dropna().drop_duplicates(subset=['Player'])
    duplicate = all_data_to_rate.groupby('Player').filter(lambda x: len(x) > 2).drop_duplicates(subset='Player')
    all_data_to_rate = pd.concat([all_data_to_rate, duplicate])
    for index, row in all_data_to_rate.iterrows():
        all_data_to_rate.loc[index, 'NBA Analyzer Rate scope {}'.format(scope)] = int(float(rater(player_name=row['Player'], data=data)))

    if player_name:
        all_data_to_rate = all_data_to_rate.sort_values('NBA Analyzer Rate scope {}'.format(scope), ascending=False).reset_index()
        return all_data_to_rate.loc[all_data_to_rate['Player'] == player_name]
    else:
        return all_data_to_rate.sort_values('NBA Analyzer Rate scope {}'.format(scope), ascending=False).reset_index()
# if __name__ == "__main__":
#     x = get_player_rating_league()
#     print(x)
#     pass
