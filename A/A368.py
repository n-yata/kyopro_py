N, K = map(int, input().split())
A = list(map(int, input().split()))
for i in range(K):
    a = A.pop()
    A.insert(0, a)
print(*A)
