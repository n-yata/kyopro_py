n, m = map(int, input().split())
dic = {}
ans = list()
for i in range(m):
    a, b = map(str, input().split())
    if a not in dic and b == "M":
        dic[a] = 1
        ans.append("Yes")
        continue
    ans.append("No")
for a in ans:
    print(a)
