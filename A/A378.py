a = list(map(int, input().split()))
dic = {}
for i in a:
    if not i in dic:
        dic[i] = 0
    dic[i] += 1
ans = 0
for v in dic.values():
    if v == 2 or v == 3:
        ans += 1
    elif v == 4:
        ans += 2
print(ans)
