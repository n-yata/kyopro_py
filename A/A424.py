a, b, c = map(int, input().split())
if a + b <= c or b + c <= a or c + a <= b:
    print("No")
    exit()

if a == b or b == c or c == a:
    print("Yes")
else:
    print("No")
