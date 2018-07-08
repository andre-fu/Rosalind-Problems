#with open('FILE_NAME', 'r') as fasta:



name, seq = None, []
for line in fasta:
    line = line.rstrip()
    if line.startswith('>'):
        if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

