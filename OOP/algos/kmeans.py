"""
K-means from scratch
@belovm96
"""

import numpy as np
from matplotlib import pyplot as plt
import matplotlib

class KMeans:
    def __init__(self, data):
        self.data = data
    def initialize(self, k):
        self.k = k
        c_idx = np.random.randint(self.data.shape[0], size=k)
        self.centroids = {tuple(data):[] for data in self.data[c_idx, :]}
        
    def fit(self):
        while True:
            for p in self.data:
                min_d = float('inf')
                for c in self.centroids:
                    if np.linalg.norm(p-np.array(c)) < min_d:
                        min_d = np.linalg.norm(p-np.array(c))
                        min_c = c
                self.centroids[min_c].append(p)
            
            self.new_centroids = {}
            for c in self.centroids:
                mean = np.mean(self.centroids[c], axis=0)
                self.new_centroids[tuple(mean)] = []
            
            if self.new_centroids.keys() != self.centroids.keys():
                self.centroids = self.new_centroids
            else:
                break
            
        return self.centroids
    
    def elbow(self):
        self.SSE = [0 for i in range(20)]
        for k in range(1, 20):
            self.initialize(k)
            centroid_to_points = self.fit()
            for c in centroid_to_points:
                c_np = np.array(c)
                sq_diffs = np.square(np.array(centroid_to_points[c]) - np.tile(c_np, (len(centroid_to_points[c]), 1)))
                self.SSE[k] += np.sum(sq_diffs)
        
        print("Showing the elbow plot. Close the plot window to continue.")
        plt.plot([i for i in range(1, 20)], self.SSE[1:])
        plt.xlabel('Number of Clusters')
        plt.ylabel('Distortion Score')
        plt.tight_layout()
        plt.show()
    
    def plot(self):
        print(f'Plotting {self.k}-means results')
        cmap = plt.cm.rainbow
        norm = matplotlib.colors.Normalize(vmin=1.5, vmax=4.5)
        colors = []
        p_to_c = {}
        for i, c in enumerate(self.centroids):
            for p in self.centroids[c]:
                p_to_c[tuple(p)] = i+1
        
        for p in self.data:
            colors.append(p_to_c[tuple(p)])
                
        plt.scatter(self.data[:, 0], self.data[:, 1], color=cmap(norm(colors)))
        plt.tight_layout()
        plt.show()
        
            
class DataGeneration:
    def __init__(self):
        np.random.seed(1)
        x = 2
        data1 = np.random.normal(size=(100, 2)) + [ x, x]
        data2 = np.random.normal(size=(100, 2)) + [ x,-x]
        data3 = np.random.normal(size=(100, 2)) + [-x,-x]
        data4 = np.random.normal(size=(100, 2)) + [-x, x]
        data  = np.concatenate((data1, data2, data3, data4))
        np.random.shuffle(data)
        self.data = data

        
if __name__ == "__main__":
    generator = DataGeneration()
    k_means = KMeans(generator.data)
    k = input("Choose number of clusters: ")
    k_means.initialize(int(k))
    k_means.fit()
    k_means.plot()
    k_means.elbow()
