h, w, x, y = map(int, input().split())
s = list()
for i in range(h):
    s.append(list(input()))
t = input()

ans = 0
x -= 1
y -= 1
for c in t:
    if c == "U" and s[x - 1][y] != "#":
        if s[x - 1][y] == "@":
            ans += 1
            s[x - 1][y] = "."
        x -= 1
    elif c == "D" and s[x + 1][y] != "#":
        if s[x + 1][y] == "@":
            ans += 1
            s[x + 1][y] = "."
        x += 1
    elif c == "L" and s[x][y - 1] != "#":
        if s[x][y - 1] == "@":
            ans += 1
            s[x][y - 1] = "."
        y -= 1
    elif c == "R" and s[x][y + 1] != "#":
        if s[x][y + 1] == "@":
            ans += 1
            s[x][y + 1] = "."
        y += 1
print("{} {} {}".format(x + 1, y + 1, ans))
