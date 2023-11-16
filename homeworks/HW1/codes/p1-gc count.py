
f = open("rosalind_gc.txt", "r")

text = f.read()
DNA_strings = text.split('>')[1:] # the first index is empty string. so I removed it.


seq_names = []
seqs = []

# seperating all DNA strings from each other
for dna in DNA_strings:
    data = dna.split('\n')[:-1] # the last index is empty string. so I removed it.
    seq_names.append(data[0])
    seqs.append(''.join(data[1:]))
    
# claculate GC-Count in each DNA string
GC_counts = []
for seq in seqs:
    GC_counts.append((seq.count('G') + seq.count('C')) / len(seq) * 100)

# find maximum percentage in GC_counts
max_index = GC_counts.index(max(GC_counts))

print(seq_names[max_index])
print(GC_counts[max_index])

# print(seq_names)
# print(seqs)
# print(GC_counts)
f.close()

