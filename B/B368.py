n = int(input())
a = list(map(int, input().split()))
ans = 0
while True:
    ans += 1
    a.sort(reverse=True)
    a[0] -= 1
    a[1] -= 1
    cnt = 0
    for i in a:
        if i > 0:
            cnt += 1
    if 1 >= cnt:
        break
print(ans)
