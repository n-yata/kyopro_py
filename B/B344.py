a = []
while True:
    x = int(input())
    if 0 == x:
        a.append(x)
        break
    a.append(x)
ra = a[::-1]
for i in ra:
    print(i)
