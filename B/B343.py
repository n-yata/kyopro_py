n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(len(a)):
        if 1 == a[j]:
            print(j+1, end=' ')
    print()
