s = input()
ans = 1
for i in range(len(s)):
    for j in range(i+1, len(s)):
        x = s[i:j+1]
        if x == x[::-1]:
            ans = max(ans, len(x))
print(ans)