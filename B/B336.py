n = int(input())
b = bin(n)
ans = 0
for i in b[::-1]:
    if ('1' == i):
        break
    ans += 1
print(ans)
