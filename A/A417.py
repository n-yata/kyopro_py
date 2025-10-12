n, a, b = map(int, input().split())
s = input()
if a != 0:
    s = s[a:]
if b != 0:
    s = s[:-b]
print(s)
