a, b, c = map(int, input().split())
ok = False
if a == b and a == c:
    ok = True
if a + b == c or a + c == b or b + c == a:
    ok = True
if ok:
    print("Yes")
else:
    print("No")
