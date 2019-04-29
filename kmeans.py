#%% [markdown]
# # K-means Algorithm

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

""" Tests: euclidian_dist(p1, p2) """
p1 = (5.9, 3.2)
p2 = (5.9, 3.2)
print('Test 1 - p1 = p1: ' + str(euclidian_dist(p1, p2)))

p1 = (1.0, 0.0)
p2 = (0.0, 1.0)
print('Test 2: root(2): ' + str(euclidian_dist(p1, p2)))

p1 = (2.0, 0.0)
p2 = (1.0, 3.0)
print('Test 3: root(10): ' + str(euclidian_dist(p1, p2)))

p1 = (6.2, 3.2)
p2 = (5.9, 3.2)
print('Test 4: dist(c1, dp1): ' + str(euclidian_dist(p1, p2)))

p1 = (6.6, 3.7)
p2 = (5.9, 3.2)
print('Test 5: dist(c2, dp1): ' + str(euclidian_dist(p1, p2)))

p1 = (6.5, 3.0)
p2 = (5.9, 3.2)
print('Test 6: dist(c3, dp1): ' + str(euclidian_dist(p1, p2)))

#%%
# Initialize centroids: K = 3
c1 = (6.2, 3.2) # red
c2 = (6.6, 3.7) # green
c3 = (6.5, 3.0) # blue

centroids = [c1, c2, c3]
centroids

#%%
# Calculate the distance of all data points
def calculate_dist_all(data_points, centroids):
  distances = []
  for point in data_points:
    distance_per_point = []
    for centroid in centroids:
      dist = euclidian_dist(centroid, point)
      distance_per_point.append(dist)
    distances.append(distance_per_point)
  return distances

distances = calculate_dist_all(data_points, centroids)

df = pd.DataFrame(data=distances)
df.head()

#%%
# Calculate the nearest centroid to each data point
groups = df.idxmin(axis=1)
groups.head()

#%%
# Assign data points to each centroid
clusters = [[], [], []]
count = 0
for dp in groups.values:
  clusters[dp].append(data_points[count])
  count += 1

clusters

#%%
# Recalculate centroids
c_centroids = 0
for cluster in clusters:
  x_axis = 0
  y_axis = 0
  for dp in cluster:
    x_axis += dp[0] / len(cluster)
    y_axis += dp[1] / len(cluster)
  centroids[c_centroids] = (x_axis, y_axis)
  c_centroids += 1

centroids

