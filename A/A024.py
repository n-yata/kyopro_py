A, B, C, K = map(int, input().split())
S, T = map(int, input().split())

ans = A * S + B * T
if (K <= S+T):
    ans -= (S+T) * C
print(ans)
