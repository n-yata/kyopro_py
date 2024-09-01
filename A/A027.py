from collections import defaultdict

l1, l2, l3 = map(int, input().split())
dic = defaultdict(int)

dic[l1] += 1
dic[l2] += 1
dic[l3] += 1

for k, v in dic.items():
    if v == 2:
        continue
    print(k)
    exit()
