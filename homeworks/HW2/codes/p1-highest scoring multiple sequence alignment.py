
import os
import numpy as np
cwd = os.getcwd()

inputFile = open(cwd + '/rosalind_ba5m.txt', "r")
outputFile = open(cwd + '/p1_output.txt', "w")

DNAs = inputFile.read().split('\n')


def add_gap(dna, index):
    return dna[:index] + '-' + dna[index:]

def match(char1, char2, char3):
    return 1 if char1 == char2 == char3 else 0


def msa(dna1, dna2, dna3):
    score_matrix = [[[0 for k in range(len(dna3)+1)] for j in range(len(dna2)+1)] for i in range(len(dna1)+1)]
    backtrack = [[[0 for k in range(len(dna3)+1)] for j in range(len(dna2)+1)] for i in range(len(dna1)+1)]

    for i in range(1, len(dna1)+1):
        for j in range(1, len(dna2)+1):
            for k in range(1, len(dna3)+1):
                scores = [score_matrix[i-1][j-1][k-1] + match(dna1[i-1], dna2[j-1], dna3[k-1]), 
                          score_matrix[i-1][j][k], 
                          score_matrix[i][j-1][k], 
                          score_matrix[i][j][k-1], 
                          score_matrix[i-1][j-1][k], 
                          score_matrix[i-1][j][k-1],
                          score_matrix[i][j-1][k-1]]
                
                backtrack[i][j][k], score_matrix[i][j][k] = max(enumerate(scores), key=lambda p: p[1])

    dna1_a, dna2_a, dna3_a = dna1, dna2, dna3

    i, j, k = len(dna1), len(dna2), len(dna3)
    last_index_score = score_matrix[i][j][k]

    while i*j*k != 0: # until i=0 or j=0 or k=0
        if backtrack[i][j][k] == 0:
            i -= 1
            j -= 1
            k -= 1
        elif backtrack[i][j][k] == 1:
            i -= 1
            dna2_a = add_gap(dna2_a, j)
            dna3_a = add_gap(dna3_a, k)
        elif backtrack[i][j][k] == 2:
            j -= 1
            dna1_a = add_gap(dna1_a, i)
            dna3_a = add_gap(dna3_a, k)
        elif backtrack[i][j][k] == 3:
            k -= 1
            dna1_a = add_gap(dna1_a, i)
            dna2_a = add_gap(dna2_a, j)
        elif backtrack[i][j][k] == 4:
            i -= 1
            j -= 1
            dna3_a = add_gap(dna3_a, k)
        elif backtrack[i][j][k] == 5:
            i -= 1
            k -= 1
            dna2_a = add_gap(dna2_a, j)
        elif backtrack[i][j][k] == 6:
            j -= 1
            k -= 1
            dna1_a = add_gap(dna1_a, i)

    
    # alignment is done and now we should add gap in first of them
    alignedDNAs = [dna1_a, dna2_a, dna3_a]
    max_alignment_size = max(len(dna1_a),len(dna2_a),len(dna3_a))

    for i in range(len(alignedDNAs)):
        for j in range(max_alignment_size - len(alignedDNAs[i])):
            alignedDNAs[i] = add_gap(alignedDNAs[i], 0)

    return str(last_index_score), alignedDNAs[0], alignedDNAs[1], alignedDNAs[2]


import time
start_time = time.time()

result = msa(DNAs[0], DNAs[1], DNAs[2])
for d in result:
    outputFile.write(d+'\n')
    
# print("--- %s seconds ---" % (time.time() - start_time))


inputFile.close()
outputFile.close()