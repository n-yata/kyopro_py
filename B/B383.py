def calc(a, b, x, y):
    res = 0
    for i, s_i in enumerate(s):
        for j, s_ij in enumerate(s_i):
            if s_ij == "." and (
                abs(a - i) + abs(b - j) <= d or abs(x - i) + abs(y - j) <= d
            ):
                res += 1
    return res


h, w, d = map(int, input().split())
s = [input() for _ in range(h)]
ans = 0
for x1 in range(h):
    for y1 in range(w):
        if s[x1][y1] == "#":
            continue
        for x2 in range(h):
            for y2 in range(w):
                if (x1, y1) == (x2, y2) or s[x2][y2] == "#":
                    continue
                ans = max(ans, calc(x1, y1, x2, y2))
print(ans)
