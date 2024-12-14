n = int(input())
ans = 0
nowT = 0
dic = {}
lasT = 0
for i in range(n):
    t, v = map(int, input().split())
    dic[t] = v
    if i == n - 1:
        lasT = t
for i in range(1, lasT + 1):
    nowT = 0
    if ans != 0:
        ans -= 1
    if i in dic:
        ans += dic[i]
print(ans)
