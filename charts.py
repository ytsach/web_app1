from new_rate import rater
import altair as alt
from get_player_stat import get_statistic
import pandas as pd
import utils


def get_player_df(player_name):
    return [rater(player_name=player_name, data=get_statistic()[2])[0],
            rater(player_name=player_name, data=get_statistic('60')[2])[0],
            rater(player_name=player_name, data=get_statistic('30')[2])[0],
            rater(player_name=player_name, data=get_statistic('14')[2])[0],
            rater(player_name=player_name, data=get_statistic('7')[2])][0]


def get_chart_player(team_one_name, team_two_name, team=False):
    if team:
        team_one = []
        team_two = []
        for player in team_one_name:
            team_one.append(get_player_df(player))
        for player in team_two_name:
            team_two.append(get_player_df(player))
        data_graph_team_one = utils.combine_lists(team_one)
        data_graph_player_two = utils.combine_lists(team_two)
        team_one_name = str(team_one_name).strip('[]')
        team_two_name = str(team_two_name).strip('[]')
    else:

        data_graph_team_one = get_player_df(team_one_name)
        data_graph_player_two = get_player_df(team_two_name)

    df_chart = pd.DataFrame(
        {
            'Days': [120, 60, 30, 14, 7],
            team_one_name: data_graph_team_one,
            team_two_name: data_graph_player_two
        },
        columns=['Days', team_one_name, team_two_name]
    )

    df_chart = df_chart.melt('Days', var_name='name', value_name='value')
    chart = alt.Chart(df_chart).mark_line().encode(
        x=alt.X(field='Days', type='nominal', sort='x'),
        y=alt.Y('value:Q'),
        color=alt.Color("name:N")
    ).properties(title="Stat Chart")
    return chart
