import pandas as pd
import itertools
import numpy

data = pd.read_csv('api/data.csv')


def removeadd(st):
    return float(st[0:-2])


def preprocessing_data(data, club):
    list = ['LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
            'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
            'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB']

    midfielders = ['LCM', 'CM', 'RCM', 'LDM',
                   'CDM', 'RDM']

    defenders = ['RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB']

    attackers = ['LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
                 'LAM', 'CAM', 'RAM', 'LM', 'RM']

    for i in list:
        data[i] = data[i].apply(removeadd)

    return data


def mapping(formation):
    if formation == '4231A':
        list_positions = ['ST', 'LAM', 'RAM', 'LCM', 'CAM', 'RCM', 'LB', 'LCB', 'RCB', 'RB']
        attackers = ['ST', 'RAM', 'LAM', 'CAM']
        defenders = ['LB', 'LCB', 'RCB', 'RB']
        mid_fielders = ['LCM', 'RCM']
        amd_no = [4, 2, 4]
    elif formation == '4231D':
        list_positions = ['ST', 'LAM', 'RAM', 'LCM', 'CDM', 'RCM', 'LB', 'LCB', 'RCB', 'RB']
        attackers = ['ST', 'RAM', 'LAM']
        defenders = ['CDM', 'LB', 'LCB', 'RCB', 'RB']
        mid_fielders = ['LCM', 'RCM']
        amd_no = [3, 2, 5]
    elif formation == '433':
        list_positions = ['ST', 'RW', 'LW', 'LCM', 'CM', 'RCM', 'LB', 'LCB', 'RCB', 'RB']
        attackers = ['ST', 'RW', 'LW']
        mid_fielders = ['LCM', 'CM', 'RCM']
        defenders = ['LB', 'LCB', 'RCB', 'RB']
        amd_no = [3, 3, 4]

    return (attackers, mid_fielders, defenders, amd_no)


def position_mapping(formation):
    if formation == '4231A':
        lst = [['ST'], ['LAM', 'CAM', 'RAM'], ['LCM', 'RCM'], ['LB', 'LCB', 'RCB', 'RB']]
    if formation == '4231D':
        lst = [['ST'], ['LAM', 'CAM', 'RAM'], ['LCM', 'RCM'], ['LB', 'LCB', 'RCB', 'RB']]

    if formation == '433':
        lst = [['LW','ST', 'RW'], ['LCM', 'CM', 'RCM'], ['LB', 'LCB', 'RCB', 'RB']]

    return lst


def formations(formation):
    if formation == '4231A':
        list_positions = ['ST', 'LAM', 'RAM', 'LCM', 'CAM', 'RCM', 'LB', 'LCB', 'RCB', 'RB']
    if formation == '4231D':
        lst_positions = ['ST', 'LAM', 'CAM', 'RAM', 'LCM', 'RCM', 'LB', 'LCB', 'RCB', 'RB']

    if formation == '433':
        lst_positions = ['ST', 'LW', 'RW', 'LCM', 'CM' 'RCM', 'LB', 'LCB', 'RCB', 'RB']
    return list_positions


def combo(data, combo):
    pref_score = 0
    for i in combo:
        if i[0] == data.loc[data['Name'] == i[1], 'Position'].reset_index(drop=True)[0]:
            pref_score += 1
    return pref_score


def map_value(st):
    if st[1] == '0':
        return 0

    return float(st[1:-1])


def formplayers(position, data_filter, val):
    players = set()
    for i in position:
        players_top_players = data_filter.nlargest(val, columns=[i])['Name'].values
        players.update(players_top_players)

    player_positions = itertools.permutations(players, val)
    attack_score = 0
    team_attackers = {}

    for i in player_positions:
        score = 0
        team = []
        for j in range(len(i)):
            score += data_filter.loc[data_filter['Name'] == i[j], position[j]].values[0]

            team.append((position[j], i[j]))
        t = tuple(team)
        team_attackers[t] = score

    for t in team_attackers:
        pre_score = combo(data_filter, t)
        team_attackers[t] = (team_attackers[t], pre_score)

    best_team_attakers = [v for v in sorted(team_attackers.items(), key=lambda x: (-x[1][0], -x[1][1]))][0]

    for p in best_team_attakers:
        data_filter.drop(data_filter[data_filter['Name'] == p].index)
    return best_team_attakers


def map_position_cordinates(st, formation):
    if formation == '4231A' or '4231D':
        if st == 'ST':
            left = 237
            top = 35
        elif st == 'LAM':
            left = 120
            top = 25
        elif st == 'CAM':
            left = 35
            top = 25
        elif st == 'RAM':
            left = 35
            top = 25
        elif st == 'LCM':
            left = 176
            top = 40
        elif st == 'RCM':
            left = 35
            top = 40

        elif st == 'LB':
            left = 90
            top = 70

        elif st == 'LCB':
            left = 15
            top = 70

        elif st == 'RCB':

            left = 15
            top = 70
        elif st == 'RB':
            left = 15
            top = 70

        elif st == 'GK':

            left = 237
            top = 20
        elif st == 'CDM':
            left = 35
            top = 25
        elif st == 'GK':
            left = 237
            top = 15
    if formation == '433':
        if st == 'LW':
            left = 120
            top = 85
        elif st == 'ST':
            left = 35
            top = 85
        elif st == 'RW':
            left = 35
            top = 85
        elif st == 'LCM':
            left = 120
            top = 85
        elif st == 'CM':
            left = 35
            top = 85
        elif st == 'RCM':
            left = 35
            top = 85
        elif st == 'LB':
            left = 90
            top = 85
        elif st == 'LCB':
            left = 15
            top = 85
        elif st == 'RB':
            left = 15
            top = 85
        elif st == 'RCB':
            left = 15
            top = 85
        elif st == 'GK':
            left = 237
            top = 15

    return (left, top)


def build_team(data, formation, club=None):
    data1 = data
    list = []
    if club != None:
        data1 = data.loc[data['Club'] == club]

    data1 = data1.filter(items=['LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
                                'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
                                'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB', 'Position', 'Overall', 'Name',
                                'Club', 'Nationality', 'Photo'])
    goal_keeper = tuple(
        data1.loc[data1['Position'] == 'GK'].nlargest(1, columns='Overall')[['Name', 'Overall']].values[0])
    lst = []
    df = data1.loc[data1['Name'] == goal_keeper[0]]
    df = df.fillna(0)
    d1 = {}
    d1['Position'] = 'GK'
    d1['Name'] = goal_keeper[0]
    (left, top) = map_position_cordinates('GK', formation)
    d1['left'] = left
    d1['top'] = top
    for column in df.columns[4:]:
        d1[column] = df[column].iloc[0]
    data1 = data1.dropna(subset=['LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
                                 'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
                                 'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB'])

    data_filter = preprocessing_data(data1, club)

    if len(data_filter) < 10:
        return None
    team_score = 0
    (attackers, mid_fielders, defenders, amd_no) = mapping(formation)

    players = set()

    team_attackers = formplayers(attackers, data_filter, amd_no[0])
    data_player = data_filter.loc[data_filter['Name'] == team_attackers[0][0][1]]
    data_filter = data_filter.drop(data_filter[data_filter['Name'] == team_attackers[0][0][1]].index)
    for p in team_attackers[0][1:]:
        data_player = data_player.append(data_filter.loc[data_filter['Name'] == p[1]])

        data_filter = data_filter.drop(data_filter[data_filter['Name'] == p[1]].index)

    team_midfielders = formplayers(mid_fielders, data_filter, amd_no[1])
    for p in team_midfielders[0]:
        df = data_filter.loc[data_filter['Name'] == p[1]]

        data_player = data_player.append(df, ignore_index=True)
        data_filter = data_filter.drop(data_filter[data_filter['Name'] == p[1]].index)
    team_defenders = formplayers(defenders, data_filter, amd_no[2])
    for p in team_defenders[0]:
        df = data_filter.loc[data_filter['Name'] == p[1]]

        df = data_filter.loc[data_filter['Name'] == p[1]]
        data_player = data_player.append(df, ignore_index=True)
        data_filter = data_filter.drop(data_filter[data_filter['Name'] == p[1]].index)
    team = dict(team_attackers[0] + team_midfielders[0] + team_defenders[0])

    team_score = team_attackers[1][0] + team_defenders[1][0] + team_midfielders[1][0] + goal_keeper[1]
    position_placement = position_mapping(formation)


    data_player = data_player.drop(['Position'], axis=1)
    for i in position_placement:
        list_i = []
        for j in i:
            d = {}
            d['Position'] = j
            d['Name'] = team[j]
            (left, top) = map_position_cordinates(j, formation)
            d['left'] = left
            d['top'] = top

            df = data_player.loc[data_player['Name'] == team[j]]

            for column in df.columns[4:]:
                d[column] = df[column].iloc[0]

            list_i.append(d)


        lst.append(list_i)
    lst.append([d1])
    return {"name":lst, "score":team_score}


team, team_score = build_team(data, '433', 'FC Barcelona')
# print(team)


def subsitute_player(data, team, player):
    club = team[0][0]['Club']
    fixed_players = []
    for i in team:
        for j in i:
            fixed_players.append(j['Name'])

    data_filter = data.loc[data['Club'] == club]

    fixed_players.remove(player)
    data_filter = data_filter.drop(data_filter[data_filter['Name'] == player].index)
    #
    data_fixed_players = data_filter[data_filter['Name'] == fixed_players[0]]
    data_filter = data_filter.drop(data_filter[data_filter['Name'] == fixed_players[0]].index)
    #
    #
    for i in fixed_players[1:]:
        df2 = data_filter[data_filter['Name'] == i]
        data_fixed_players = data_fixed_players.append(df2, ignore_index=True)
        data_filter = data_filter.drop(data_filter[data_filter['Name'] == i].index)
    #
    #
    #
    score = 0
    best_team = []

    for index, row in data_filter.iterrows():

        new_data = data_fixed_players.append(row, ignore_index=True)

        ret = build_team(new_data, '4231A', club)
        if ret == None:
            continue
        else:
            (team, team_score) = ret

            if team_score > score:
                score = team_score
                best_team = team

    return score, best_team


# print(subsitute_player(data,team,'Coutinho'))





def budget_build(data, budget, formation):
    data1 = data

    list = ['ID', 'Name', 'LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
            'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
            'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB', 'Position', 'Value']
    data_filter = data1.loc[:, data1.columns.isin(list)]

    data_filter = data_filter.dropna()

    list = ['LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
            'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
            'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB']

    for i in list:
        data_filter[i] = data_filter[i].apply(removeadd)

    data_filter = data_filter.dropna()

    positions = formations(formation)
    print(positions)
    data_filter['Value'] = data_filter['Value'].apply(map_value)
    team = []

    while len(positions) != 0 and budget >= 0:
        team_positions = {}
        val = budget / len(positions)
        for i in positions:
            rows = data_filter.loc[(data_filter['Value'] <= val) & (data_filter['Value'] > 0)]

            serie = rows.loc[rows[i].idxmin()][['Name', 'Value']]

            team_positions[i] = (serie['Name'], serie['Value'])
        print('hi')
        value = ([(v[0], v[1][0], v[1][1]) for v in sorted(team_positions.items(), key=lambda x: x[1][1])][0])
        print(value[0])
        team.append([value[0], value[1], value[2]])
        budget = budget - value[2]
        print(budget)
        positions.remove(value[0])
        data_filter = data_filter.drop(data_filter[data_filter['Name'] == value[1]].index)

    return team
    # print(budget_build(data,200,'4231A'))