n, q = map(int, input().split())
hole = []
for i in range(n):
    hole.append(True)
t = map(int, input().split())
for i in t:
    hole[i-1] = not hole[i-1]
ans = 0
for i in hole:
    if i:
        ans += 1
print(ans)
