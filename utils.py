import pandas as pd
from rating import get_rating_statistic


def get_relevant_data_compare(dataf):
    df = pd.DataFrame(dataf)
    return df.drop(columns=['Player','Pos','Age','Tm','PF'])

def get_player_rating(player):
    player_data = get_rating_statistic(player)
    #rating formula is PER
    per = float(player_data.iloc[0]['PER'])
    g = float(player_data.iloc[0]['G'])
    mp = float(player_data.iloc[0]['MP'])
    return str(int((per*mp)/g))


