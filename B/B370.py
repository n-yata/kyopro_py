n = int(input())
a = list()
for i in range(n):
    aa = list(map(int, input().split()))
    a.append(aa)
j = 0
for i in range(n):
    if i >= j:
        j = a[i][j] - 1
    else:
        j = a[j][i] - 1
print(j + 1)
