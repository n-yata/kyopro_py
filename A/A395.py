n = int(input())
l = list(map(int, input().split()))

ans = True
before = l[0]
for i in range(1, len(l)):
    if before >= l[i]:
        ans = False
        break
    before = l[i]
if ans:
    print("Yes")
else:
    print("No")
