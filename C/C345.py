from collections import defaultdict

S = input()

count_dic = defaultdict(int)
diff, same = 0, 0
for j, ch in enumerate(S):
    diff += j-count_dic[ch]
    same += count_dic[ch]
    count_dic[ch] += 1

if same > 0:
    ans = diff+1
    print(ans)
else:
    print(diff)
