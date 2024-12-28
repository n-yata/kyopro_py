n, d = map(int, input().split())
s = input()
cnt = 0
for c in s:
    if c == "@":
        cnt += 1
print(n - (cnt - d))
