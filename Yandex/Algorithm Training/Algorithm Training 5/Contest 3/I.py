from collections import defaultdict
from io import TextIOWrapper

TOTAL_TEAM_GOAL = 0
MEAN_TEAM_GOAL = 1
TOTAL_PLAYER_GOAL = 2
MEAN_PLAYER_GOAL = 3
PLAYER_GOAL_ON_MIN = 4
PLAYER_GOAL_BEFORE_MIN = 5
PLAYER_GOAL_AFTER_MIN = 6
TEAM_OPENS = 7
PLAYER_OPENS = 8
STATISTIC = 9

def get_statistic(fin: TextIOWrapper, teams: defaultdict, players: defaultdict, info):
    team1, team2, team1_goals, team2_goals = info

    teams[team1][0] += 1
    teams[team2][0] += 1
    teams[team1][1] += team1_goals
    teams[team2][1] += team2_goals   

    min_minute = (91, None, None) # Минута открытия, команда, игрок
    for _ in range(team1_goals):
        *player, minute = fin.readline().split()
        player = ' '.join(player)
        minute = int(minute[:-1])

        players[player][0] = team1
        players[player][2][minute] += 1

        if minute < min_minute[0]:
            min_minute = (minute, team1, player)

    for _ in range(team2_goals):
        *player, minute = fin.readline().split()
        player = ' '.join(player)
        minute = int(minute[:-1])

        players[player][0] = team2
        players[player][2][minute] += 1

        if minute < min_minute[0]:
            min_minute = (minute, team2, player)
       
    if min_minute[0] != 91:
        teams[min_minute[1]][2] += 1
        players[min_minute[2]][1] += 1

def parse_query(query: str, teams: defaultdict, players: defaultdict):
    query_list = query.split()

    if query_list[0] == 'Total':
        if query_list[2] == 'for':
            return TOTAL_TEAM_GOAL, ' '.join(query_list[3:])
        else:
            return TOTAL_PLAYER_GOAL, ' '.join(query_list[3:])
    elif query_list[0] == 'Mean':
        if query_list[4] == 'for':
            return MEAN_TEAM_GOAL, ' '.join(query_list[5:])
        else:
            return MEAN_PLAYER_GOAL, ' '.join(query_list[5:])
    elif query_list[0] == 'Goals':
        if query_list[2] == 'minute':
            return PLAYER_GOAL_ON_MIN, int(query_list[3]), ' '.join(query_list[5:])
        elif query_list[2] == 'first':
            return PLAYER_GOAL_BEFORE_MIN, int(query_list[3]), ' '.join(query_list[6:])
        else:
            return PLAYER_GOAL_AFTER_MIN, int(query_list[3]), ' '.join(query_list[6:])
    elif query_list[0] == 'Score':       
        if ' '.join(query_list[3:]) in teams:            
            return TEAM_OPENS, ' '.join(query_list[3:])
        else:
            return PLAYER_OPENS, ' '.join(query_list[3:])
    else:
        team1 = []
        team2 = []

        for i in range(len(query_list)-2):
            if query_list[i] != '-':
                team1.append(query_list[i])
            else:
                break

        for j in range(i+1, len(query_list)-1):
            team2.append(query_list[j])

        team1 = ' '.join(team1)
        team2 = ' '.join(team2)   

        return STATISTIC, team1, team2, *[int(x) for x in query_list[-1].split(':')]
    
def get_total_players_goals(players, player):
    goals = players[player][2]

    count = 0
    for i in range(1, 91):
        count += goals[i]

    return count

def get_first_goals_by_player(players, player, minute):
    goals = players[player][2]

    count = 0
    for i in range(1, minute+1):
        count += goals[i]

    return count

def get_last_goals_by_player(players, player, minute):
    goals = players[player][2]

    count = 0
    for i in range(91-minute, 91):
        count += goals[i]

    return count    

def main():
    with open('input.txt') as fin:
        teams = defaultdict(lambda: [0, 0, 0]) # Кол-во матчей, кол-во голов, кол-во открытий
        players = defaultdict(lambda: [None, 0, [0]*91]) # Команда, кол-во открытий, минуты голов

        for query in fin:
            query_type, *info = parse_query(query, teams, players)           

            if query_type == STATISTIC:
                get_statistic(fin, teams, players, info)
            elif query_type == TOTAL_TEAM_GOAL:
                print(teams[info[0]][1])
            elif query_type == MEAN_TEAM_GOAL:
                print(f'{teams[info[0]][1]/teams[info[0]][0]:.3f}')
            elif query_type == TOTAL_PLAYER_GOAL:
                print(get_total_players_goals(players, info[0]))
            elif query_type == MEAN_PLAYER_GOAL:
                print(f'{get_total_players_goals(players, info[0])/teams[players[info[0]][0]][0]:.3f}')
            elif query_type == PLAYER_GOAL_ON_MIN:
                print(players[info[1]][2][info[0]])
            elif query_type == PLAYER_GOAL_BEFORE_MIN:
                print(get_first_goals_by_player(players, info[1], info[0]))
            elif query_type == PLAYER_GOAL_AFTER_MIN:
                print(get_last_goals_by_player(players, info[1], info[0]))
            elif query_type == TEAM_OPENS:
                print(teams[info[0]][2])
            elif query_type == PLAYER_OPENS:
                print(players[info[0]][1])


if __name__ == '__main__':
    main()