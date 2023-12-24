n,s,m,l = map(int,input().split())
ans = 10**8
for a in range(101):
    for b in range(101):
        for c in range(101):
            if a*6 + b*8 + c*12 < n:
                continue
            ans = min(ans,a*s + b*m + c*l)
print(ans)