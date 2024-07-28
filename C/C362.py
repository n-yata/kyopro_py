N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

mi = 0
ma = 0
for i in range(N):
    l, r = LR[i]
    mi += l
    ma += r

if (mi <= 0 <= ma):
    print("Yes")
    level = ma
    ans = []
    for i in range(N):
        l, r = LR[i]
        d = r-l
        tmp = None
        if (d < level):
            tmp = l
            level -= d
        else:
            tmp = r-level
            level = 0
        ans.append(tmp)
    print(*ans)
else:
    print("No")
