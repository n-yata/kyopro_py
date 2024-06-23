N = int(input())
K = int(input())
X = int(input())
Y = int(input())
nk = N-K
if nk <= 0:
    print(X*N)
    exit()
ans = X*K
ans += Y*nk
print(ans)
