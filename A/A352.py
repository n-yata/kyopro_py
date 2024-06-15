N, X, Y, Z = map(int, input().split())
a = []
if X > Y:
    for i in range(Y, X+1):
        a.append(i)
else:
    for i in range(X, Y+1):
        a.append(i)
if Z in a:
    print("Yes")
else:
    print("No")
