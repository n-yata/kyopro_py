s = input()
mp = {}
for c in s:
    if c not in mp:
        mp[c] = 0
    mp[c] = mp[c]+1
maxI = max(mp.values())
l = []
for k, v in mp.items():
    if not v == maxI:
        continue
    l.append(k)
sort_l = sorted(l)
print(sort_l[0])
