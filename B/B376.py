def move(now, to, arr, other):
    res = 0
    while True:
        res += 1
        now += arr
        if now == n + 1:
            now = 1
        if now == 0:
            now = n

        if now == to:
            return res
        if now == other:
            return -1


n, q = map(int, input().split())

ans = 0
l, r = 1, 2
for _ in range(q):
    h, t_ = input().split()
    t = int(t_)
    if h == "R":
        if r == t:
            continue
        d_i = move(r, t, 1, l)
        if d_i >= 0:
            ans += d_i
        else:
            d_j = move(r, t, -1, l)
            ans += d_j
        r = t
    else:
        if l == t:
            continue
        d_i = move(l, t, 1, r)
        if d_i >= 0:
            ans += d_i
        else:
            d_j = move(l, t, -1, r)
            ans += d_j
        l = t

print(ans)
