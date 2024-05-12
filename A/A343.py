a, b = map(int, input().split())
c = a+b
for i in range(0, 10):
    if c != i:
        print(i)
        break
