import numpy as np


class SyntheticData():
    def __init__(self,gf_avg,ga_avg,gd,num_reps):
        self.gf_avg = gf_avg
        self.ga_avg = ga_avg
        self.gd = gd
        self.num_reps = num_reps
        
    
    def generateData(self):
        gf_data = np.random.normal(self.gf_avg, np.abs(self.gd)/100, self.num_reps).round(2)
        ga_data = np.random.normal(self.ga_avg, (100-np.abs(self.gd))/100, self.num_reps).round(2)
        #replacing negative values with average values to avoid calculation errors.
        #there is no such thing as a negative probability.
        gf_data = np.where(gf_data<0, np.average(gf_data), gf_data)
        ga_data = np.where(ga_data<0, np.average(gf_data), ga_data)
        return gf_data, ga_data

