import os
import numpy as np

cwd = os.getcwd()
inputFile = open(cwd + "/rosalind_ba7b.txt", "r").read()
inputLines = inputFile.split('\n')

n = int(inputLines[0])
j = int(inputLines[1])
D = np.array([list(map(int, row.split())) for row in inputLines[2:-1]])

# limb length of node j equals to minimum distance of j to each i,k in the graph
# limbLength(j) = min of [ (D[i][j] + D[j][k] - D[i][k])/2 for each i,k in graph ]
distanceJtoIK = []
for i in range(n):
    for k in range(n):
        dis = (D[i][j] + D[j][k] - D[i][k])/2
        if dis > 0:
            distanceJtoIK.append(int(dis))

print(min(distanceJtoIK))