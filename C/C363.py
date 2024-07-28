import more_itertools

N, K = map(int, input().split())
S = input()

ans = 0
for s in more_itertools.distinct_permutations(S):
    fl = True
    for i in range(len(s)-K+1):
        sl_s = s[i:i+K]
        sl_sr = sl_s[::-1]
        if sl_s == sl_sr:
            fl = False
            break
    if fl:
        ans += 1
print(ans)
