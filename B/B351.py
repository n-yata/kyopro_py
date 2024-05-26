import sys

n = int(input())
a = []
b = []
for i in range(n):
    a.append(input())
for i in range(n):
    b.append(input())
for i in range(n):
    if a[i] == b[i]:
        continue
    al = a[i]
    bl = b[i]
    for j in range(n):
        if al[j] == bl[j]:
            continue
        print(i+1, j+1)
        sys.exit()
