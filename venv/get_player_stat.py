from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

@st.cache
def get_statistic():
    # NBA season we will be analyzing
    # URL page we will scraping (see image above)
    url = "https://www.basketball-reference.com/leagues/NBA_2021_per_game.html"
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

    stats = pd.DataFrame(player_stats, columns = headers)
    # return stats.loc[stats['Player'] == name]
    return player_stats , headers, stats
# if __name__ == "__main__":
#     print(get_statistic())[2]