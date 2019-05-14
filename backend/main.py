import pandas as pd
import numpy as np
import similarity

class Compute(object):
    def __init__(self, sim_arr):
        self.simdf = pd.read_csv("../input/compute_similarity.csv")
        self.sim_arr = sim_arr
        self.data_from_sim = similarity.Similarity(self.simdf)
    
    def getResult(self):
        self.data_from_sim.setInput(self.sim_arr)
        self.data_from_sim.compute_similarity(self.data_from_sim.getResCol(), self.data_from_sim.getResValue())
        return self.data_from_sim.getResultDataframe()