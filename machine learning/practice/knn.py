"""
KNN from scratch

@belovm96
"""
import pandas as pd

def loadData():
    data = pd.read_csv('iris.csv')
    data.columns = ['seplen', 'sepwid', 'petlen', 'petwid', 'label']
    return data        

class KNN:
    def __init__(self, data, k):
        self.data = data.sample(frac=1)
        self.features = self.data[['seplen',  'sepwid',  'petlen',  'petwid']]
        self.k = int(k)
        
    def scale(self):
        self.min = self.features.min()
        self.max = self.features.max()
        self.data[['seplen',  'sepwid',  'petlen',  'petwid']] = (self.features - self.min) / (self.max - self.min)
    
    def predict(self, data, point):
        d = data[['seplen',  'sepwid',  'petlen',  'petwid']].values
        p = point[['seplen',  'sepwid',  'petlen',  'petwid']].values
        distances = (d - p)**2
        distances = distances.sum(axis=1)
        k_largest = distances.argsort()[:self.k]
        labels = data[['label']].values[k_largest].flatten()
        return max(set(labels), key = list(labels).count)
    
    def split_k_fold(self, K):
        self.K = K
        self.k_splits = {}
        step = self.features.values.shape[0] // K
        for i in range(0, self.data.values.shape[0], step):
            self.k_splits[i] = (self.data.index[i:i+step], list(self.data.index[:i])+list(self.data.index[i+step:]))
            
    def evaluate(self):
        print(f'\nPerforming {self.K}-cross validation')
        acc = []
        for k in self.k_splits:
            correct = 0
            test = self.k_splits[k][0]
            train = self.k_splits[k][1]
            train = self.data.iloc[train]
            for ind in test:
                point = self.data.iloc[ind]
                pred = self.predict(train, point)
                if int(pred) == int(point[['label']].values):
                    correct += 1       
                    
            acc.append(correct/len(test))
            
        print('\nAccuracy for each fold:\n', acc)
        
        return acc
        
data = loadData()
k = input('Please provide k: ')
knn = KNN(data, k)
knn.scale()
knn.split_k_fold(5)
knn.evaluate()
