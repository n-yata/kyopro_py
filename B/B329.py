n = int(input())
a = set(map(int,input().split()))
ans = sorted(list(a))
print(ans[-2])