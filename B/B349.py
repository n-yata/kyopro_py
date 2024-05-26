import sys

s = input()
mp1 = {}
for i in s:
    if not i in mp1:
        mp1[i] = 0
    mp1[i] += 1
mp2 = {}
for k in mp1:
    v = mp1[k]
    if not v in mp2:
        mp2[v] = list()
    mp2[v].append(k)
for k in mp2:
    v = mp2[k]
    if len(v) == 2:
        continue
    print('No')
    sys.exit()
print('Yes')
