A, B, C, D = map(int, input().split())
t = B/A
a = D/C

if t > a:
    print('TAKAHASHI')
elif t < a:
    print('AOKI')
else:
    print('DRAW')
