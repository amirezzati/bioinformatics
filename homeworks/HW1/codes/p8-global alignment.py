import os
from Bio.Align import substitution_matrices
from itertools import product

cwd = os.getcwd()
f = open(cwd + "/rosalind_glob.txt", "r")

text = f.read()
DNA_strings = text.split('>')[1:] # the first index is empty string. so I removed it.

seqs = []
for dna in DNA_strings:
    data = dna.split('\n')
    seqs.append(''.join(data[1:]))

seq1 = seqs[0]
seq2 = seqs[1]

blosum62 = substitution_matrices.load("BLOSUM62")

def get_max_alignment(s, t):
    sl, tl = len(s), len(t)
    matrix = {(0, 0): (0, None)}
    matrix.update({((i, 0), (i * - 5, (i - 1, 0))) for i in range(1, sl + 1)})
    matrix.update({((0, i), (i * - 5, (0, i - 1))) for i in range(1, tl + 1)})
    
    for i, j in product(range(1, sl + 1), range(1, tl + 1)):
        cost = blosum62.get((s[i - 1], t[j - 1]))
        
        if cost == None:
            cost = blosum62.get((t[j - 1], s[i - 1]))
        diagonal = matrix[(i - 1, j - 1)][0] + cost
        up = matrix[(i - 1, j)][0] - 5
        left = matrix[(i, j - 1)][0] - 5
        b = max(diagonal, up, left)
        
        if diagonal == b:
            matrix[(i, j)] = (b, (i - 1, j - 1))
        elif up == b:
            matrix[(i, j)] = (b, (i - 1, j))
        elif left == b:
            matrix[(i, j)] = (b, (i, j - 1))
            
    return matrix[(i, j)][0]


print(int(get_max_alignment(seq1, seq2)))