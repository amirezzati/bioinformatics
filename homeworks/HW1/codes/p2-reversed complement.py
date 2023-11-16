DNA = 'AGGTTATACCCAGCCCCAGCTAATGCGTCCCTGCGAGGCGCCCTGTTATTACGACTTCGCTTAACCTGGAATAAGACGGGTGTCTCAAGACGAACTCTCCATTTAAGTTGTTTGTGTCAGTTCGGGTAAAAAGCGTATTACAGAAATGTACGTTCGTAGCGTCGCTGCTTTTCGGTATCATTCTCGGGATTGAGCTATCCACAGAACCATACGACGGATGAGCGCACACTCATATCAAGGGTCTGCGGTGGACCCCTCGCGTCGAAGTGTATCTCATCCAATGCAGGTCGGCCAGGGAGGGCGGAAAACCCGCCCGTCACTCGGCGCACTGGGAACTTGCATAACAGACCAGTCCACTCCGCAGACGATGTTTACAACCGACAAATTAACAATGGAGGCGGTTCACTGAATGTAGCTAATCGCTACACATTACTTGCAGCTAGGGTGTGTTGGCTGGAGGTATTAAGGGGAAATCGTTCCTAGCAATATAACAGGAAACGTATGACACCTACGTACAGACTTTGCAGTCGGCCTCCTCACTGCGACCGTTCTCCAGTCACCGGTAATCACTGGCCCTTTACCTTTTTCCGGTCCCTGCGCGTGTGCGACACCAGGGGCTTCTCCTGCCAACCCACCGCGGCAAGGTTTGTATAGCCACCTTACCTGGCCCATAGGCTGAAGCCTGGAAAAGGTGCCAAGGCCGGCATATATACCGCCTCGGGGGTCACTTGGTGCAGGGTATAGCACTTCATTTGGCGCGATAGCAACCGGTCTTCTTTACGGTCACGGCAGTCAAAATCGCCTGCGGAGAATTACTTGAGAGGTGGCATCTGCAGATAGTTGAATGCGTTTGGACGGACACGGGTGCGAAGAATTGTTATTTACAACATCTCATATCCCATTCACGACAGCTCGTATCCGCCTAGGCTCTTTGCCGATGTTGACCACACTACAGATGAGCCCTATCACT'

complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

rc_DNA = str() # reversed complement of DNA
for i in range(len(DNA)-1, -1, -1):
    rc_DNA += complement_map[DNA[i]]

print(rc_DNA)