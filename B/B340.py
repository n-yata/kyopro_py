Q = int(input())
a = []
for i in range(Q):
    q, x = map(int, input().split())
    if 1 == q:
        a.append(x)
    else:
        ra = a[::-1]
        print(ra[x-1])
