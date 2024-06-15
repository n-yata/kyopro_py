N, M = map(int, input().split())
H = list(map(int, input().split()))
ans = 0
for i in range(N):
    M -= H[i]
    if 0 > M:
        break
    ans += 1
print(ans)
