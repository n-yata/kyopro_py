n, m = map(int, input().split())
s = [input() for _ in range(n)]

ans = m + 10
for bit in range(1 << n):
    store = []
    for i in range(n):
        if bit >> i & 1:
            store.append(i)
    data = [0] * m
    for s_i in store:
        for j, s_j in enumerate(s[s_i]):
            if s_j == "o":
                data[j] = 1
    if data == [1] * m:
        ans = min(ans, len(store))

print(ans)
