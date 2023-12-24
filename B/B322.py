n,m = map(int, input().split())
s = input()
t = input()
ans = 0
if not t.startswith(s):
    ans += 2
if not t.endswith(s):
    ans += 1
print(ans)