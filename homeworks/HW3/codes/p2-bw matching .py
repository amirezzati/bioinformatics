import os
import numpy as np

def last_to_first(bwt_str):
    first_to_last = sorted(range(len(bwt_str)), key=lambda i: bwt_str[i]) 
    return np.argsort(first_to_last) # convet to last_to_first


def BW_matching(lastColumn, pattern, lastToFirst):
    top = 0
    bottom = len(lastColumn) - 1
    
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
            return bottom - top + 1


cwd = os.getcwd()
inputFile = open(cwd + "/rosalind_ba9l.txt", "r")
outputFile = open(cwd + '/p2_output.txt', "w")

bwt = inputFile.readline()[:-1] # remove '\n' at the end of line
patterns = inputFile.readline().split(' ')

lastToFirst = last_to_first(bwt)

outputFile.write(' '.join([str(BW_matching(bwt, pattern, lastToFirst)) for pattern in patterns]))

inputFile.close()
outputFile.close()