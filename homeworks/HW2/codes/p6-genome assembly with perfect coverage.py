import os

cwd = os.getcwd()
input_file = open(cwd + "/rosalind_pcov.txt", "r")


dnas = input_file.read().split('\n')
try:
    dnas.remove('')
except ValueError:
    pass


pair_kmer = dict([(dna[:-1], dna[1:]) for dna in dnas])

k = list(pair_kmer.keys())[0]
superstring = ''
while len(superstring) < len(dnas):
    superstring += pair_kmer[k][-1]
    k = pair_kmer[k]
print(superstring)