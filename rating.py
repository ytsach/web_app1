from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st


@st.cache
def get_rating_statistic(player_name=None, all_data=None):
    # NBA season we will be analyzing
    # URL page we will scraping (see image above)
    url = "https://www.basketball-reference.com/leagues/NBA_2022_advanced.html"
    # this is the HTML from the given URL
    html = urlopen(url)
    soup = BeautifulSoup(html, features="lxml")

    # use findALL() to get the column headers
    soup.findAll('tr', limit=2)
    # use getText()to extract the text we need into a list
    headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
    # exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
    headers = headers[1:]
    indices = 18, 23
    headers = [i for j, i in enumerate(headers) if j not in indices]
    # avoid the first header row
    rows = soup.findAll('tr')[1:]
    player_stats = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]

    new_player_stat = []
    for lst in player_stats:
        new_player_stat.append(list(filter(lambda x: x != "", lst)))
    stats = pd.DataFrame(new_player_stat, columns=headers).drop(
        columns=['USG%', 'Pos', 'Age', 'TS%', 'Tm', '3PAr', 'FTr', 'ORB%', 'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%',
                 'TOV%', 'OWS', 'DWS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP', 'WS']).dropna()
    # return stats.loc[stats['Player'] == name]
    if all_data:
        return stats
    else:
        return stats.loc[stats['Player'].str.contains(player_name)]

# if __name__ == "__main__":
#     print(rater('Bradley Beal'))
#     pass
