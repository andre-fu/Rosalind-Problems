inds = []


with open('rosalind_subs.txt', 'r') as file:
        dnalist = file.readlines()
        
for i in range(0, len(dnalist)):
    s = dnalist[0] #string
    t = dnalist[1] #substringfor i in xrange(len(s)-len(t)+1):

for i in range(len(s)-len(t)+1):
    if s[i:i+len(t)] == t:
        inds.append(i+1)
for i in inds:
    print (i)
