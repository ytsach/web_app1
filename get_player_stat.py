from urllib.request import urlopen
from bs4 import BeautifulSoup
from get_inj import get_inj_players
import pandas as pd
import streamlit as st
import utils

@st.cache(suppress_st_warning=True)
def get_statistic(days=None,totals=None,year=22):
    # NBA season we will be analyzing
    # URL page we will scraping (see image above)
    # if days exists then it will take last n days stat
    if days:
        url = "https://www.basketball-reference.com/friv/last_n_days.fcgi?n={}&type=per_game".format(days)
    elif totals:
        url = "https://www.basketball-reference.com/leagues/NBA_20{}_totals.html".format(year)
    else:
        url = "https://www.basketball-reference.com/leagues/NBA_20{}_per_game.html".format(year)

    # this is the HTML from the given URL
    html = urlopen(url)
    soup = BeautifulSoup(html,features="lxml")

    # use findALL() to get the column headers
    soup.findAll('tr', limit=2)
    # use getText()to extract the text we need into a list
    headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
    # exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
    headers = headers[1:]
    # avoid the first header row
    rows = soup.findAll('tr')[1:]
    player_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]

    stats = pd.DataFrame(player_stats, columns = headers).drop_duplicates(subset=['Player'])
    duplicate_players = stats.groupby('Player').filter(lambda x: len(x) > 2).drop_duplicates(subset='Player')
    stats = pd.concat([stats,duplicate_players])

    if days:
        stats = utils.clean_n_days_stat(stats)
    else:
        stats = utils.clean_per_game_stat(stats)

    # inj_players =get_inj_players()
    # headers.append('INJ')
    # for index,row in stats.iterrows():
    #     if str(row['Player']) in str(inj_players):
    #         row['INJ'] = "True"
    #     else:
    #         row['INJ'] = "False"

    return player_stats , headers, stats.dropna().drop_duplicates(subset=['Player'])
# if __name__ == "__main__":
#     print(get_statistic())[2]