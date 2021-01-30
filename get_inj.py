from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

@st.cache
def get_inj_players():
    # NBA season we will be analyzing
    # URL page we will scraping (see image above)
    url = "https://www.basketball-reference.com/friv/injuries.fcgi"
    # this is the HTML from the given URL
    html = urlopen(url)
    soup = BeautifulSoup(html, features="lxml")

    # use findALL() to get the column headers
    soup.findAll('tr', limit=3)
    # use getText()to extract the text we need into a list
    headers = [th.getText() for th in soup.findAll('tr', limit=3)[0].findAll('th')]
    # exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
    # headers = headers[1:]
    # avoid the first header row
    rows = soup.findAll('tr')[1:]
    player_name = [i.next.text for i in rows]
    player_stats = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]

    for i in range(len(player_stats)):
        player_stats[i].insert(0,player_name[i])


    stats = pd.DataFrame(player_stats, columns=headers)
    # return stats.loc[stats['Player'] == name]
    return stats