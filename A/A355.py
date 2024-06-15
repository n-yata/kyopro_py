import sys

A, B = map(int, input().split())
if A == B:
    print(-1)
    sys.exit()
ab = [A, B]
for i in range(1, 4):
    if not i in ab:
        print(i)
        sys.exit()
