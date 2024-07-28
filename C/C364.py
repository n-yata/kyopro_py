N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

cntA = 0
sumA = 0
for a in A:
    sumA += a
    cntA += 1
    if sumA > X:
        break
cntB = 0
sumB = 0
for b in B:
    sumB += b
    cntB += 1
    if sumB > Y:
        break
print(min(cntA, cntB))
