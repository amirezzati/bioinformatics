import os
import numpy as np

cwd = os.getcwd()
inputFile = open(cwd + "/rosalind_ba7e.txt", "r")
outputFile = open(cwd + "/p7_output.txt", "w")

n = int(inputFile.readline())

inputFile = inputFile.read()
inputLines = inputFile.split('\n')[:n]

D = np.array([line.split() for line in inputLines], dtype= float)


def neighborJoiningTree(D, nodes, last_node_num):
    n = D.shape[0]
    D_star = np.zeros((n,n))
    last_node_num += 1

    # it will finish when 2 nodes remain in the D matrix
    if n == 2:            
        Tree = {}
        Tree[nodes[0]] = [(nodes[1], D[0][1])]
        Tree[nodes[1]] = [(nodes[0], D[0][1])]
        return Tree
        
    # total distance of node i to other nodes
    R = D.sum(axis=0)
    
    # compute D* matrix for half of D matrix
    for i in range(n-1):
        for j in range(i+1,n):
            D_star[i][j] = (n-2)*D[i][j] - R[i] - R[j]
            D_star[j][i] = D_star[i][j]
    
    # find the pair i,j which has minimum distance in D* matrix
    [i, j] = np.where(D_star==np.min(D_star))
    [i, j] = [i[0], j[0]]  # select a pair in list of minimum distance 
    (ni, nj) = (nodes[i], nodes[j])  # save node indices to make connection to new node later
    
    # calculate distance of new node to nodes i, j
    dis_i2newNode = ( D[i][j] + ((R[i] - R[j]) / (n-2)) ) / 2
    dis_j2newNode = (D[i][j] + ((R[j] - R[i]) / (n-2)) ) / 2
    del(D_star, R)
    
    # calculate distance of new node to others except i, j
    D_newNode = []
    for k in range(n):
        if k not in (i,j):        
            D_newNode.append((D[i][k] + D[j][k] - D[i][j]) / 2)
    D_newNode.append(0)
    
    # remove row and col of node ith and jth
    D = np.delete(D, (i, j), 0)
    D = np.delete(D, (i, j), 1) 
    
    # add new node distance to D matrix
    D = np.append(D, [D_newNode[:-1]], 0)
    D = np.append(D, [[d] for d in D_newNode], 1)
    
    # delete node i and j from nodes list and adding new node(last_node_num) to nodes list
    nodes = np.append(nodes, last_node_num)
    for leaf in (j,i):
        nodes = np.delete(nodes, leaf)
        
    # compute neighbor joining tree for remaining nodes
    Tree = neighborJoiningTree(D, nodes, last_node_num)
    
    # add connection between new node and node i, j
    k = nodes[-1]
    Tree[k] += [(ni, "%.3f" %(dis_i2newNode)), (nj, "%.3f" %(dis_j2newNode))]
    Tree[ni] = [(k, "%.3f" % (dis_i2newNode))]
    Tree[nj] = [(k, "%.3f" % (dis_j2newNode))]

    return Tree


initial_nodes = np.array(range(n)) # node 0, 1, ..., n-1
nj_tree = neighborJoiningTree(D, initial_nodes, n-1) # last_node_num = n-1

edges = []
for a in nj_tree.keys():
    for b in nj_tree[a]:
        edges.append((a, b[0], b[1]))

for edge in sorted(edges):
    outputFile.write('{0}->{1}:{2}\n'.format(edge[0],edge[1],edge[2]))
outputFile.close()