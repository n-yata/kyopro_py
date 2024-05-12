n = int(input())
mp = {}
l = list(map(int, input().split()))
for i in range(len(l)):
    mp[l[i]] = i
q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    x = mp[a]
    y = mp[b]
    if x < y:
        print(a)
    else:
        print(b)
