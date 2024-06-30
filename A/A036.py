A, B = map(int, input().split())
ans = B//A
if B % A != 0:
    ans += 1
print(ans)
