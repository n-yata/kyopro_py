n = int(input())
n_div = []
ans = [1]

for i in range(1, 10):
    if n % i == 0:
        n_div.append(i)

for x in range(1, n+1):
    for y in (n_div):
        if x % int(n/y) == 0 and int(n/y) <= x:
            ans.append(str(y))
            break
    else:
        ans.append('-')

print(*ans, sep='')
