import numpy as np
import pandas as pd

# scale data
scale = np.array([[9], [8], [7], [9], [5], [4], [3], [2], [1], [1/2], [1/3], [1/4], [1/5], [1/6], [1/7], [1/8], [1/9]])
max_alpha_total = np.zeros([100, 1])
RI = np.zeros([100, 1])
for i in range(100):    # order of iteration
    max_alpha = np.zeros([10000, 1])  # iterate times
    for j in range(10000):
        scale_matrix = np.random.randint(1, 17, (i+1, i+1))
        judge_matrix = np.zeros([i+1, i+1])
        weight = np.zeros([i+1, 1])
        # generate judge matrix
        for k in range(i+1):
            for m in range(i+1):
                judge_matrix[k, m-k] = scale[scale_matrix[k, m-1]]
                judge_matrix[m-k, k] = 1 / scale[scale_matrix[k, m-1]]
                judge_matrix[k, k] = 1
        alpha, beta = np.linalg.eig(judge_matrix)
        max_alpha[j] = max(alpha.real)
    max_alpha_mean = max_alpha.mean()
    max_alpha_total[i] = max_alpha_mean
    if i == 0:
        RI[i] = 0
    else:
        RI[i] = (max_alpha_mean - (i+1)) / i   # i=0时无法计算

# save result
max_alpha_total = pd.DataFrame(max_alpha_total, columns=['lambda'])
RI = pd.DataFrame(RI, columns=['RI'])
result = pd.concat([max_alpha_total, RI], axis=1)
