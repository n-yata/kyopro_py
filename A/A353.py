import sys

N = int(input())
HN = list(map(int, input().split()))
H1 = HN[0]
for i in range(1, N):
    if HN[i] <= H1:
        continue
    print(i+1)
    sys.exit()
print(-1)
