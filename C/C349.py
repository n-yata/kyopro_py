S = input()
T = input().lower()

flag = 0
i = 0
for s_i in S:
    if s_i == T[i]:
        i += 1
    if i >= 3:
        break

print("Yes" if i >= 3 or i == 2 and T[-1] == "x" else "No")
