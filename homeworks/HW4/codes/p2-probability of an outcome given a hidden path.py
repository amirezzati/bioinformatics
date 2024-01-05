import os

cwd = os.getcwd()
inputFile = open(cwd + "/rosalind_ba10b.txt", "r")

x = list(inputFile.readline().strip()) # emitted x
inputFile.readline() # --
alphabet = inputFile.readline().split()
inputFile.readline() # --
pi = list(inputFile.readline().strip()) # hidden path
inputFile.readline() # --
states = inputFile.readline().split()
inputFile.readline() # --
column_alphabet = inputFile.readline().strip().split() # column states

emission = {}
for i in range(len(states)):
    row = inputFile.readline().strip().split()
    for j in range(len(column_alphabet)):
        emission[(row[0], column_alphabet[j])] = float(row[j+1])

# print(transition)
# print(pi)
# print(x)

prob = 1
for i in range(len(pi)):
    prob *= emission[(pi[i],x[i])]

print(prob)