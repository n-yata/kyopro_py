N = int(input())
S = []
maxL = 0
for i in range(N):
    s = input()
    S.append(s)
    maxL = max(maxL, len(s))

for i in range(maxL):
    out = ''
    for s in S:
        if len(s)-1 >= i:
            out += s[i]
        else:
            out += '*'
    ans = out[::-1].rstrip('*')
    print(ans)
