import pandas as pd

matches = pd.read_json('grupoALibertadores2018.json')

grupoA = pd.DataFrame()
grupoA['teams'] = matches['local'].unique()
grupoA['points'] = 0


def points(x):
    if x['result'] == 'local_won':
        grupoA.loc[grupoA['teams'] == x['local'], 'points'] += 3
    elif x['result'] == 'draw':
        grupoA.loc[grupoA['teams'] == x['local'], 'points'] += 1
        grupoA.loc[grupoA['teams'] == x['visitor'], 'points'] += 1
    else:
        grupoA.loc[grupoA['teams'] == x['visitor'], 'points'] += 3


matches.apply(lambda row: points(row), axis=1)
print(grupoA.sort_values(by=['points'], ascending=False))
