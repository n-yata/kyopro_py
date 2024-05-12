mp = {
    1: ['AB', 'BC', 'CD', 'DE', 'EA', 'BA', 'CB', 'DC', 'ED', 'AE'],
    2: ['AC', 'BD', 'CE', 'DA', 'EB', 'CA', 'DB', 'EC', 'AD', 'BE']
}

s = input()
t = input()
slen = 0
tlen = 0

for key, value in mp.items():
    if s in value:
        slen = key
    if t in value:
        tlen = key

if slen == tlen:
    print('Yes')
else:
    print('No')
