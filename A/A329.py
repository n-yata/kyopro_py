s = input()
ans = ""
for i in range(len(s)):
    if(i == len(s)): ans += s[i]
    else: ans += s[i] + " "
print(ans)