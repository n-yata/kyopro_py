
H = int(input())
now = 0
ans = 0
while now <= H:
    now += 1 << ans
    ans += 1
print(ans)
