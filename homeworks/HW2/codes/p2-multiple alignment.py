import numpy as np
import os 

cwd = os.getcwd()

input_file = open(cwd + "/rosalind_mult.txt", "r")
outputFile = open(cwd + '/p2_output.txt', "w")

text = input_file.read()
DNA_strings = text.split('>')[1:] # the first index is empty string. so I removed it.

DNAs = []
for dna in DNA_strings:
    data = dna.split('\n')
    DNAs.append(''.join(data[1:]))


def align(backtrack, DNAs_a, DNAs, i, j, k, m):
    while i > 0 or j > 0 or k > 0 or m > 0:
        direc = backtrack[i, j, k, m]
        DNAs_a[0].append(DNAs[0][i - 1] if direc[0] else '-')
        DNAs_a[1].append(DNAs[1][j - 1] if direc[1] else '-')
        DNAs_a[2].append(DNAs[2][k - 1] if direc[2] else '-')
        DNAs_a[3].append(DNAs[3][m - 1] if direc[3] else '-')
        i, j, k, m = i - direc[0], j - direc[1], k - direc[2], m - direc[3]


# 15 different directions
dirs = {'1':[0, 0, 0, 1], # [i, j, k, l-1]
        '2': [0, 0, 1, 0], #[i, j, k-1, l]
        '3': [0, 1, 0, 0], 
        '4': [1, 0, 0, 0], 
        '5': [0, 0, 1, 1],
        '6': [0, 1, 0, 1], 
        '7': [1, 0, 0, 1], 
        '8': [0, 1, 1, 0], 
        '9': [1, 0, 1, 0], 
        '10': [1, 1, 0, 0],
        '11': [0, 1, 1, 1], 
        '12': [1, 0, 1, 1], 
        '13': [1, 1, 1, 0], 
        '14': [1, 1, 0, 1], 
        '15': [1, 1, 1, 1]}


score_matrix = np.zeros((len(DNAs[0]) + 1, len(DNAs[1]) + 1, len(DNAs[2]) + 1, len(DNAs[3]) + 1))
backtrack = [[[[None for m in range(len(DNAs[3]) + 1)] for k in range(len(DNAs[2]) + 1)] for j in range(len(DNAs[1]) + 1)] for i in range(len(DNAs[0]) + 1)]
backtrack = np.asarray(backtrack)

# intialize matrix with gap score
for i in range(1, len(DNAs[0]) + 1):
    score_matrix[i, 0, 0, 0] = -i * 3
    backtrack[i, 0, 0, 0] = dirs['4']
for i in range(1, len(DNAs[1]) + 1):
    score_matrix[0, i, 0, 0] = -i * 3
    backtrack[0, i, 0, 0] = dirs['3']
for i in range(1, len(DNAs[2]) + 1):
    score_matrix[0, 0, i, 0] = -i * 3
    backtrack[0, 0, i, 0] = dirs['2']
for i in range(1, len(DNAs[3]) + 1):
    score_matrix[0, 0, 0, i] = -i * 3
    backtrack[0, 0, 0, i] = dirs['1']
    

def mismatch_penalty(chars):
    penalty = 0
    for c1 in range(len(chars) - 1):
        for c2 in range(c1 + 1, len(chars)):
            penalty += 0 if chars[c1] == chars[c2] else -1
    return penalty

# fill score matrix
for i in range(len(DNAs[0]) + 1):
    for j in range(len(DNAs[1]) + 1):
        for k in range(len(DNAs[2]) + 1):
            for m in range(len(DNAs[3]) + 1):
                if i + j + k + m > 1:
                    best_score = -1000
                    best_direc = None
                    for idx in range(1, 16):
                        direc = dirs[str(idx)]
                        if (direc[0]==0 or i > 0) and (direc[1]==0 or j > 0) and (direc[2]==0 or k > 0) and (direc[3]==0 or m > 0):
                            
                            char1 = DNAs[0][i - 1] if direc[0] else '-'
                            char2 = DNAs[1][j - 1] if direc[1] else '-'
                            char3 = DNAs[2][k - 1] if direc[2] else '-'
                            char4 = DNAs[3][m - 1] if direc[3] else '-'

                            chars = [char1, char2, char3, char4]
                            score = score_matrix[i - direc[0]][j - direc[1]][k - direc[2]][m - direc[3]]
                            score += mismatch_penalty(chars)

                            if score > best_score:
                                best_score = score
                                best_direc = direc

                    score_matrix[i, j, k, m] = best_score
                    backtrack[i, j, k, m] = best_direc


DNAs_a = [[], [], [], []]
align(backtrack, DNAs_a, DNAs, len(DNAs[0]), len(DNAs[1]), len(DNAs[2]), len(DNAs[3]))


outputFile.write(str(int(score_matrix[len(DNAs[0]), len(DNAs[1]), len(DNAs[2]), len(DNAs[3])]))+'\n')
outputFile.write(''.join(reversed(DNAs_a[0]))+'\n')
outputFile.write(''.join(reversed(DNAs_a[1]))+'\n')
outputFile.write(''.join(reversed(DNAs_a[2]))+'\n')
outputFile.write(''.join(reversed(DNAs_a[3])))

input_file.close()
outputFile.close()