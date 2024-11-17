m = int(input())
lst = [1]
while lst[-1] <= m:
    lst.append(lst[-1] * 3)

ans = []
i = len(lst) - 1
while m > 0:
    while m < lst[i]:
        i -= 1
    ans.append(i)
    m -= lst[i]
print(len(ans))
print(*ans)
