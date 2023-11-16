import os
from Bio.Align import substitution_matrices
from itertools import product

cwd = os.getcwd()
f = open(cwd + "/test.txt", "r")

text = f.read()
DNA_strings = text.split('>')[1:] # the first index is empty string. so I removed it.

seqs = []
for dna in DNA_strings:
    data = dna.split('\n')
    seqs.append(''.join(data[1:]))

seq1 = seqs[0]
seq2 = seqs[1]

pam250 = substitution_matrices.load("PAM250")
# print(pam250)


def get_local_alignment(s, t):
    sl, tl = len(s), len(t)
    m = {(0, 0): (0, None)}
    m.update({((i, 0), (i * - 5, (i-1, 0))) for i in range(1, sl+1)})
    m.update({((0, i), (i * - 5, (0, i-1))) for i in range(1, tl+1)})
    for i, j in product(range(1, sl+1), range(1, tl+1)):
        cost = pam250.get((s[i-1], t[j-1]))
        if cost == None:
            cost = pam250.get((t[j-1], s[i-1]))

        d = m[(i-1, j-1)][0] + cost
        l = m[(i-1, j)][0] - 5
        u = m[(i, j-1)][0] - 5
        z = 0
        b = max(d, l, u, z)
        
        if d == b:
            m[(i, j)] = (b, (i-1, j-1))
        elif l == b:
            m[(i, j)] = (b, (i-1, j))
        elif u == b:
            m[(i, j)] = (b, (i, j-1))
        elif z == b:
            m[(i, j)] = (b, None)

    c, v = max(m.items(), key=lambda x: x[1][0])
    
    # print(m)
    print(v[0])
    sa = ''
    ta = ''
    while m[c][1] is not None:
        i, j = c
        c = m[c][1]
        # print(m[c])
        if i-1 == c[0] and j-1 == c[1]:
            sa += s[i-1]
            ta += t[j-1]
        elif i == c[0]:
            ta += t[j-1]
        elif j == c[1]:
            sa += s[i-1]

    print(''.join(reversed(sa)))
    print(''.join(reversed(ta)))

get_local_alignment(seq1, seq2)

f.close()