import os
import numpy as np

cwd = os.getcwd()
inputFile = open(cwd + "/rosalind_ba10c.txt", "r")

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
# print(pi)
# print(x)

# path_probability in each length with each state
path_probability = [{state : {"prob" : (1.0 / len(states)) * emission[states_idx[state]][alphabet_idx[x[0]]], "prev" : None} for state in states}]

for n in range(1, len(x)):
    path_probability.append({})
    for state in states:
        prob, prev_state = max([(path_probability[n-1][prev_state]["prob"] * transition[states_idx[prev_state]][states_idx[state]], prev_state) for prev_state in states], key = lambda x: x[0])
        path_probability[n][state] = {"prob" : prob * emission[states_idx[state]][alphabet_idx[x[n]]], "prev" : prev_state}


prev, state = max([(path_probability[-1][state]["prev"], state) for state in path_probability[-1]], key=lambda x: x[0])
path = state
for i in range(len(path_probability) - 2, -1, -1):
    path = prev + path
    prev = path_probability[i][prev]["prev"]


print(path)