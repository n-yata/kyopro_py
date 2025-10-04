n, s = map(int, input().split())
t = list(map(int, input().split()))
t = [0] + t
for i in range(n):
    if t[i + 1] - t[i] <= s:
        continue
    print("No")
    exit()
print("Yes")
