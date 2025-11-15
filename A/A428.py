s, a, b, x = map(int, input().split())

cycle = a + b
full = x // cycle
remain = x % cycle

distance = s * (a * full + min(remain, a))
print(distance)
