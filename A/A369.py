a = list(map(int, input().split()))
a.sort()
if a[1] - a[0] == 0:
    print(1)
elif (a[1] - a[0]) % 2 == 0:
    print(3)
else:
    print(2)