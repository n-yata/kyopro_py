N = int(input())
A = list(map(int, input().split()))
MOD = 10**8

A.sort()
cnt = 0
for i in range(N-1):
    l = i
    r = N
    while r-l > 1:
        m = (l+r)//2
        if (A[m]+A[i] >= MOD):
            r = m
        else:
            l = m
    cnt += N-r

print(sum(A)*(N-1)-(cnt*MOD))
