S = input()
T = input()

ans = []
nowT = 0
for i in range(len(S)):
    for j in range(nowT, len(T)):
        if S[i] != T[j]:
            continue
        ans.append(j+1)
        nowT = j+1
        break
print(*ans)
