import sys

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(0 for _ in range(M))
for i in range(N):
    X = list(map(int, input().split()))
    for j in range(M):
        B[j] += X[j]
for i in range(M):
    if A[i] > B[i]:
        print("No")
        sys.exit()
print("Yes")
