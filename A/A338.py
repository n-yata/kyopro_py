import sys

s = input()
s1 = s[0]
if (s1.islower()):
    print('No')
    sys.exit()
s2 = s[1:]
fl = True
for c in s2:
    if (c.isupper()):
        fl = False
        break
if (fl):
    print('Yes')
else:
    print('No')
