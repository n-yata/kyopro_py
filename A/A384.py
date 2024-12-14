n, c1, c2 = map(str, input().split())
s = input()
ans = list()
for a in s:
    if a != c1:
        ans.append(c2)
    else:
        ans.append(a)
print("".join(map(str, ans)))
