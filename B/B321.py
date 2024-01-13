n,x = map(int, input().split())
a = list(map(int, input().split()))
a.append(-1)

for last in range(0,101):
    b = a.copy()
    b[n-1] = last
    b.sort()
    sum = 0
    for i in range(1,n-1):
        sum += b[i]
    if sum >= x:
        print(last)
        exit()
print(-1)