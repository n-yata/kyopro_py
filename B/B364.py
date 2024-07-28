H, W = map(int, input().split())
si, sj = map(int, input().split())
si -= 1
sj -= 1
C = []
for i in range(H):
    C.append(input())
X = input()

for x in X:
    if x == 'L' and sj-1 >= 0 and C[si][sj-1] != '#':
        sj -= 1
    elif x == 'R' and sj+1 <= W-1 and C[si][sj+1] != '#':
        sj += 1
    elif x == 'U' and si-1 >= 0 and C[si-1][sj] != '#':
        si -= 1
    elif x == 'D' and si+1 <= H-1 and C[si+1][sj] != '#':
        si += 1
si += 1
sj += 1
print("{} {}".format(si, sj))
