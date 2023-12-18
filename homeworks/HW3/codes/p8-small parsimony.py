import os

# files
cwd = os.getcwd()
inputFile = open(cwd + "/rosalind_ba7f.txt", "r")
outputFile = open(cwd + "/p8_output.txt", "w")

# setup
alphabet = 'ACGT'
tree = {}
sequences = []

n = int(inputFile.readline().strip())
numberOfnodes = 2*n - 1

for line in inputFile.readlines():
    v, w = line.strip().split('->')
    v = int(v)
    if w[0] in alphabet:
        sequences.append(w)
        w = len(sequences) - 1 # create index of seq w
    else:
        w = int(w)

    if v not in tree.keys():
        tree[v] = [w]
    else:
        tree[v].append(w)

    if w not in tree.keys():
        tree[w] = []

sequences += ['' for i in range(n, numberOfnodes)] # empty string for the nodes which we should calculate them
inputFile.close()
del(v,w, line)

print('initial sequences: ', sequences)
print('Tree structure: ', tree)

# functions
def hamming_distance(v, w):
    return sum(1 for i, j in zip(v, w) if i != j)

def small_parsimony(Tree, sequences, n):

    def sp_scoring(Tree, column): # parismony scores for each column or character in sequences

        Tag = [0 for i in range(numberOfnodes)] # leaf nodes equal to 1 and others equal 0
        
        S, pointers = {}, {}
        for v in range(n): # for all sequences in the leafs
            S[v] = {}
            Tag[v] = 1
            pointers[v] = sequences[v][column]
            for k in alphabet:
                if k == sequences[v][column]:
                    S[v][k] = 0
                else:
                    S[v][k] = float('inf')

        # while there is node which we didn't calculate score for it
        while 0 in Tag:  
            v = Tag.index(0) # find first index that has value of 0
            Tag[v] = 1
            
            S[v] = {}
            pointers[v] = {}
            son_v, daughter_v = Tree[v][0], Tree[v][1]
            
            # calculate S[v] for each k in alphabet
            for alphabet_char in alphabet:
                son_v_scores = []
                daughter_v_scores = []
                for sequence_char in alphabet:
                    # delta part of score
                    delta_ik = 1
                    if alphabet_char == sequence_char:
                        delta_ik = 0
                  
                    son_v_scores.append(S[son_v][sequence_char] + delta_ik)
                    daughter_v_scores.append(S[daughter_v][sequence_char] + delta_ik)
        
                S[v][alphabet_char] = min(son_v_scores) + min(daughter_v_scores)
         
                # set pointers[v][alphabet_char] to min score of son and daughter
                son_p = alphabet[son_v_scores.index(min(son_v_scores))]
                daughter_p = alphabet[daughter_v_scores.index(min(daughter_v_scores))]
                pointers[v][alphabet_char] = (son_p, daughter_p)
        
        return S, pointers

    
    def sp_complete_sequences(Tree, S, pointers, sequences):  
        best = float('inf')
        root_index = numberOfnodes - 1
        charOfNode = ['' for i in range(numberOfnodes)]
        for ch in S[root_index].keys():            
            if S[root_index][ch] < best:           
                best = S[root_index][ch]
                charOfNode[root_index] = ch 
        
        for v in range(2*n-2, n-1, -1):    
            char = charOfNode[v]
            sequences[v] += char       
            [son_v, daughter_v] = Tree[v] 
            charOfNode[son_v], charOfNode[daughter_v] = pointers[v][char]

        return sequences
    
    # construct sequences one char by one char
    root_index = numberOfnodes - 1
    parsimony_score = 0
    m = len(sequences[0])
    for i in range(m): # over all chars of sequence
        S,pointers = sp_scoring(Tree, i) # calculate score for char ith of sequences
        parsimony_score += min(S[root_index].values())    
        sequences = sp_complete_sequences(Tree, S, pointers, sequences) 
    
    return sequences, parsimony_score

# runnig small parsimony
sequences, parsimony_score = small_parsimony(tree, sequences, n)

print('final sequences: ', sequences)
print('parsimony_score: ', parsimony_score)

edges = []
for v in tree.keys():
    for w in tree[v]:
        hd = hamming_distance(sequences[v], sequences[w])
        edges.append(sequences[w] + '->' + sequences[v] + ':' + str(hd))
        edges.append(sequences[v] + '->' + sequences[w] + ':' + str(hd))

print('edges: ', edges)
outputFile.write(str(parsimony_score))
for edge in edges:
    outputFile.write('\n'+edge)
outputFile.close()