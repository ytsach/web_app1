from get_player_stat import get_statistic
import pandas as pd
import streamlit as st


# def check_if_empty(dataf):
#     if dataf.empty


def rater(player_name=None, data=None):
    # data = get_statistic()[2]
    player_data = data.loc[data['Player'].str.contains(player_name)]
    if player_data.empty:
        return 0
    fgm = float(player_data.iloc[0]['FG'])

    stl = float(player_data.iloc[0]['STL'])
    threes = float(player_data.iloc[0]['3P'])
    ftm = float(player_data.iloc[0]['FT'])
    blk = float(player_data.iloc[0]['BLK'])
    reb = float(player_data.iloc[0]['TRB'])
    ast = float(player_data.iloc[0]['AST'])
    ftmiss = float(player_data.iloc[0]['FTA']) - ftm
    fgmiss = float(player_data.iloc[0]['FGA']) - fgm
    to = float(player_data.iloc[0]['TOV'])
    # min = pd.to_numeric(player_data.iloc[0]['MP'])
    pts = float(player_data.iloc[0]['PTS'])
    # g = pd.to_numeric(player_data.iloc[0]['G'])

    # formula = ((fgm * 55.91 + stl * 65.89 + threes * 65.757 + ftm * 46.845 + blk * 70.19 + reb * 45.67 + ast * 50 + pts * 57 - ftmiss * 50.091 - fgmiss * 65.19 - to * 53.897) * 1 / min) * g
    formula = ((
                fgm * 58.91 + stl * 70.89 + threes * 61.757 + ftm * 50.845 + blk * 75.19 + reb * 45.67 + ast * 50 + pts * 45 - ftmiss * 70.091 - fgmiss * 65.19 - to * 65.897))
    return "{:.1f}".format(formula)

# if __name__ == "__main__":
#     print(rater(player_name='Bradley Beal'))
#     pass
