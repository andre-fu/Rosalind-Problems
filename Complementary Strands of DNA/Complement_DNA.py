with open('rosalind_revc.txt', 'r') as file:
    ssdna = file.read().replace('\n', '')

idx = 0

print ssdna[idx]

cdna = '
while (idx <= len(ssdna)) :
    try:
        if (ssdna[idx] == 'A'):
            cdna  += 'T'
        if (ssdna[idx] == 'C'):
            cdna += 'G'
        if (ssdna[idx] == 'T'):
            cdna += 'A'
        if (ssdna[idx] == 'G'):
            cdna += 'C'
    except:
        pass
    idx += 1

cdna = cdna[::-1]

print cdna