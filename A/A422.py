x, y = map(int, input().split("-"))
if y == 8:
    print(x + 1, "-", 1, sep="")
else:
    print(x, "-", y + 1, sep="")
