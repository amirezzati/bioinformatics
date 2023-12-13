import os
import numpy as np

def leaf_distance_matrix(n, adjacent):
    distances = np.zeros((n, n), dtype=int)
    
    # DFS to find path cost between start node to other nodes
    def dfs(curr_node, start_node, dest_nodes, weight, seen):
        seen.add(curr_node)
        
        for next_node, next_weight in adjacent[curr_node].items():
            if not dest_nodes:
                return
            elif next_node in dest_nodes:
                distances[start_node, next_node] = distances[next_node, start_node] = weight + next_weight
                dest_nodes.remove(next_node)
            elif next_node not in seen:
                dfs(next_node, start_node, dest_nodes, weight + next_weight, seen)

    for i in range(n - 1):
        dest_nodes = set(range(i + 1, n))
        dfs(i, i, dest_nodes, 0, set())

    return distances

cwd = os.getcwd()
inputFile = open(cwd + "/rosalind_ba7a.txt", "r")

n = int(inputFile.readline().rstrip())

start = [] # start of edges
end = [] # end of edges
weight = [] # weight of edges

while True:
    line = inputFile.readline()
    if line is None or line == '':
        break
    
    # extract value of a line such a->b:w
    line_sp = line.rstrip().split('->')
    a  = int(line_sp[0])
    b, w = map(int, line_sp[1].split(':'))
    start.append(a)
    end.append(b)
    weight.append(w)

adjacent = {}
for i in range(len(start)):
    if start[i] in adjacent:
        adjacent[start[i]][end[i]] = weight[i]
    else:
        adjacent[start[i]] = {end[i]: weight[i]}


leaf_distance_matrix = leaf_distance_matrix(n, adjacent)
for i in range(len(leaf_distance_matrix)):
    print(' '.join(map(str, leaf_distance_matrix[i])))

inputFile.close()