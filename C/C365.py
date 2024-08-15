N, M = map(int, input().split())
A = list(map(int, input().split()))

MAX = 2*10**14 + 1

ok = 0
ng = MAX + 1
while ng - ok > 1:
    mid = (ng+ok)//2

    cost = 0
    for i in range(N):
        if A[i] < mid:
            cost += A[i]
        else:
            cost += mid

    if (cost <= M):
        ok = mid
    else:
        ng = mid

if (ok == MAX):
    print("infinite")
else:
    print(ok)
