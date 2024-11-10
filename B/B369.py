n = int(input())
firstR = True
firstL = True
r = -1
l = -1
ans = 0
for _ in range(n):
    a, s = map(str, input().split())
    a = int(a)
    if firstR and s == "R":
        firstR = False
        r = a
        continue
    if firstL and s == "L":
        firstL = False
        l = a
        continue
    if s == "R":
        ans += abs(a - r)
        r = a
    if s == "L":
        ans += abs(a - l)
        l = a
print(ans)
