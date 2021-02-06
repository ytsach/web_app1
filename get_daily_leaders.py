from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
from datetime import datetime
import streamlit as st



@st.cache(suppress_st_warning=True)
def get_daily_leaders():
    page = requests.get('http://www.espn.com/nba/dailyleaders')
    soup = BeautifulSoup(page.text,features="html.parser")
    header = soup.find('tr',attrs={'class':'colhead'})
    columns = [col.get_text() for col in header.find_all('td')]
    final_df = pd.DataFrame(columns=columns)
    players= soup.find_all('tr', attrs = {'class': re.compile('player-46')})
    players_from_leaders = {}
    for player in players:
        stats = [stat.get_text() for stat in player.find_all('td')]
        players_from_leaders[stats[1].lower()] = stats[2].lower()
        tmp_df = pd.DataFrame(stats).transpose()
        tmp_df.columns = columns

        final_df= pd.concat([final_df,tmp_df],ignore_index=True)
    return final_df
# if __name__ == "__main__":
#     print(get_daily_leaders())