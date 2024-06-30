from collections import defaultdict

dic = defaultdict(lambda: 0)
A, B, C = map(int, input().split())
dic[A] += 1
dic[B] += 1
dic[C] += 1
if dic[5] == 2 and dic[7] == 1:
    print("YES")
else:
    print("NO")
