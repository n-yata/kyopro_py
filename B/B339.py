mp = {'u': 'r', 'r': 'd', 'd': 'l', 'l': 'u'}
mp_r = {'u': 'l', 'l': 'd', 'd': 'r', 'r': 'u'}

h, w, n = map(int, input().split())
matrix = []
for i in range(h):
    row = []
    for j in range(w):
        row.append('.')
    matrix.append(row)
nowI = 0
nowJ = 0
nowD = 'u'
for i in range(n):
    if '.' == matrix[nowI][nowJ]:
        matrix[nowI][nowJ] = '#'
        nowD = mp[nowD]
    else:
        matrix[nowI][nowJ] = '.'
        nowD = mp_r[nowD]

    if 'u' == nowD:
        nowI = nowI - 1 if 0 <= (nowI - 1) else h-1
    elif 'd' == nowD:
        nowI = (nowI + 1) % h
    elif 'l' == nowD:
        nowJ = nowJ - 1 if 0 <= (nowJ - 1) else w-1
    elif 'r' == nowD:
        nowJ = (nowJ + 1) % w

for i in range(h):
    for j in range(w):
        print(matrix[i][j], end="")
    print()
