import os

cwd = os.getcwd()
inputFile = open(cwd + "/rosalind_ba7c.txt", "r")
outputFile = open(cwd + "/p5_output.txt", "w")

n = int(inputFile.readline())

inputFile = inputFile.read()
inputLines = inputFile.split('\n')[:n]

D = [list(map(int, line.split())) for line in inputLines]
# print(D)

# inputFile.close()

def limb_length(D, n):
    distances = []
    for i in range(n-1):
        for k in range(i+1, n):
            dis = (D[i][n] + D[k][n] - D[i][k]) /2
            distances.append(int(dis))    
    return min(distances)


def get_path(tree, source, dest):
    # find path between node i and node k
    def dfs(tree, i, k, visited=None):
        if visited is None:
            visited = set()
        stack = [(i, [i])]

        while stack:
            vertex, path = stack.pop(0)
            if vertex not in visited:
                if vertex == k:
                    return path
                visited.add(vertex)
                for neighbor in tree[vertex]:
                    stack.append((neighbor[0], path + [neighbor[0]]))
        return False

    # find path with DFS
    path = dfs(tree, source, dest)

    # calculate path_distance
    path_distance = [0]
    for i in range(1, len(path)):
        for d in tree[path[i]]:
            if d[0] == path[i - 1]:
                path_distance.append(path_distance[i - 1] + d[1])

    return list(zip(path, path_distance))


def add_leaf_n(tree, path, n, limb, x):
    def add_leaf_parent(path, x):
        left = path[0]
        for right in path[1:]:
            if right[1] < x:
                left = right
            elif right[1] == x:
                return right[0], tree
            elif right[1] > x:
                tree[left[0]].remove((right[0], right[1] - left[1]))
                tree[right[0]].remove((left[0], right[1] - left[1]))
                left_x = x - left[1]
                right_x = right[1] - x
                new = len(tree)
                tree[new] = [(left[0], left_x), (right[0], right_x)]
                tree[left[0]].append((new, left_x))
                tree[right[0]].append((new, right_x))
                return new, tree

    # add node n to tree
    parent_n, tree = add_leaf_parent(path, x)

    # Adding leaf edge to parent
    tree[parent_n].append((n, limb))
    tree[n].append((parent_n, limb))
    return tree

def three_leaves(D, n):
    for i in range(n - 1):
        for k in range(i + 1, n):
            if D[i][k] == D[i][n] + D[k][n]:
                return (i, k)
            
def additive_phylogeny(D, n):
    if n == 1: # when we have only 2 nodes such node 0 and 1
        nodes = list(range(len(D)))
        tree = dict(zip(nodes, list([] for _ in nodes)))
        tree[0].append((1, D[0][1]))
        tree[1].append((0, D[0][1]))
        return tree

    # D_bald matrix
    limb_l = limb_length(D, n)
    for j in range(n):
        D[j][n] = D[j][n] - limb_l
        D[n][j] = D[j][n]

    # three leaves i, k, n which D[i][k] == D[i][n] + D[k][n]
    (i, k) = three_leaves(D, n)
    x = D[i][n]

    # recursion
    tree = additive_phylogeny(D, n - 1)

    # adding leaf n
    path_ik = get_path(tree, i, k)
    tree = add_leaf_n(tree, path_ik, n, limb_l, x)

    return tree
       

# running additive phylogeny
tree = additive_phylogeny(D, n-1) 
    
edges = []
for u in tree.keys():
    for w in tree[u]:
        outputFile.write(str(u)+'->'+str(w[0])+':'+ str(w[1])+'\n')

outputFile.close()