x, y = map(int, input().split())
ans = x + y
if ans > 12:
    ans -= 12
print(ans)
