import pymongo as mongo
from Team import Team

myclient = mongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Premier_League"]

s_gf_col = mydb["synthetic_gf"]
s_ga_col = mydb["synthetic_ga"]
# s_gf_col = None
def SaveSyntheticData(teams:Team):
    for team in teams:
        gf_dataList = []
        ga_dataList = []
        for j in range(1,team.synthetic_gf_data.__len__()+1):
            db_data = {"team": team.name, "season": j, "value": team.synthetic_gf_data[j-1]}
            gf_dataList.append(db_data)
        s_gf_col.insert_many(gf_dataList)
        for j in range(1,team.synthetic_ga_data.__len__()+1):
            db_data = {"team": team.name, "season": j, "value": team.synthetic_ga_data[j-1]}
            ga_dataList.append(db_data)
        s_ga_col.insert_many(ga_dataList)


matchResults = mydb["match_res"]
teamData = mydb["team_data"]
leagues = mydb["leagues"]

weekly = mydb['weekly']



def SaveMatchResult(matchlist1,matchlist2):
        matchResults.insert_many(matchlist1)
        matchResults.insert_many(matchlist2)



def SaveTeamResults(teamRes):
    teamData.insert_many(teamRes)


def CreateWeeklyTable(data):
    weekly.insert_many(data)


# data = {"team": "Manchester City"}
# myDoc = s_gf_col.find(data)
# for x in myDoc:
#     print(x)
# s_gf_col.drop()


