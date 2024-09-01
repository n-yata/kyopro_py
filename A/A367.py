A, B, C = map(int, input().split())
if C < B:
    C += 24

l = list()
for i in range(B, C+1):
    l.append(i % 24)

if A in l:
    print('No')
else:
    print('Yes')
