from rna_table import *

with open('rosalind_prot.txt', 'r') as file:
    dnalist = file.read().splitlines()

rna = dnalist[0] 
print (rna)
protein_str = ''
for i in range(0, len(rna), 3):
    for key in codons:
        if rna[i:i + 3] == key:
            print (rna[i:i+3])
            print (codons[key])
            protein_str += codons[key]

print ('\n' + protein_str)