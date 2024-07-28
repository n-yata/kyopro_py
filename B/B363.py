N, T, P = map(int, input().split())
L = list(map(int, input().split()))

L.sort(reverse=True)
ans = 0
while True:
    cnt = 0
    fl = False
    for i in range(len(L)):
        if L[i] >= T:
            cnt += 1
        if cnt >= P:
            fl = True
            break
        L[i] += 1
    if fl:
        break
    ans += 1
print(ans)
