a,b,c = map(int,input().split())
fl = False;
if a+b == c:
    fl = True
if a+c == b:
    fl = True
if b+c == a:
    fl = True
if fl: print('Yes')
else: print('No')