N = int(input())
P = []
idx = -1
max_diff = -1
for i in range(N):
    a, b = map(int, input().split())
    P.append((a, b))
    if b-a > max_diff:
        max_diff = b-a
        idx = i
ans = 0
for i in range(N):
    if i == idx:
        ans += P[i][1]
    else:
        ans += P[i][0]
print(ans)
