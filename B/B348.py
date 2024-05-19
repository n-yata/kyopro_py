import math

n = int(input())
a = list()
for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y))
for i in range(n):
    mp = {}
    for j in range(n):
        if i == j:
            continue
        xp = pow(a[i][0] - a[j][0], 2)
        yp = pow(a[i][1] - a[j][1], 2)
        mp[j+1] = math.sqrt(xp+yp)
    s_mp = sorted(mp.items(), key=lambda x: x[1], reverse=True)
    print(next(iter(s_mp))[0])
