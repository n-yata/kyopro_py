N = int(input())
mp = {}
for i in range(N):
    A, C = map(int, input().split())
    if not C in mp:
        mp[C] = A
        continue
    a1 = mp[C]
    a2 = A
    if a1 > a2:
        mp[C] = a2
ans = 0
for val in mp.values():
    if val > ans:
        ans = val
print(ans)
