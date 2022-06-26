from soupsieve import match
from Data import SyntheticData
import pandas as pd
import numpy as np
from Fixture import GetPremierFixture
from Result import Result
from Team import Team
from Match import Match
import DB_Operations as do


sim_size = int(input("What is the simulation size? :"))

#Reading the past season data
df = pd.read_csv('Data.csv')
lastPlayedWeek = 0

team_names, played, won, drawn, lost, gf, ga, gd, points = [
    ], [], [], [], [], [], [], [], []

for i in range(4):
    # print(df.loc[i][0])
    team_names.append(df.loc[i][0])
    played.append(df.loc[i][1])
    won.append(df.loc[i][2])
    drawn.append(df.loc[i][3])
    lost.append(df.loc[i][4])
    gf.append(df.loc[i][5])
    ga.append(df.loc[i][6])
    gd.append(df.loc[i][7])
    points.append(df.loc[i][8])

team_names = tuple(team_names)
played = tuple(played)
won = tuple(won)
drawn = tuple(drawn)
lost = tuple(lost)
gf = tuple(gf)
ga = tuple(ga)
gd = tuple(gd)
points = tuple(points)


previousData = zip(team_names, played, won, drawn, lost, gf, ga, gd, points)

previousData = tuple(previousData)

#Initializing the teams. Manually. Not an ingenious method but since it works, i'll not touch it.
Manchester_City = Team(previousData[0][0],
                       previousData[0][1],
    previousData[0][2],
    previousData[0][3],
    previousData[0][4],
    previousData[0][5],
    previousData[0][6],
    previousData[0][7],
    previousData[0][8],)

Chelsea = Team(previousData[1][0],
               previousData[1][1],
    previousData[1][2],
    previousData[1][3],
    previousData[1][4],
    previousData[1][5],
    previousData[1][6],
    previousData[1][7],
    previousData[1][8],)

Tottenham_Hotspur = Team(previousData[2][0],
                         previousData[2][1],
    previousData[2][2],
    previousData[2][3],
    previousData[2][4],
    previousData[2][5],
    previousData[2][6],
    previousData[2][7],
    previousData[2][8],)

Liverpool = Team(previousData[3][0],
                 previousData[3][1],
    previousData[3][2],
    previousData[3][3],
    previousData[3][4],
    previousData[3][5],
    previousData[3][6],
    previousData[3][7],
    previousData[3][8],)

teams = [Manchester_City, Chelsea, Tottenham_Hotspur, Liverpool]

for team in teams:
    team.calculateRatio()

ManData = SyntheticData(Manchester_City.gf_avg,
                        Manchester_City.ga_avg, Manchester_City.p_goal_difference, sim_size)
Manchester_City.SetSyntheticData(*ManData.generateData())

CheData = SyntheticData(Chelsea.gf_avg, Chelsea.ga_avg,
                        Chelsea.p_goal_difference, sim_size)
Chelsea.SetSyntheticData(*CheData.generateData())


LivData = SyntheticData(Liverpool.gf_avg, Liverpool.ga_avg,
                        Liverpool.p_goal_difference, sim_size)
Liverpool.SetSyntheticData(*LivData.generateData())

TotData = SyntheticData(Tottenham_Hotspur.gf_avg,
                        Tottenham_Hotspur.ga_avg, Tottenham_Hotspur.p_goal_difference, sim_size)
Tottenham_Hotspur.SetSyntheticData(*TotData.generateData())


fixture = GetPremierFixture(teams)

# returns a (team1,team2) match
# tuple(fixture[week])[match_number]

weeks = []
for week in fixture:
    weeks.append(tuple(week))

all_matches = []
for matches in weeks:
    all_matches.append(tuple(matches)[0])
    all_matches.append(tuple(matches)[1])


#Save the synthetic generated data to database first.
do.SaveSyntheticData(teams)




# print("Home Team:",home,", Away Team:", away)
def playWeek(week:int,simulations:int):
    home1, away1 = weeks[week-1][0]
    home2, away2 = weeks[week-1][1]
    match1_dbs = []
    match2_dbs = []
    team_scores = []
    for season in range(1,simulations):
        match1 = Match(home1,away1,week,season)
        match1 = match1.PlayMatch()
        match1_db = {"season": match1.season, "week": match1.week,"home":match1.home.name,"away": match1.away.name,"home_goals":
        match1.home_goal,"away_goal": match1.away_goal,"home_score_acq": match1.home_score_acq,"away_score_acq": match1.away_score_acq}
        match1_dbs.append(match1_db)
        # print(match.home_goal)
        match2 = Match(home2,away2,week,season)
        match2 = match2.PlayMatch()
        match2_db = {"season": match2.season, "week": match2.week,"home":match2.home.name,"away": match2.away.name,"home_goals":
        match2.home_goal,"away_goal": match2.away_goal,"home_score_acq": match2.home_score_acq,"away_score_acq": match2.away_score_acq}
        match2_dbs.append(match2_db)
        # print(match2.home_goal)


        # I CREATE THE TEAM WEEKLY POINTS GAIN DATA --- NOT CUMULATIVE SUM OF POINTS
        team_data = {"season":match1.season ,"week": match1.week, "team": match1.home.name,"points": match1.home_score_acq}
        team_scores.append(team_data)
        team_data = {"season":match1.season ,"week": match1.week, "team": match1.away.name,"points": match1.away_score_acq}
        team_scores.append(team_data)
        team_data = {"season":match2.season ,"week": match2.week, "team": match2.home.name,"points": match2.home_score_acq}
        team_scores.append(team_data)
        team_data = {"season":match2.season ,"week": match2.week, "team": match2.away.name,"points": match2.away_score_acq}
        team_scores.append(team_data)

    do.SaveTeamResults(team_scores)
    do.SaveMatchResult(match1_dbs,match2_dbs)

    if(do.teamData.find_one({"week":season})):
        query= {"season": match1.season, "week": match1.week}
        teams = []
        for x in do.teamData.find(query):
            print(x['team'])
            data = {"team": x['team'],"points": x['points']}
            teams.append(data)
        week_data = {"season":match1.season ,
        "week": match1.season,
        "teams":teams}
        print(week_data)
        # do.CreateWeeklyTable(week_data)
            
            
    

    # print(do.matchResults.find_one({"home":"Tottenham Hotspur"}))






def AllPlayLeague(sim_size):
    for week in range(1,7):
        playWeek(week,sim_size)


# playWeek(1,sim_size)
# AllPlayLeague(sim_size)

while(lastPlayedWeek<6):
    print("Play for week ",lastPlayedWeek+1)
    input("Waiting 'enter' to play")
    playWeek(lastPlayedWeek+1,sim_size)
    lastPlayedWeek +=1
    # for x in do.teamData.find({"team":"Tottenham Hotspur"}):
    #     print(x)


# query= {"team": "Tottenham Hotspur", "week": 1}
# query= {"season": 1, "week": 1}
# for x in do.teamData.find(query):
#     print(x)








print("End of the Simulation")



def dropTable():
    do.s_gf_col.drop()
    do.s_ga_col.drop()
    do.matchResults.drop()
    do.teamData.drop()


dropTable()
