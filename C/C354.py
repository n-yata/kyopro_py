N, T = map(int, input().split())
A = list(map(int, input().split()))

X = [set() for i in range(N)]
Y = [set() for i in range(N)]
TL = set()
TR = set()


def judge(se, a, t):
    se.add(a)
    if (len(se) == N):
        print(t+1)
        exit()


for i in range(T):
    a = A[i] - 1
    di, mo = divmod(a, N)
    judge(Y[di], a, i)
    judge(X[mo], a, i)
    if (a % (N+1) == 0):
        judge(TL, a, i)
    if (a % (N-1) == 0 and 1 <= a < (N**2)-1):
        judge(TR, a, i)
print(-1)
