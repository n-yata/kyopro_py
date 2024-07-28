import math

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

AB2 = (x2 - x1)**2 + (y2 - y1)**2
BC2 = (x3 - x2)**2 + (y3 - y2)**2
CA2 = (x3 - x1)**2 + (y3 - y1)**2

if math.isclose(AB2+BC2, CA2) or math.isclose(AB2+CA2, BC2) or math.isclose(BC2 + CA2, AB2):
    print('Yes')
else:
    print('No')
