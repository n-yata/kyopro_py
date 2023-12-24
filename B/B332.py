k,g,m = map(int,input().split())
x = 0
y = 0
for i in range(k):
    if g == x:
        x = 0
        continue
    elif y == 0:
        y = m
        continue
    z = min(g-x,y)
    x += z
    y -= z
print('{} {}'.format(x,y))
