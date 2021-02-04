import pandas as pd
from rating import get_rating_statistic


def get_relevant_data_compare(dataf):
    df = pd.DataFrame(dataf)
    # return df.drop(columns=['Player', 'Pos', 'Age', 'Tm'])
    return df.drop(columns=['Player', 'Tm'])


def get_player_rating(player, all_data=None, statistic=pd.DataFrame({'A': []})):
    if statistic.empty:
        player_data = get_rating_statistic(player)
    else:
        player_data = statistic.loc[statistic['Player'] == player]
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
    return df.drop(columns=['3PA', '3P%', 'ORB', 'DRB', 'PF', 'GmSc'])


def clean_per_game_stat(dataf):
    df = pd.DataFrame(dataf)
    return df.drop(columns=['3PA', '3P%', '2P', '2PA', 'eFG%', '2P%', 'ORB', 'DRB', 'PF'])


def fix_names(names):
    for i, name in enumerate(names):
        if name == 'Marvin Bagley III':
            names.pop(i)
            names.append('Marvin Bagley')
        elif name == 'Kelly Oubre Jr.':
            names.pop(i)
            names.append('Kelly Oubre')
        elif name == 'Larry Nance Jr.':
            names.pop(i)
            names.append('Larry Nance')
    return names


def _color_red_or_green(val):
    color = 'red' if val < 0 else 'green'
    return 'color: %s' % color


def get_dif_trade(df1, df2):
    fg1, fg2 = df1.iloc[0]['FG%'], df2.iloc[0]['FG%']
    ft1, ft2 = df1.iloc[0]['FT%'], df2.iloc[0]['FT%']
    three1, three2 = df1.iloc[0]['3P'], df2.iloc[0]['3P']
    reb1, reb2 = df1.iloc[0]['REB'], df2.iloc[0]['REB']
    ast1, ast2 = df1.iloc[0]['AST'], df2.iloc[0]['AST']
    stl1, stl2 = df1.iloc[0]['STL'], df2.iloc[0]['STL']
    blk1, blk2 = df1.iloc[0]['BLK'], df2.iloc[0]['BLK']
    tov1, tov2 = df1.iloc[0]['TOV'], df2.iloc[0]['TOV']
    pts1, pts2 = df1.iloc[0]['PTS'], df2.iloc[0]['PTS']
    return pd.DataFrame([[float(fg2) - float(fg1),
                          float(ft2) - float(ft1),
                          float(three2)-float(three1),
                          float(reb2)-float(reb1),
                          float(ast2)-float(ast1),
                          float(stl2)-float(stl1),
                          float(blk2)-float(blk1),
                          (float(tov1)-float(tov2)),
                          float(pts2) - float(pts1)]],
                        columns=['FG%', 'FT%', '3P', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PTS']).style.applymap(
        _color_red_or_green).format("{:.2f}")

def get_dif_comp(df1, df2):
    fg1, fg2 = df1.iloc[0]['FG%'], df2.iloc[0]['FG%']
    ft1, ft2 = df1.iloc[0]['FT%'], df2.iloc[0]['FT%']
    three1, three2 = df1.iloc[0]['3P'], df2.iloc[0]['3P']
    reb1, reb2 = df1.iloc[0]['TRB'], df2.iloc[0]['TRB']
    ast1, ast2 = df1.iloc[0]['AST'], df2.iloc[0]['AST']
    stl1, stl2 = df1.iloc[0]['STL'], df2.iloc[0]['STL']
    blk1, blk2 = df1.iloc[0]['BLK'], df2.iloc[0]['BLK']
    tov1, tov2 = df1.iloc[0]['TOV'], df2.iloc[0]['TOV']
    pts1, pts2 = df1.iloc[0]['PTS'], df2.iloc[0]['PTS']
    return pd.DataFrame([[float(fg2) - float(fg1),
                          float(ft2) - float(ft1),
                          float(three2)-float(three1),
                          float(reb2)-float(reb1),
                          float(ast2)-float(ast1),
                          float(stl2)-float(stl1),
                          float(blk2)-float(blk1),
                          (float(tov1)-float(tov2)),
                          float(pts2) - float(pts1)]],
                        columns=['FG%', 'FT%', '3P', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PTS']).style.applymap(
        _color_red_or_green).format("{:.2f}")


def index_fix(df):
    df.index = range(1,len(df)+1)
    return df