S, T = map(str, input().split())
for w in range(1, len(S)):
    for c in range(0, w):
        tmp = []
        i = c
        while i < len(S):
            tmp.append(S[i])
            i += w
        if ("".join(tmp) == T):
            print("Yes")
            exit()
print("No")
