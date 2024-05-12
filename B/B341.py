n = int(input())
a = list(map(int, input().split()))
for i in range(n-1):
    s, t = map(int, input().split())
    if a[i] < s:
        continue
    x = (a[i]//s)*t
    a[i+1] += x
print(a[n-1])
