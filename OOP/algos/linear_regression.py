"""
Linear Regression from scratch
@belovm96
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Dataloader:
    def __init__(self, path):
        self.data = pd.read_csv(path)
        self.length = len(self.data)
        self.drop_address()
        self.features, self.label = self.get_feature_label()
        self.normalize()
        self.bias()
        
    def drop_address(self):
        self.data = self.data.drop(columns='Address')
        
    def get_feature_label(self):
        columns = [column for column in self.data.columns if column != 'Price']
        return self.data[columns], self.data[['Price']]
    
    def normalize(self):
        self.min = self.features.min()
        self.max = self.features.max()
        self.features = (self.features - self.min) / (self.max - self.min)
        self.data[self.features.columns] = self.features
        
        self.min = self.label.min()
        self.max = self.label.max()
        self.label = (self.label - self.min) / (self.max - self.min)
        self.data['Price'] = self.label
    
    def train_val_split(self, p):
        self.train_num = int(self.length * p)
        self.val_num = self.length - self.train_num
        return self.data.iloc[:self.train_num], self.data.iloc[self.train_num:]
    
    def bias(self):
        self.data['Bias'] = 1
        self.features['Bias'] = 1
        
        
class LinearRegression:
    def __init__(self, path='./USA_Housing.csv', step=0.1, n_iter=100):
        self.dataloader = Dataloader(path)
        self.train, self.val = self.dataloader.train_val_split(0.8)
        
        self.X = self.train[self.dataloader.features.columns].values
        self.y = self.train[self.dataloader.label.columns].values
        
        self.X_val = self.val[self.dataloader.features.columns].values
        self.y_val = self.val[self.dataloader.label.columns].values
        
        self.coeffs = np.zeros((self.X.shape[1], 1))
        self.n_samples = self.X.shape[0]
        self.step = step
        self.n_iter = n_iter
        self.MSE = []
        
    def fit(self):
        for i in range(self.n_iter):
            self.coeffs = self.coeffs - (self.step/self.n_samples) * self.X.T @ (self.X @ self.coeffs - self.y)
            self.MSE.append(self.get_mse())
        return self.coeffs
    
    def get_mse(self):
        preds = self.X @ self.coeffs
        return (1/(self.n_samples)) * np.sum((preds - self.y)**2)
    
    def mse(self):
        return self.MSE[-1]
    
    def plot_mse(self):
        plt.plot([i for i in range(1, self.n_iter + 1)], self.MSE)
        plt.xlabel('Iteration')
        plt.ylabel('MSE')
        plt.show()
        
lr = LinearRegression()
lr.fit()
print('MSE:', lr.mse())
lr.plot_mse()