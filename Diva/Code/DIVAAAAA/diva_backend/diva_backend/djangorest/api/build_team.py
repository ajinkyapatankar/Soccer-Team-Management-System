import pandas as pd
import itertools
import numpy

data = pd.read_csv('api/data.csv')


def removeadd(st):
    return float(st[0:-2])


def preprocessing_data(data):
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
    elif formation == '442':
        list_positions = ['LS', 'RS', 'CAM', 'LCM', 'RCM', 'CDM', 'LB', 'LCB', 'RCB', 'RB']
        attackers = ['LS', 'RS', 'CAM']
        mid_fielders = ['LCM', 'RCM', 'CDM']
        defenders = ['LB', 'LCB', 'RCB', 'RB']
        amd_no = [3, 3, 4]

    elif formation == '352':
        list_positions = ['LS', 'RS', 'CAM', 'LDM', 'RDM', 'LWB', 'LCB', 'CB', 'RCB', 'RWB']
        attackers = ['LS', 'RS', 'CAM']
        mid_fielders = ['LDM', 'RDM']
        defenders = ['LWB', 'LCB', 'CB', 'RCB', 'RWB']
        amd_no = [3, 2, 5]
    return (attackers, mid_fielders, defenders, amd_no)


def position_mapping(formation):
    if formation == '4231A':
        lst = [['ST'], ['LAM', 'CAM', 'RAM'], ['LCM', 'RCM'], ['LB', 'LCB', 'RCB', 'RB']]
    if formation == '4231D':
        lst = [['ST'], ['LAM', 'CAM', 'RAM'], ['LCM', 'RCM'], ['LB', 'LCB', 'RCB', 'RB']]

    if formation == '433':
        lst = [['LW','ST', 'RW'], ['LCM', 'CM', 'RCM'], ['LB', 'LCB', 'RCB', 'RB']]

    if formation == '442':
        lst = [['LS', 'RS'], ['CAM'], ['LCM', 'RCM'], ['CDM'], ['LB', 'LCB', 'RCB', 'RB']]
    if formation == '352':
        lst = [['LS', 'RS'], ['LWB', 'CAM', 'RWB'], ['LDM', 'RDM'], ['LCB', 'CB', 'RCB']]

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
        df=data.loc[data['Name'] == i[1]].reset_index(drop=True)[["Position", i[0]]]
        pref_pos=df["Position"][0]
        score=df[i[0]][0]

        if i[0] == pref_pos[0]:
            pref_score += 1
        elif i[0][0] == pref_pos[0][0]:
            pref_score += 1*score/100


    return pref_score


def map_value(st):
    if st[1] == '0':
        return 0

    return float(st[1:-1])

def players_list(team):
    lst=[]
    team_players=team
    for i in team_players:
        for j in i:
            lst.append(j['Name'])
    return lst


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

def formplayers2(position, data_filter, val):
    players = set()
    score=0
    team_attackers=[]
    best={}
    for i in position:
        players_top_players = data_filter.nlargest(1, columns=[i])['Name'].values[0]
        score += data_filter.loc[data_filter['Name'] == players_top_players, i].values[0]
        data_filter=data_filter.drop(data_filter[data_filter['Name'] == players_top_players].index)
        team_attackers.append((i,players_top_players))
        # players.update(players_top_players)

    best[tuple(team_attackers)]=(score,0)
    best_team_attakers = [v for v in sorted(best.items(), key=lambda x: (-x[1][0], -x[1][1]))][0]
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

    if formation == '442':
        if st == 'LS':
            left = 165
            top = 35
        elif st == 'RS':
            left = 60
            top = 35
        elif st == 'CAM':
            left = 237
            top = 25
        elif st == 'LCM':
            left = 150
            top = 10
        elif st == 'RCM':
            left = 80
            top = 10
        elif st == 'CDM':
            left = 237
            top = 0
        elif st == 'LB':
            left = 90
            top = 20
        elif st == 'LCB':
            left = 15
            top = 20
        elif st == 'RB':
            left = 15
            top = 20
        elif st == 'RCB':
            left = 15
            top = 20
        elif st == 'GK':
            left = 237
            top = 15
    if formation == '352':
        if st == 'LS':
            left = 165
            top = 35
        elif st == 'RS':
            left = 60
            top = 35
        elif st == 'LWB':
            left = 105
            top = 50
        elif st == 'CAM':
            left = 52
            top = 50
        elif st == 'RWB':
            left = 50
            top = 50
        elif st == 'LDM':
            left = 150
            top = 30
        elif st == 'RDM':
            left = 80
            top = 30
        elif st == 'LCB':
            left = 142
            top = 40
        elif st == 'CB':
            left = 15
            top = 40
        elif st == 'RCB':
            left = 15
            top = 40
        elif st == 'GK':
            left = 237
            top = 15

    return (left, top)


def build_team(data, formation, club=None, nation=None):
    data1 = data
    list = []
    if club != None and club!="":
        data1 = data.loc[data['Club'] == club]

    if nation != None and nation!="":
        data1 = data.loc[data['Nationality'] == nation]

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

    data_filter = preprocessing_data(data1)

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
    players = players_list(lst)

    return {"name":lst, "score":team_score,"players":players}

def build_budget_team(data, formation,budget, club=None, nation=None):
    data1 = data
    list = []
    data['value_adjusted'] = data['Value']
    for index, row in data.iterrows():
        val = data.at[index, 'Value'][1:]
        if val[-1] == 'M':
            val = float(val[0:-1]) * 1000000
        elif val[-1] == 'K':
            val = float(val[0:-1]) * 1000
        else:
            val = 0.0
        data.at[index, 'value_adjusted'] = val
    data['value_adjusted'].astype(float)
    print(type(data['value_adjusted']))
    if club != None and club!="":
        data1 = data.loc[data['Club'] == club]

    if nation != None and nation!="":
        data1 = data.loc[data['Nationality'] == nation]
    if budget!=0:
        upper_limit = 1.15 * (float(budget) / 11.0)
        data1 = data1.loc[(data1['value_adjusted'] <= upper_limit) & (data1['value_adjusted'] > 0.0)]

    data1 = data1.filter(items=['LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
                                'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
                                'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB', 'Position', 'Overall', 'Name',
                                'Club', 'Nationality', 'Photo'])

    goal_keeper = tuple(
        data1.loc[data1['Position'] == 'GK'].nlargest(1, columns='Overall')[['Name', 'Overall']].values[0])
    print(goal_keeper)
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

    data_filter = preprocessing_data(data1)

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
    players = players_list(lst)
    # print({"name":lst, "score":team_score,"players":players})
    return {"name":lst, "score":team_score,"players":players}

def greddy_team(data, formation, club=None, nation=None):
    data1 = data
    list = []
    if club != None and club!="":
        data1 = data.loc[data['Club'] == club]

    if nation != None and nation!="":
        data1 = data.loc[data['Nationality'] == nation]
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

    data_filter = preprocessing_data(data1)

    if len(data_filter) < 10:
        return None
    team_score = 0
    (attackers, mid_fielders, defenders, amd_no) = mapping(formation)

    players = set()

    team_attackers = formplayers2(attackers, data_filter, amd_no[0])
    data_player = data_filter.loc[data_filter['Name'] == team_attackers[0][0][1]]
    data_filter = data_filter.drop(data_filter[data_filter['Name'] == team_attackers[0][0][1]].index)
    for p in team_attackers[0][1:]:
        data_player = data_player.append(data_filter.loc[data_filter['Name'] == p[1]])

        data_filter = data_filter.drop(data_filter[data_filter['Name'] == p[1]].index)

    team_midfielders = formplayers2(mid_fielders, data_filter, amd_no[1])
    for p in team_midfielders[0]:
        df = data_filter.loc[data_filter['Name'] == p[1]]

        data_player = data_player.append(df, ignore_index=True)
        data_filter = data_filter.drop(data_filter[data_filter['Name'] == p[1]].index)
    team_defenders = formplayers2(defenders, data_filter, amd_no[2])
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
    players = players_list(lst)

    return {"name":lst, "score":team_score,"players":players}


# team= build_team(data, '4231A', 'Liverpool')
# print(team)


def subsitute_player(data, team,club, player,formation,nation):

    players_org = team
    fixed_players=team
    if club!= "":
        data_filter = data.loc[data['Club'] == club]
    if nation!="":
        data_filter = data.loc[data['Nationality'] == nation]
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



    for index, row in data_filter.iterrows():

        new_data = data_fixed_players.append(row, ignore_index=True)

        ret = build_team(new_data,formation, club,nation)
        if ret == None:
            continue
        else:
            (team, team_score,team_players) = (ret["name"],ret["score"],ret["players"])

            if team_score > score:
                score = team_score

                best_team = team
                best_players=team_players
                substitute = row['Name']

    for i in best_team:
        for val in i:
            if val['Name'] in players_org:
                val['sub_flag'] = 0
            elif val['Name'] not in players_org:
                val['sub_flag'] = 1

    return {"name": best_team, "score": score, "players": best_players, "substitute": substitute}



# print(subsitute_player(data,team,'Liverpool','V. van Dijk','4231A'))




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


def club_rating(club):
    lst = list(data.loc[data['Club'] == club]['Overall'].values)

    return lst
# print(club_rating('Liverpool'))

def box_plot():
    d={}
    clubs_list=['Liverpool','Manchester City','Juventus','Chelsea','Manchester United']

    d["labels"]=clubs_list
    lst=list()
    final_dict = {}
    for c in clubs_list:
        # print(c)
        l=club_rating(c)
        lst.append({'name':c,'values':l})
    # d["Overall"]=lst
    return {'type':'box','name':lst}
# print(box_plot('Liverpool','Manchester City','Juventus','Chelsea','Manchester United'))


def box_plot2():

    d={}
    clubs_list=['Liverpool','Manchester City','Juventus','Chelsea','Manchester United']

    d["labels"]=clubs_list
    lst=list()
    final_dict = {}
    for c in clubs_list:
        # print(c)
        l=club_rating(c)
        lst.append({'name':c,'values':l})
    # d["Overall"]=lst
    return {'type':'box','name':lst}

def percent_players():
    d={}
    player_data=data['Position']
    lst=[]
    position_count = player_data.value_counts()
    labels = position_count.index.tolist()
    values = position_count.values.tolist()



    # lst.append({'name':labels,'values':values})
    return {'type':'pie','name':{'name':labels,'values':values}}

def bar_plot():
    player_data = data['Nationality']
    lst = []
    position_count = player_data.value_counts()
    labels = position_count.index.tolist()
    values = position_count.values.tolist()

    lst.append({'name': labels, 'values': values})
    return {'type': 'bar', 'name': {'name': labels, 'values': values}}


def radar_plot(type):
    plt_cols = ['Crossing', 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
                'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
                'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower',
                'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
                'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
                'Marking', 'StandingTackle', 'SlidingTackle']
    forwards = ['ST', 'LF', 'RF', 'CF', 'LW', 'RW']
    midfielders = ['CM', 'LCM', 'RCM', 'RM', 'LM', 'CDM', 'LDM', 'RDM', 'CAM', 'LAM', 'RAM', 'LCM', 'RCM']
    defenders = ['CB', 'RB', 'LB', 'RCB', 'LCB', 'RWB', 'LWB']
    if type=='forwards':
        players = data[data['Position'].isin(forwards)]
    elif type=='midfielders':
        players = data[data['Position'].isin(midfielders)]
    elif type=='defenders':
        players = data[data['Position'].isin(defenders)]

    top_fwds =players.sort_values(by='Overall', ascending=False).head(10)
    lst=[]
    for index,row in top_fwds.iterrows():
        player=row['Name']
        values=[row[v] for v in plt_cols]
        lst.append({'name':player,'values':values})



    return {'type':'scatterpolar','name':lst}


