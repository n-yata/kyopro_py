dic = {}
abc = "BCDEFGHIJKLMNOPQRSTUVWXYZ"
s = input()
for i in range(26):
    dic[s[i]] = i

ans = 0
now = dic["A"]
for a in abc:
    ans += abs(now - dic[a])
    now = dic[a]
print(ans)
