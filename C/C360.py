from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

dd = defaultdict(list)
for i in range(N):
    dd[A[i]].append(W[i])
ans = 0
for lst in dd.values():
    if len(lst) == 1:
        continue
    lst = sorted(lst)
    for n in range(len(lst)-1):
        ans += lst[n]
print(ans)
