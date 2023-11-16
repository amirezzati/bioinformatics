import os
from Bio.Align import substitution_matrices

cwd = os.getcwd()
f = open(cwd + "/rosalind_laff.txt", "r")
outputFile = open(cwd + '/p10_output.txt', "w")

text = f.read()
DNA_strings = text.split('>')[1:] # the first index is empty string. so I removed it.

seqs = []
for dna in DNA_strings:
    data = dna.split('\n')
    seqs.append(''.join(data[1:]))

seq1 = seqs[0]
seq2 = seqs[1]

blosum62 = substitution_matrices.load("BLOSUM62")

def get_local_alignment_affine_gap(s, t):
    sl, tl = len(s), len(t)
    
    x = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
    m = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
    y = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
    backtrack = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
    max_score = -1
    max_i, max_j = 0, 0

    for i in range(1, sl + 1):
        for j in range(1, tl + 1):
            x[i][j] = max([x[i - 1][j] - 1, m[i - 1][j] - 11])
            y[i][j] = max([y[i][j - 1] - 1, m[i][j - 1] - 11])
            op = [x[i][j], m[i - 1][j - 1] + blosum62[s[i - 1]][t[j - 1]], y[i][j], 0]
            m[i][j] = max(op)
            backtrack[i][j] = op.index(m[i][j])

            if m[i][j] > max_score:
                max_score = m[i][j]
                max_i, max_j = i, j

    # Backtrack to start of the local alignment
    i, j = max_i, max_j
    sa, ta = s[:i], t[:j]
    while backtrack[i][j] != 3 and i * j != 0:
        if backtrack[i][j] == 0:
            i -= 1
        elif backtrack[i][j] == 1:
            i -= 1
            j -= 1
        elif backtrack[i][j] == 2:
            j -= 1
    sa, ta = sa[i:], ta[j:]

    return {"score": int(max_score), "sa": sa, "ta": ta}

import time
start_time = time.time()

dic = get_local_alignment_affine_gap(seq1, seq2)

outputFile.write(str(dic['score'])+'\n')
outputFile.write(dic['sa']+'\n')
outputFile.write(dic['ta'])

print("--- %s seconds ---" % (time.time() - start_time))

f.close()
outputFile.close()