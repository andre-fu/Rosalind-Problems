with open("rosalind_dna.txt", "r") as myfile:
    dna = myfile.read().replace('\n', '')

def DNAcount(dna):
    A = 0
    C = 0
    G = 0
    T = 0
    for i in range(0, len(dna)):
        if (dna[i] == 'A'):
            A += 1
        if (dna[i] == 'C'):
            C += 1
        if (dna[i] == 'G'):
            G += 1
        if (dna[i] == 'T'):
            T += 1
        
    return (str(A) + " " + str(C) + " " + str(G) + " " + " " + str(T))

ret = DNAcount(dna)
print (ret) 
