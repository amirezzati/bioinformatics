import os
import numpy as np

cwd = os.getcwd()
inputFile = open(cwd + "/rosalind_ba10d.txt", "r")

x = list(inputFile.readline().strip()) # emitted x
inputFile.readline() # --
alphabet = inputFile.readline().split()
alphabet_idx = {alphabet[i]:i for i in range(len(alphabet))}
inputFile.readline() # --
states = inputFile.readline().split()
states_idx = {states[i]:i for i in range(len(states))}
inputFile.readline() # --
column_states = inputFile.readline().strip().split() # column states

transition = np.zeros((len(states), len(states)))
for i in range(len(column_states)):
    transition[i, :] = [float(i) for i in inputFile.readline().strip().split()[1:]]

inputFile.readline() # --
column_alphabet = inputFile.readline().strip().split() # column alphabet

emission = np.zeros((len(states), len(column_alphabet)))
for i in range(len(states)):
    emission[i, :] = [float(i) for i in inputFile.readline().strip().split()[1:]]


# print(transition)
# print(emission)
# print(x)

# path_probability in each length with each state
probability = []
# add probability for length 1 (X[0])
probability.append({state : (1.0 / len(states)) * emission[states_idx[state]][alphabet_idx[x[0]]] for state in states})

for n in range(1, len(x)):
    probability.append({})

    for state in states:
        probability[n][state] = 0
        for prev in states: # over all states in previous observation X[n-1]
            probability[n][state] += probability[n-1][prev] *\
                                    transition[states_idx[prev]][states_idx[state]] *\
                                    emission[states_idx[state]][alphabet_idx[x[n]]]

x_prob = 0
for state in states:
    x_prob += probability[len(x)-1][state]

print(x_prob)