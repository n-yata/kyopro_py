n, d = map(int, input().split())
s = list(input())
l = list()
for i in range(n):
    if s[i] == "@":
        l.append(i)
for i in range(d):
    s[l.pop()] = "."
print("".join(s))
