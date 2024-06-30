N, K = map(int, input().split())
A = list(map(int, input().split()))

gray = set()
for a in A:
    if 1 <= a <= K:
        gray.add(a)
ans = K * (K+1) // 2 - sum(gray)
print(ans)
