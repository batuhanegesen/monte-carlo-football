from Team import Team
import numpy as np
import DB_Operations as db


class Match:
    def __init__(self, home: Team, away: Team, week: int, season: int):
        self.home = home
        self.away = away
        self.week = week
        self.season = season
        self.winner = Team
        self.home_goal = 0
        self.away_goal = 0
        self.home_score_acq = 0
        self.away_score_acq = 0
        

    def PlayMatch(self):
        print("Playing this particular match between {} and {} in week {}, season {}"
        .format(self.home.name, self.away.name, self.week, self.season))

        ### home goals
        query = {"team": self.home.name, "season":self.season}
        obj = db.s_gf_col.find_one(query)
        s_gf = obj['value']

        query = {"team": self.away.name, "season":self.season}
        obj = db.s_ga_col.find_one(query)
        s_ga = obj['value']

        self.home_goal = np.round(s_gf * s_ga)
        print("home goals: ",self.home_goal)
        #### away goals
        query = {"team": self.away.name, "season":self.season}
        obj = db.s_gf_col.find_one(query)
        s_gf = obj['value']

        query = {"team": self.home.name, "season":self.season}
        obj = db.s_ga_col.find_one(query)
        s_ga = obj['value']

        self.away_goal = np.round(s_gf * s_ga)
        print("away goals: ",self.away_goal)

        if(self.home_goal>self.away_goal):
            self.winner = self.home
            self.home_score_acq = 3
            self.away_score_acq = 0
            print(self.winner.name)
            # print("winner is :",self.winner.name)
            # db.SaveMatchResult(self)
            #home gets 3 points for win
        elif(self.home_goal<self.away_goal):
            self.winner = self.away
            self.away_score_acq = 3
            self.home_score_acq = 0
            print(self.winner.name)
        else:
            #drawn game
            self.home_score_acq = 1
            self.away_score_acq = 1
        return self
            
        



