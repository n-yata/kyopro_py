s_list = []
ng_row = set()
for i in range(8):
    s = input()
    s_list.append(s)
    for j in range(8):
        if s[j] == '#':
            ng_row.add(j)

ans = 0
for i in range(8):
    if '#' in s_list[i]:
         continue
    for j in range(8):
        if j in ng_row:
            continue
        ans += 1
print(ans)
        