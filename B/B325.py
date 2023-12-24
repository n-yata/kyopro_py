n = int(input())
z = list()
for i in range(n):
    w,x = map(int,input().split())
    z.append((w,x))
ans = 0
for i in range(24):
    sum = 0
    for j in range(n):
        x = (z[j][1] + i)%24
        if x < 9 or 18 <= x:
            continue
        sum += z[j][0]
    ans = max(ans,sum)
print(ans)