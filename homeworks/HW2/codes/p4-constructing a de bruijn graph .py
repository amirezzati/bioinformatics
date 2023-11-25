import os

cwd = os.getcwd()
input_file = open(cwd + "/rosalind_dbru.txt", "r")
outputFile = open(cwd + '/p4_output.txt', "w")


def reversed_complement(dna):
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    rc_dna = str() # reversed complement of DNA
    for i in range(len(dna)-1, -1, -1):
        rc_dna += complement_map[dna[i]]
    return rc_dna


kp_mers = input_file.read().split('\n')
kp_mers.remove('')

kp_mers_rc = [reversed_complement(s) for s in kp_mers]
kp_mers.extend(kp_mers_rc)
kp_mers = list(set(kp_mers))

for kp_mer in sorted(kp_mers):
    outputFile.write(f'({kp_mer[:-1]}, {kp_mer[1:]})\n')


input_file.close()
outputFile.close()