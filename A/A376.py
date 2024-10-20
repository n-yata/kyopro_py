N, C = map(int, input().split())
T = list(map(int, input().split()))
ans = 0
before = -10000
for i in range(N):
    if T[i]-before >= C:
        before = T[i]
        ans += 1
print(ans)