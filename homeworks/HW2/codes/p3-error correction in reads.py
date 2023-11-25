import os
from Bio import SeqIO
from collections import Counter

cwd = os.getcwd()
input_file = open(cwd + "/rosalind_corr.txt", "r")
outputFile = open(cwd + '/p3_output.txt', "w")

seqs, seq_names = [], []
for seq_record in SeqIO.parse(input_file, "fasta"):
    seq_names.append(seq_record.name)
    seqs.append(str(seq_record.seq))

# print(seqs)


def reversed_complement(dna):
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    rc_dna = str() # reversed complement of DNA
    for i in range(len(dna)-1, -1, -1):
        rc_dna += complement_map[dna[i]]
    return rc_dna

def hamming_distance(s1, s2):
    return sum([int(a != b) for a, b in zip(s1, s2)])


c = Counter()
for seq in seqs:   
    seq_rc = reversed_complement(seq)
    if seq_rc in c:
        c[seq_rc] += 1
    else:
        c[seq] += 1

corrects, incorrects = [], []
for seq, count in c.items():
    if count >= 2:
        corrects.append(seq)
    else:
        incorrects.append(seq)


for incorrect in incorrects:
    for correct in corrects:
        if hamming_distance(incorrect, correct) == 1:
            outputFile.write(f'{incorrect}->{correct}\n')
            break
        elif hamming_distance(incorrect, reversed_complement(correct)) == 1:
            outputFile.write(f'{incorrect}->{reversed_complement(correct)}\n')
            break


input_file.close()
outputFile.close()