import os
import numpy as np
cwd = os.getcwd()

f = open(cwd + "/rosalind_pdst.txt", "r")

text = f.read()
DNA_strings = text.split('>')[1:] # the first index is empty string. so I removed it.

# print(DNA_strings)

seq_names = []
seqs = []
for dna in DNA_strings:
    data = dna.split('\n')
    seq_names.append(data[0])
    seqs.append(''.join(data[1:]))

def distance(a, b):
    distance = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            distance += 1
    return distance/len(a)


d = np.zeros((len(seq_names), len(seq_names)))
# calculate distance for half of matrix that i > j
for i in range(len(seq_names)):
    for j in range(len(seq_names)):
        if i>j:
            d[i, j] = distance(seqs[i], seqs[j])

# add d and d.T because d[i,j] = d[j, i]
d = d + d.T
# print(d)
for r in range(len(d)): # rows   
    for c in range(len(d[r])): # columns
        print ('{:.4f}'.format(d[r][c]), " ", sep="", end="")  
    print()

f.close()
