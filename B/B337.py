import sys

s = input()
if 0 == len(s):
    print('Yes')
    sys.exit()

check = s[0]
for i in range(len(s)):
    if 0 == i:
        continue
    if s[i] != s[i-1]:
        check += s[i]

if check in ('ABC', 'A', 'B', 'C', 'AB', 'AC', 'BC'):
    print('Yes')
else:
    print('No')
