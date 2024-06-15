S = input()
u, l = 0, 0
for i in range(len(S)):
    if S[i].isupper():
        u += 1
    else:
        l += 1
if u > l:
    print(S.upper())
else:
    print(S.lower())
