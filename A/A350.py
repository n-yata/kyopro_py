import sys

s = input()
n = int(s[3:6])

if n == 316:
    print('No')
    sys.exit()

if 0 < n and n < 350:
    print('Yes')
else:
    print('No')
