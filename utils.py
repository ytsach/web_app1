import pandas as pd
from rating import get_rating_statistic


def get_relevant_data_compare(dataf):
    df = pd.DataFrame(dataf)
    # return df.drop(columns=['Player', 'Pos', 'Age', 'Tm'])
    return df.drop(columns=['Player', 'Tm'])


def get_player_rating(player,all_data=None,statistic=pd.DataFrame({'A' : []})):
    if statistic.empty:
        player_data = get_rating_statistic(player)
    else:
        player_data = statistic.loc[statistic['Player']==player]
    # rating formula is PER
    per = float(player_data.iloc[0]['PER'])
    g = float(player_data.iloc[0]['G'])
    mp = float(player_data.iloc[0]['MP'])
    if all_data:
        return str(int((per * mp) / g)), per, g, mp
    else:
        return str(int((per * mp) / g))


def get_sum_to_trade(players_df, len_players):
    pts = "{:.1f}".format(players_df['PTS'].apply(pd.to_numeric).sum())
    stl = "{:.1f}".format(players_df['STL'].apply(pd.to_numeric).sum())
    threes = "{:.1f}".format(players_df['3P'].apply(pd.to_numeric).sum())
    reb = "{:.1f}".format(players_df['TRB'].apply(pd.to_numeric).sum())
    blk = "{:.1f}".format(players_df['BLK'].apply(pd.to_numeric).sum())
    fg = "{:.2f}".format(players_df['FG%'].apply(pd.to_numeric).sum() / len_players)
    ft = "{:.2f}".format(players_df['FT%'].apply(pd.to_numeric).sum() / len_players)
    ast = "{:.1f}".format(players_df['AST'].apply(pd.to_numeric).sum())
    tov = "{:.1f}".format(players_df['TOV'].apply(pd.to_numeric).sum())
    data_combined = [fg, ft, threes, reb, ast, stl, blk, tov, pts]
    data_df = pd.DataFrame([data_combined], columns=['FG%', 'FT%', '3P', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PTS'])
    return data_df

def clean_n_days_stat(dataf):
    df = pd.DataFrame(dataf)
    return df.drop(columns=['3PA', '3P%', 'ORB', 'DRB', 'PF','GmSc'])

def clean_per_game_stat(dataf):
    df = pd.DataFrame(dataf)
    return df.drop(columns=['3PA', '3P%', '2P','2PA','eFG%','2P%','ORB', 'DRB', 'PF'])

