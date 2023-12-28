import numpy as np

# getting input
first_line = input()
n, k = list(map(int, first_line.split()))

kmers = []
for i in range(n):
    kmer = input()
    kmers.append(kmer)
    del(kmer)

q = int(input())
queries = []
for i in range(q):
    query = input()
    queries.append(query)
    del(query)


# functions
def construct_debruijn_graph(kmers):
    edges = {}
    for kmer in kmers:
        if kmer[:-1] not in list(edges.keys()):
            edges[kmer[:-1]]=[kmer[1:]]
        else:
            edges[kmer[:-1]].append(kmer[1:])

    return edges


def assembly(sequences, seq, curr_node_, edges_):
    if curr_node_ in edges_:
        seq += curr_node_[-1]
        childs = edges_.pop(curr_node_)
        for child in childs:
            assembly(sequences, seq, child, edges_.copy())
        return

    else:
        seq += curr_node_[-1]
        sequences.append(seq)
        return

def last_to_first(bwt_str):
    first_to_last = sorted(range(len(bwt_str)), key=lambda i: bwt_str[i]) 
    return np.argsort(first_to_last) # convet to last_to_first


# this function also return map of first col index to original index of sequence
def bwt_transform(text):
    rotations = [(i, text[i:] + text[:i]) for i in range(len(text))]
    sorted_rotations = sorted(rotations, key=lambda x: x[1])
    mapFirstColToOrigIndex = [elem[0] for elem in sorted_rotations]

    bwt_result = ''.join([rotation[1][-1] for rotation in sorted_rotations])
    return mapFirstColToOrigIndex, bwt_result


# this function return first index of queries in first column
def bw_matching(lastColumn, pattern, lastToFirst):
    top = 0
    bottom = len(lastColumn) - 1
    # print(lastColumn)
    while top <= bottom:
        if len(pattern) != 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]

            topToBottomChars = lastColumn[top:bottom+1] # top index to bottom index chars in lastColumn
            if symbol in topToBottomChars:
                top_inedx = top + topToBottomChars.find(symbol)
                bottom_index = bottom - topToBottomChars[::-1].find(symbol)
                top = lastToFirst[top_inedx]
                bottom = lastToFirst[bottom_index]
            else:
                return 0
        else:
            return [i for i in range(top, bottom + 1)]


# main
edges = construct_debruijn_graph(kmers)
# print(edges)
keys = edges.keys()
values = [x for xs in edges.values() for x in xs]
first_nodes = list(set(keys) - set(values))
# print(first_nodes)
# assembly all sequences that are possible
sequences = []
for curr_node in first_nodes:
    curr_node_ = curr_node
    edges_ = edges.copy()
    seq = curr_node_[:-1]
    
    assembly(sequences, seq, curr_node_, edges_)


# print(sequences)
# finding queries indices with bw matching
queries_indices = []
for query in queries:
    indices = []
    for seq in sequences:
        firstCol_to_origIndex, bwt = bwt_transform(seq)
        last2first = last_to_first(bwt)
        match = bw_matching(bwt, query, last2first)
        if match == 0: # the query doesnt exist in sequence
            indices.append(match)
        else: # the query exists in sequence and match is list of first col indices
            indices.extend([firstCol_to_origIndex[index]+1 for index in match])
    # queries_indices.append(indices)
    queries_indices.append(sorted(list(set(indices))))

print('list: ', queries_indices)
for query_indices in queries_indices:
    print(-1) if len(query_indices)==1 and query_indices[0]==0 else print(' '.join([str(i) for i in query_indices if i != 0])) 