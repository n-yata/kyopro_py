N = int(input())
flag = False
flag2 = False
ans = "Yes"
for i in range(N):
    s = input()
    if flag2:
        ans = "No"
    elif s == "sweet":
        if flag:
            flag2 = True
        else:
            flag = True
    else:
        flag = False
print(ans)
