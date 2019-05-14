import pandas as pd
import numpy as np
from scipy import spatial

class Similarity(object):
    def __init__(self, simidf):
        self.df = simidf
        self.use_df = None
        self.res_col = []
        self.res_col_value = []
        self.similarity_value = []
        self.simi_result_id = []
        self.resultDF = None
        self.data = pd.read_csv("../input/use_this_dataset.csv")

    def setInput(self, inputs):
        for i in inputs:
            self.res_col.append(i['name'])
            self.res_col_value.append(i['value'])
    
    def getResCol(self):
        return self.res_col

    def getResValue(self):
        return self.res_col_value

    def compute_similarity(self, col, value):
        input_value = value 
        res_to_compute = []
        for i in col:
            tmp = []
            for index, row in self.data.iterrows():
                tmp.append(row[i])
            res_to_compute.append(tmp)

        # Remove the plus character
        for n,i in enumerate(res_to_compute):
            for m,j in enumerate(i):
                tmp = str(j)[0:2]
                if tmp == 'na':
                    res_to_compute[n][m] = 0.0
                else:
                    res_to_compute[n][m] = float(tmp)
        res_to_compute = np.array(res_to_compute).T
        input_value = np.array(input_value)
        res_to_compute = res_to_compute.astype(np.float)
        
        # Note that spatial.distance.cosine computes the distance
        # ,and not the similarity. So, you must subtract the value 
        # from 1 to get the similarity.
        
        for i in res_to_compute:
            result = 1 - spatial.distance.cosine(input_value, i)
            self.similarity_value.append(result)

        self.resultDF = self.data
        self.resultDF['Similarity'] = np.array((self.similarity_value)).T
        self.resultDF = self.resultDF[pd.notnull(self.resultDF['Similarity'])]
        self.resultDF = self.resultDF.sort_values(by=['Similarity'], ascending=False)
        self.resultDF = self.resultDF.fillna(0)
    
    def getSimilarityValue(self):
        return self.similarity_value

    def getResultDataframe(self):
        return self.resultDF

    def getResultID(self):
        self.simi_result_id = self.getResultDataframe()['ID'].tolist()
        return self.simi_result_id
        
