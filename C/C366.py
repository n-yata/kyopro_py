s = set()
d = [0] * (10**6 + 10)
for _ in range(int(input())):
    com = list(map(int, input().split()))
    if com[0] == 1:
        x = com[1]
        s.add(x)
        d[x] += 1
    elif com[0] == 2:
        x = com[1]
        d[x] -= 1
        if d[x] <= 0:
            s.discard(x)
    else:
        print(len(s))
