from Result import Result

class TeamBase:
    points = 0
    played = 0
    wins = 0
    drawns = 0
    lost = 0
    goal_difference  = 0
    goals_for = 0
    goals_against = 0

class Team(TeamBase):
    def __init__(self,name:str,p_played:int,p_wins:int,
    p_drawns:int,p_lost:int,p_goals_for:int,p_goals_against:int,p_goal_difference:int,p_points:int):
        self.name = name
        self.p_points = p_points
        self.p_played = p_played
        self.p_wins = p_wins
        self.p_drawns = p_drawns
        self.p_lost = p_lost
        self.p_goal_difference = p_goal_difference
        self.p_goals_for = p_goals_for
        self.p_goals_against = p_goals_against
        self.gf_avg = 0
        self.ga_avg = 0
        self.synthetic_gf_data = []
        self.synthetic_ga_data = []
        self.season = 1
        self.week = 1

    def calculateRatio(self):
        self.gf_avg = self.p_goals_for / self.p_played
        self.ga_avg = self.p_goals_against / self.p_played
        return self.gf_avg, self.ga_avg

    def SetSyntheticData(self,data_gf,data_ga):
        self.synthetic_gf_data = data_gf
        self.synthetic_ga_data = data_ga

    def WeekUpdate(self,result:Result,goals_for:int,goals_against:int):
        if(result == Result.WON):
            self.points += 3
            self.wins += 1
        elif(result == Result.DRAWN):
            self.points += 1
            self.drawns += 1
        elif(result == Result.LOST):
            self.lost += 1
            #no points recieved.
        self.goals_for += goals_for
        self.goals_against = goals_against
        self.goal_difference = self.goals_for - self.goals_against
        self.played += 1

        
        
