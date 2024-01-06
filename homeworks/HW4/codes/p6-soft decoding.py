import os
import numpy as np

cwd = os.getcwd()
inputFile = open(cwd + "/rosalind_ba10j.txt", "r")

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

def forward_prob():
    forward = np.ones((len(x), len(states)), dtype=float)

    for i in range(len(states)):
        forward[0][i] = (1.0 / len(states)) * emission[i][alphabet_idx[x[0]]]

    for k in range(1, len(x)):
        for i in range(len(states)):
            emit  = emission[i][alphabet_idx[x[k]]]
            transit = 0
            for j in range(len(states)):
                transit += transition[j][i] * forward[k-1][j]
            forward[k][i] = transit * emit
    
    return forward
    

def backward_prob():
    backward = np.ones((len(x), len(states)), dtype=float)

    for i in range(len(states)):
        backward[-1][i] = 1.0
    for i in range(1, len(x)):
        for k in range(len(states)):
            backward_k = 0
            for l in range(len(states)):
                weight  = emission[l][alphabet_idx[x[-i]]] * transition[k][l]
                backward_k += backward[-i][l] * weight
            backward[-i-1][k] = backward_k

    return backward


forward = forward_prob()
backward = backward_prob()

x_prob = 0
for i in range(len(states)):
    x_prob += forward[-1][i] # sum all states in last index of observation -> P(x)

prob_pi = np.ones((len(x), len(states)), dtype=float) # P(pi_i = k | x) = (forward * backward) / x_prob
for k in range(len(states)):
    for i in range(len(x)):
        prob_pi[i][k] = forward[i][k] * backward[i][k] / x_prob

print('      '.join(states))
for i in range(len(x)):
    print(' '.join(['%.4f' % elem for elem in prob_pi[i]]))