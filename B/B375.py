from math import sqrt

n = int(input())
a,b = 0,0
ans = 0
for i in range(n):
    c,d = map(int, input().split())
    ans += sqrt(pow(a-c,2)+pow(b-d,2))
    a,b = c,d
c,d = 0,0
ans += sqrt(pow(a-c,2)+pow(b-d,2))
print(ans)