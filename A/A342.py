s = input()
mp = {}
for i in range(len(s)):
    if not s[i] in mp:
        mp[s[i]] = []
    mp[s[i]].append(i)
for i in mp.keys():
    if len(mp[i]) != 1:
        continue
    print(mp[i][0]+1)
