H, W, N = map(int, input().split())
T = input()
S_list = []
for i in range(H):
    S_list.append(input())

ans = 0
for h in range(H):
    for w in range(W):
        now = S_list[h][w]
        nh, nw = h, w
        if now == '#':
            continue
        fl = True
        for t in T:
            if t == 'L' and nw-1 >= 0:
                nh, nw = nh, nw-1
            elif t == 'R' and nw+1 <= W-1:
                nh, nw = nh, nw+1
            elif t == 'U' and nh-1 >= 0:
                nh, nw = nh-1, nw
            elif t == 'D' and nh+1 <= H-1:
                nh, nw = nh+1, nw
            else:
                fl = False
                break
            now = S_list[nh][nw]
            if now == '#':
                fl = False
                break
        if fl:
            ans += 1
print(ans)
