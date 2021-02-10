from get_player_stat import get_statistic
import pandas as pd
import streamlit as st


# def check_if_empty(dataf):
#     if dataf.empty

@st.cache(suppress_st_warning=True)
def rater(player_name=None, data=None):
    # data = get_statistic()[2]
    player_data = data.loc[data['Player'].str.contains(player_name)]
    if player_data.empty:
        to_chart = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        return 0, to_chart
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
    # formula = ((
    #             fgm * 0.477 + stl * 9.2 + threes * 4.48 + ftm * 0.22 + blk * 12.2 + reb * 2.7 + ast * 4.48 + pts * 1 - ftmiss * 0.78 - fgmiss * 0.533 - to * 6.3))
    formula = ((
            fgm * 10.2 + stl * 14.2 + threes * 13.48 + ftm * 6.02 + blk * 16.2 + reb * 3.7 + ast * 6.48 + pts * 1.12 - ftmiss * 8.8 - fgmiss * 8.6 - to * 8.3))

    to_chart = fgm, -fgmiss, ftm, -ftmiss, threes, reb, ast, stl, blk, -to, pts
    # return "{:.1f}".format(formula)
    return float(round(formula, 2)), to_chart

# if __name__ == "__main__":
#     print(rater(player_name='Bradley Beal'))
#     pass
