import streamlit as st
import pandas as pd
from get_player_stat import get_statistic
import utils

def get_top_ast(player_stats):
    player_stats = player_stats[['Player','AST','Tm','G','GS','MP','FG','FGA','FG%','3P','FT','FTA','FT%','TRB','STL','BLK','TOV','PTS']]

    player_stats['AST'] = player_stats['AST'].astype('float')
    st.dataframe(player_stats.sort_values(by=["AST"], ascending=False).reset_index().drop(columns=['index']).dropna())

def get_top_reb(player_stats):
    player_stats = player_stats[['Player','TRB','Tm','G','GS','MP','FG','FGA','FG%','3P','FT','FTA','FT%','AST','STL','BLK','TOV','PTS']]

    player_stats['TRB'] = player_stats['TRB'].astype('float')
    st.dataframe(player_stats.sort_values(by=["TRB"], ascending=False,kind="stable").reset_index().drop(columns=['index']).dropna())

def get_top_blk(player_stats):
    player_stats = player_stats[['Player','BLK','Tm','G','GS','MP','FG','FGA','FG%','3P','FT','FTA','FT%','TRB','AST','STL','TOV','PTS']]

    player_stats['BLK'] = player_stats['BLK'].astype('float')
    st.dataframe(player_stats.sort_values(by=["BLK"], ascending=False).reset_index().drop(columns=['index']).dropna())
def get_top_stl(player_stats):
    player_stats = player_stats[['Player','STL','Tm','G','GS','MP','FG','FGA','FG%','3P','FT','FTA','FT%','TRB','AST','BLK','TOV','PTS']]

    player_stats['STL'] = player_stats['STL'].astype('float')
    st.dataframe(player_stats.sort_values(by=["STL"], ascending=False).reset_index().drop(columns=['index']).dropna())
def get_top_to(player_stats):
    player_stats = player_stats[['Player','TOV','Tm','G','GS','MP','FG','FGA','FG%','3P','FT','FTA','FT%','TRB','AST','STL','BLK','PTS']]

    player_stats['TOV'] = player_stats['TOV'].astype('float')

    st.dataframe(player_stats.sort_values(by=["TOV"], ascending=False).reset_index().drop(columns=['index']).dropna())
def get_top_3p(player_stats):
    player_stats = player_stats[['Player','3P','Tm','G','GS','MP','FG','FGA','FG%','FT','FTA','FT%','TRB','AST','STL','BLK','TOV','PTS']]

    player_stats['3P'] = player_stats['3P'].astype('float')

    st.dataframe(player_stats.sort_values(by=["3P"], ascending=False).reset_index().drop(columns=['index']).dropna())
def get_top_pts(player_stats):
    player_stats['PTS'] = player_stats['PTS'].astype('float')
    player_stats = player_stats[['Player','PTS','Tm','G','GS','MP','FG','FGA','FG%','3P','FT','FTA','FT%','TRB','AST','STL','BLK','TOV']]
    st.dataframe(player_stats.sort_values(by=["PTS"], ascending=False).reset_index().drop(columns=['index']).dropna())

def get_top_fg(player_stats):
    new_fg_list = []
    for index, row in player_stats.iterrows():
        if float(row['G']) > 4 and float(row['MP']) > 12:
            new_fg_list.append(row)
    new_fg_pd = pd.DataFrame(new_fg_list)
    new_fg_pd = new_fg_pd[['Player','FG%','Tm','G','GS','MP','FG','FGA','3P','FT','FTA','FT%','TRB','AST','STL','BLK','TOV','PTS']]

    st.dataframe(new_fg_pd.sort_values(by=["FG%"], ascending=False).reset_index().drop(columns=['index']).dropna())

def get_top_ft(player_stats):
    new_ft_list = []
    for index, row in player_stats.iterrows():
        if float(row['G']) > 4 and float(row['MP']) > 12 and float(row['FTA']) >2.5:
            new_ft_list.append(row)
    new_ft_pd = pd.DataFrame(new_ft_list)
    new_ft_pd = new_ft_pd[['Player','FT%','Tm','G','GS','MP','FG','FG%','FG%','3P','FT','FTA','TRB','AST','STL','BLK','TOV','PTS']]

    st.dataframe(new_ft_pd.sort_values(by=["FT%"], ascending=False).reset_index().drop(columns=['index']).dropna())





def app():
    st.title('NBA Player Category leaders')

    st.markdown("""
        Here you can get the category leaders 
        """)

    # Web scraping of NBA player stats
    player_stats_data = get_statistic()
    player_stats = player_stats_data[2].drop(columns=['Pos', 'Age']).dropna()
    cat_array = ["FG","FT","3P","REB","AST","STL","BLK","TO","PTS"]

    cat = st.sidebar.selectbox('Category Leaders:', cat_array)

    if cat == "AST":
        get_top_ast(player_stats)
    elif cat == "REB":
        get_top_reb(player_stats)
    elif cat == "BLK":
        get_top_blk(player_stats)
    elif cat == "STL":
        get_top_stl(player_stats)
    elif cat == "TO":
        get_top_to(player_stats)
    elif cat == "PTS":
        get_top_pts(player_stats)
    elif cat == "3P":
        get_top_3p(player_stats)
    elif cat == "FG":
        get_top_fg(player_stats)
    elif cat == "FT":
        get_top_ft(player_stats)



