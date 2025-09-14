a = list(map(int, input().split()))

for i in range(4):
    b = [i for i in range(1, 6)]
    b[i], b[i + 1] = b[i + 1], b[i]
    if a == b:
        exit(print("Yes"))
print("No")
