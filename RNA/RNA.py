with open('rosalind_rna.txt', 'r') as file:
    dna = file.read().replace('\n','')

rna = dna.replace('T','U')

print rna
