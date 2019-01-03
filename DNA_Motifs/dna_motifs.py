with open('rosalind_subs.txt', 'r') as file:
    dnalist = file.read().splitlines()


s = dnalist[0] #string
t = dnalist[1] #substring

print (s)
#print (t)
print (s[0:0+len(t)] )
print (t)
indices = []

for i in range(len(s)-len(t)+1):
    print (s[i:i+len(t)])
    if s[i:i+len(t) ] == t:
        print('here')
        indices.append(i+1)

for i in indices:
    print (i)

#print('done')