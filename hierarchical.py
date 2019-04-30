#%% [markdown]
# # Hierarchical Clustering

#%%
# Libraries Imports
import numpy as np
import pandas as pd

#%%
# Initialize Data Points
""" (x-axis, y-axis) """
cA_data_points = [(4.7, 3.2), (4.9, 3.1), (5.0, 3.0), (4.6, 2.9)]
cB_data_points = [(5.9, 3.2), (6.7, 3.1), (6.0, 3.0), (6.2, 2.8)]

print(cA_data_points)
print(cB_data_points)

#%%
# Euclidian distance
def euclidian_dist(p1, p2):
  p1_arr = np.array(p1)
  p2_arr = np.array(p2)
  return np.linalg.norm(p1_arr-p2_arr)

p1 = (4.7, 3.2)
p2 = (6.7, 3.1)
print('Test 1: ' + str(euclidian_dist(p1, p2)))

p1 = (4.7, 3.2)
p2 = (6.0, 3.0)
print('Test 2: ' + str(euclidian_dist(p1, p2)))

#%%
# Calculate distance between cluster members
distances_a = []
for a_dp in cA_data_points:
  distances_b = []
  for b_dp in cB_data_points:
    dist = euclidian_dist(a_dp, b_dp)
    distances_b.append(dist)
  distances_a.append(distances_b)

dist_df = pd.DataFrame(data=distances_a)
dist_df.head()

#%%
# Distance between the two fastest members
max_dist = dist_df.max().max()
print('complete link: ' + str(max_dist))

#%%
# Distance between the two closest members
min_dist = dist_df.min().min()
print('single link: ' + str(min_dist))

#%%
# Average distance between all pairs
mean_dist = dist_df.mean().mean()
print('average link: ' + str(mean_dist))

#%% [markdown]
# ## Most robust measure to noise
# > average