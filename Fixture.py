import functools
import operator


def fixtures(teams):
    if len(teams) % 2:
        teams.append('Day off')  # if team number is odd - use 'day off' as fake team     

    rotation = list(teams)       # copy the list

    fixtures = []
    for i in range(0, len(teams)-1):
        fixtures.append(rotation)
        rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]

    return fixtures


def GetPremierFixture(teams):
    matches = fixtures(teams)
    fixtureAll = []
    for f in matches:    
        fixtureAll.append(zip(*[iter(f)]*2))
        # print(tuple(zip(*[iter(f)]*2)))

    reverse_teams =  [list(x) for x in zip(teams[1::2], teams[::2])]
    reverse_teams = functools.reduce(operator.add,  reverse_teams)    # swap team1 with team2, and so on ....

    matches = fixtures(reverse_teams)

    # print ("return matches")
    for f in matches:    
        fixtureAll.append(zip(*[iter(f)]*2))
        # print (tuple(zip(*[iter(f)]*2)))

    return fixtureAll



