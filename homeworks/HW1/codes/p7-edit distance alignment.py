import os
import numpy as np
cwd = os.getcwd()

f = open(cwd + "/rosalind_edta.txt", "r")

text = f.read()
DNA_strings = text.split('>')[1:] # the first index is empty string. so I removed it.

seqs = []
for dna in DNA_strings:
    data = dna.split('\n')
    seqs.append(''.join(data[1:]))

seq1 = seqs[0]
seq2 = seqs[1]

# print(seq1, seq2)
d_matrix = np.zeros((len(seq1)+1, len(seq2)+1))

for i in range(1, len(seq1) + 1):
    d_matrix[i][0] = i
for i in range(1, len(seq2) + 1):
    d_matrix[0][i] = i
for i in range(1, len(seq1) + 1):
    for j in range(1, len(seq2) + 1):
        if seq1[i-1] == seq2[j-1]:
            cost = 0
        else:
            cost = 1
        d_matrix[i][j] = min(d_matrix[i-1][j] + 1, d_matrix[i][j-1] + 1, d_matrix[i-1][j-1] + cost)

print(int(d_matrix[len(seq1)][len(seq2)]))



def cost(char1, char2):
    if char1 == char2:
        return(0) # match cost = 0
    return(1) # mismatch cost = 0

seq1_ = ''
seq2_ = ''
i = len(seq1)
j = len(seq2)

while i*j != 0:
    if d_matrix[i][j] == d_matrix[i-1][j-1] + cost(seq1[i-1], seq2[j-1]):
        seq1_ = seq1[i-1] + seq1_
        seq2_ = seq2[j-1] + seq2_
        i -= 1
        j -= 1
    elif i > 0 and d_matrix[i][j] == d_matrix[i-1][j] + 1:
        seq1_ = seq1[i-1] + seq1_
        seq2_ = '-' + seq2_
        i -= 1
    else:
        seq2_ = seq2[j-1] + seq2_
        seq1_ = '-' + seq1_
        j -= 1

print(seq1_)
print(seq2_)