N = int(input())
A = list(map(int, input().split()))
place = [-1] * (N+1)
for i, a in enumerate(A):
    place[a] = i

ans = []
for i in range(N):
    if A[i] != i+1:
        targ = place[i+1]
        A[i], A[targ] = A[targ], A[i]
        place[A[targ]] = targ
        ans.append((i+1, targ+1))
print(len(ans))
for a, b in ans:
    print(a, b)
