import os
import sys

cwd = os.getcwd()
input_file = open(cwd + "/rosalind_gasm.txt", "r")


def reversed_complement(dna):
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    rc_dna = str() # reversed complement of DNA
    for i in range(len(dna)-1, -1, -1):
        rc_dna += complement_map[dna[i]]
    return rc_dna

def flatten(dnas):
    return [kmer for dna in dnas for kmer in dna]

def find_k_meres_nodes(dnas, k):
    length = len(dnas[0])
    return [[[dna[i:i+k], dna[i+1:i+k+1]] for i in range(length-k)] for dna in dnas]


dnas = input_file.read().split('\n')
try:
    dnas.remove('')
except ValueError:
    pass

dnas_rc = [reversed_complement(s) for s in dnas]

l = len(dnas[0])


m = 0
for k in range(l-1, 1, -1):
    pair_kmer = dict(flatten(find_k_meres_nodes(dnas, k)))
    pair_kmer_rc = dict(flatten(find_k_meres_nodes(dnas_rc, k)))

    f = km = list(pair_kmer.keys())[m]
    m+=1
    superstring = ''
    while True:
        if km in pair_kmer:
            superstring += km[-1]
            km = pair_kmer.pop(km)
            if km == f:
                print(superstring)
                sys.exit()

        elif km in pair_kmer_rc:
            superstring += km[-1]
            km = pair_kmer_rc.pop(km)
            if km == f:
                print(superstring)
                sys.exit()
        else:
            break

input_file.close()