import numpy as np
import matplotlib.pyplot as plt

# Step 1 - Collect data
england = np.array([375, 57, 245, 1472, 105, 54, 193, 147, 1102, 720, 253, 685, 488, 198, 360, 1374, 156], dtype=np.float64)
n_ireland = np.array([135, 47, 267, 1494, 66, 41, 209, 93, 674, 1033, 143, 586, 355, 187, 334, 1506, 139], dtype=np.float64)
scotland = np.array([458, 53, 242, 1462, 103, 62, 184, 122, 957, 566, 171, 750, 418, 220, 337, 1572, 147], dtype=np.float64)
wales = np.array([475, 73, 227, 1582, 103, 64, 235, 160, 1137, 874, 265, 803, 570, 203, 365, 1256, 175], dtype=np.float64)

# england = np.array([np.random.rand() * 5.0 + i for i in range(200)])
# n_ireland = np.array([np.random.rand() * 200.0 for i in range(200)])
# scotland = np.array([np.random.rand() * 10.0 + i for i in range(200)])
# wales = np.array([np.random.rand() * 15.0 + i for i in range(200)])

# .T transposes the array
original_data = np.array([england, n_ireland, scotland, wales]).T

# Step 2 - Offset data
# print original_data[0]
for i,row in enumerate(original_data):
    mean = np.mean(row)
    original_data[i] = row - mean
# print original_data[0]

# Step 3 - Get covariance matrix

cov_matrix = np.cov(original_data)
# print cov_matrix[0]

# Step 4 - Get eigenvectors and eigenvalues
# temp.append(np.linalg.eigh(cov_matrix))
vals,vects = np.linalg.eigh(cov_matrix)
temp = [(val,vec) for val,vec in zip(vals,vects)]
# print val
# print vect

# Step 5 - Generate a feature vector.  Here we reduce dimensions to 1 based on the largest eigenvalue
# print evals.index
# sort by a[start=0: stop=len:step=-1]
N = 17
sort_array = sorted(temp,key = lambda x:x[0])[::-1]
feature = [value[1] for value in sort_array][:min(N,len(sort_array))]
# print feature
# for value in sort_array:
#     feature.append(value[1])
# print feature


# Step 6 - Generate new data
new_data = np.dot(feature,original_data)
# print new_data


# Step 7 - Plot
plt.plot(new_data[0][0], 0, 'c.', label = "England",markersize=20)
plt.plot(new_data[0][1], 0, 'm.', label = "Ireland",markersize=20)
plt.plot(new_data[0][2], 0, 'b.', label = "Scotland",markersize=20)
plt.plot(new_data[0][3], 0, 'r.', label = "Wales",markersize=20)
plt.legend()
plt.show()

plt.plot(new_data[0][0], new_data[1][0], 'c.', label = "England",markersize=20)
plt.plot(new_data[0][1], new_data[1][1], 'm.', label = "Ireland",markersize=20)
plt.plot(new_data[0][2], new_data[1][2], 'b.', label = "Scotland",markersize=20)
plt.plot(new_data[0][3], new_data[1][3], 'r.', label = "Wales",markersize=20)
plt.legend()
plt.show()

# Here we plot for 1 dimension
