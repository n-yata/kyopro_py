import string

N = int(input())
S = input()

dic = {ch: ch for ch in string.ascii_lowercase}
Q = int(input())
for _ in range(Q):
    c, d = input().split()
    for ch in string.ascii_lowercase:
        if dic[ch] == c:
            dic[ch] = d
ans_lst = [dic[s] for s in S]
print(*ans_lst, sep='')
