os = {"Ocelot": 1, "Serval": 2, "Lynx": 3}
x, y = map(str, input().split())

osX = os[x]
osY = os[y]
if osX >= osY:
    print("Yes")
else:
    print("No")
