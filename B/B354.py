N = int(input())
S = []
T = 0
for i in range(N):
    s, c = map(str, input().split())
    S.append(s)
    T += int(c)
S = sorted(S)
print(S[T % N])
