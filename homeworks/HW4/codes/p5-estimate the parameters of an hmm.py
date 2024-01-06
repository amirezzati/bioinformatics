import os
import numpy as np

cwd = os.getcwd()
inputFile = open(cwd + "/rosalind_ba10h.txt", "r")

x = list(inputFile.readline().strip()) # emitted x
inputFile.readline() # --
alphabet = inputFile.readline().split()
alphabet_idx = {alphabet[i]:i for i in range(len(alphabet))}
inputFile.readline() # --
pi = list(inputFile.readline().strip()) # hidden path pi
inputFile.readline() # --
states = inputFile.readline().split()
states_idx = {states[i]:i for i in range(len(states))}


transition = np.zeros((len(states), len(states)))
emission = np.zeros((len(states), len(alphabet)))

# counting number of each observation in each state -> (state, observation) occurrence
count_e = {state: {alph: 0 for alph in alphabet} for state in states}
for i in range(len(x)):
    count_e[pi[i]][x[i]] += 1

for state in count_e.keys():
    count_e[state]['all'] = sum([count_e[state][alph] for alph in count_e[state].keys()])

# print(count_e)

# counting occurrence of next state for each state -> (state, next_state) occurrence
count_a = {state: {state: 0 for state in states} for state in states}
for i in range(len(x)-1):
    count_a[pi[i]][pi[i+1]] += 1

for state in count_a.keys():
    count_a[state]['all'] = sum([count_a[state][next_state] for next_state in count_a[state].keys()])

# print(count_a)


# fill the transition matrix out
for state in states:
    for next_state in states:
        transition[states_idx[state]][states_idx[next_state]] = "%.3f" % (count_a[state][next_state] / count_a[state]['all'] if count_a[state]['all'] != 0 else 1/len(states))

# fill the emission matrix out
for state in states:
    for alph in alphabet:
        emission[states_idx[state]][alphabet_idx[alph]] = "%.3f" % (count_e[state][alph] / count_e[state]['all'] if count_e[state]['all'] != 0 else 1/len(alphabet))


# print(transition)
# print(emission)

print(' '.join(states))
for i in range(transition.shape[0]):
    print(states[i], ' '.join(str(elem) for elem in transition[i]))
print('--------')
print(' '.join(alphabet))
for i in range(emission.shape[0]):
    print(states[i], ' '.join(str(elem) for elem in emission[i]))