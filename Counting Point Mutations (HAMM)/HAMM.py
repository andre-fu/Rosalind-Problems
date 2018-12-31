with open('rosalind_hamm.txt', 'r') as file:
    dnalist = file.readlines()

for i in range(0, len(dnalist)):
    s = dnalist[0]
    t = dnalist[1]

k = 0
for i in range(0, len(s)):
    if (s[i] != t[i]):
        k = k +1
    else:
        pass

print (k)