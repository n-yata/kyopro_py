from collections import defaultdict

a, b, c, d = map(str, input().split())
mp = defaultdict(int)
mp[a] += 1
mp[b] += 1
mp[c] += 1
mp[d] += 1
a = list()
for v in mp.values():
    a.append(v)
if (a[0] == 1 and a[1] == 3) or (a[0] == 2 and a[1] == 2) or (a[0] == 3 and a[1] == 1):
    print("Yes")
else:
    print("No")
