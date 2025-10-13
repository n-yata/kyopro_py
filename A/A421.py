n = int(input())
l = []
for i in range(n):
    l.append(input())
x, y = input().split()
x = int(x)
a = l[x - 1]
if a == y:
    print("Yes")
else:
    print("No")
