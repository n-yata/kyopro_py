R, G, B = map(int, input().split())
C = input()
ans = 101
if C == "Red":
    ans = min(G, B)
elif C == "Green":
    ans = min(R, B)
elif C == "Blue":
    ans = min(R, G)
print(ans)
