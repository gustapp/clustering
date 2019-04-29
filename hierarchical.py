#%% [markdown]
# # Hierarchical Clustering

#%%
# Libraries Imports
import numpy as np
import pandas as pd

#%%
# Initialize Data Points
""" (x-axis, y-axis) """
data_points = [(5.9, 3.2), (4.6, 2.9), (6.2, 2.8), (4.7, 3.2), (5.5, 4.2), (5.0, 3.0), (4.9, 3.1), (6.7, 3.1), (5.1, 3.8), (6.0, 3.0)]
len(data_points)

#%%
# Euclidian distance
def euclidian_dist(p1, p2):
  p1_arr = np.array(p1)
  p2_arr = np.array(p2)
  return np.linalg.norm(p1_arr-p2_arr)

