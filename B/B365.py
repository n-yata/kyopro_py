N = int(input())
A = list(map(int, input().split()))

mp = {}
for i in range(len(A)):
    mp[A[i]] = i
A.sort(reverse=True)
print(mp[A[1]] + 1)
