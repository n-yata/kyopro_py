a, m, l, r = map(int, input().split())
left = (l-a)//m
if (l-a) % m != 0:
    left += 1
right = (r-a)//m
print(right-left+1)
