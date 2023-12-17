import os
import numpy as np

cwd = os.getcwd()
inputFile = open(cwd + "/rosalind_ba7d.txt", "r")
outputFile = open(cwd + "/p6_output.txt", "w")

n = int(inputFile.readline())

inputFile = inputFile.read()
inputLines = inputFile.split('\n')[:n]

D = np.array([line.split() for line in inputLines], dtype= float)
np.fill_diagonal(D, np.inf)


def UPGMA(D,n):     
    Clusters = {node:[node] for node in range(n)} # each node has itself at first
    Graph = {node:[] for node in range(n)} # initial nodes have not any child
    Age = {node:0 for node in range(n)} # initial node ages equal 0
    heads = list(range(n)) # only the nodes which are root of clusters

    # until we have just one cluster and one root
    while len(heads)>1:
        Cnew = len(Graph) # next index
        
        [i, j] = np.where(D==np.min(D))
        [i, j] = [i[0], j[0]]   # select a pair in list of minimum distance
        Ci, Cj = heads[i], heads[j]

        # updating Age, Clusters, and Graph
        Age[Cnew] = D[i][j]/2   # age of new cluster node
        Clusters[Cnew] = Clusters[Ci] + Clusters[Cj]    # new cluster members
        Graph[Cnew] = [Ci, Cj] # cluster node's children
        
        Ci_num, Cj_num = len(Clusters[Ci]), len(Clusters[Cj])
        
        # calculate distance of new cluster to other clusters
        D_Cnew = []
        for k in range(len(heads)):
            if k != i and k != j:
                distance = ((Ci_num*D[i][k]) + (Cj_num*D[j][k]) ) / (Ci_num + Cj_num)
                D_Cnew.append(distance)
        
        # remove previous clusters from heads and add new cluster to heads 
        heads.remove(Ci)
        heads.remove(Cj)
        heads.append(Cnew)
                
        # remove previous row and column of cluster ith and cluster jth 
        D = np.delete(D, (i, j), 0)
        D = np.delete(D, (i, j), 1) 
        
        # add new row
        D = np.append(D, [D_Cnew], 0)
        # add new column
        D_Cnew.append(float('inf'))
        D = np.append(D, [[d] for d in D_Cnew], 1)
    
    # compute edge's weights
    edges = []
    for a in Graph.keys():
        for b in Graph[a]:
            weight = abs(Age[a] - Age[b])
            edges.append((a, b, "%.3f" % weight))
            edges.append((b, a, "%.3f" % weight))
    return edges            


edges = UPGMA(D,n)

for edge in sorted(edges):
    outputFile.write(f'{edge[0]}->{edge[1]}:{edge[2]}\n')
outputFile.close()