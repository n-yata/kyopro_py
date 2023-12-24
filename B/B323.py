n = int(input())
mp = {}
for i in range(n):
    mp[i+1] = 0
    s = input()
    for j in range(len(s)):
        if 'o' == s[j]:
            mp[i+1] += 1
cnt_mp = {}
for i in mp:
    if mp[i] not in cnt_mp:
        cnt_mp[mp[i]] = list()
    cnt_mp[mp[i]].append(i)
sort_list = sorted(cnt_mp, reverse=True)
ans_list = list()
for i in sort_list:
    for j in range(len(cnt_mp[i])):
        ans_list.append(cnt_mp[i][j])
print(*ans_list)