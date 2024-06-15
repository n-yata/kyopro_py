N, L, R = map(int, input().split())
A = []
for i in range(1, L):
    A.append(i)
r = []
for i in range(L, R+1):
    r.append(i)
A += r[::-1]
for i in range(R+1, N+1):
    A.append(i)
print(*A)
