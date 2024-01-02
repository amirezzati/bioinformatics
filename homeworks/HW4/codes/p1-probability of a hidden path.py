import os

cwd = os.getcwd()
inputFile = open(cwd + "/rosalind_ba10a.txt", "r")

pi = list(inputFile.readline().strip()) # hidden path
inputFile.readline() # --
states = inputFile.readline().split()
inputFile.readline() # --
column_states = inputFile.readline().strip().split() # column states

transition = {}
for i in range(len(column_states)):
    row = inputFile.readline().strip().split()
    for j in range(len(column_states)):
        transition[(row[0], column_states[j])] = float(row[j+1])

# print(transition)
# print(pi)

prob = 1/len(states)
for i in range(len(pi)-1):
    prob *= transition[(pi[i],pi[i+1])]

print(prob)