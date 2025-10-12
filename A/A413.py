n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in a:
    ans += i
if ans <= m:
    print("Yes")
else:
    print("No")
