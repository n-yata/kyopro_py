import sys

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = A+B
C = sorted(C)
fl = False
for c in C:
    if c in A:
        if fl:
            print("Yes")
            sys.exit()
        else:
            fl = True
    else:
        fl = False
print("No")
