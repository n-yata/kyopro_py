from collections import *

N = int(input())
A = list(map(int, input().split()))
q = deque()
for a in A:
    q.append(a)
    while len(q) >= 2:
        r = q.pop()
        l = q.pop()
        if l == r:
            q.append(l+1)
        else:
            q.append(l)
            q.append(r)
            break
print(len(q))
