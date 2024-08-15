N, T, A = map(int, input().split())
zan = N-(A+T)
if A > T+zan or T > A+zan:
    print('Yes')
else:
    print('No')
