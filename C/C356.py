N, M, K = map(int, input().split())
AA = []
R = []
for i in range(M):
    CAR = list(map(str, input().split()))
    AA.append(list(map(int, CAR[1:-1])))
    R.append(True if CAR[-1] == "o" else False)

ans = 0
for i in range(1 << N):
    ok = True
    for j in range(M):
        col = 0
        for a in AA[j]:
            if (i & (1 << (a-1))):
                col += 1
        if ((R[j]) != (col >= K)):
            ok = False
    if (ok):
        ans += 1

print(ans)
