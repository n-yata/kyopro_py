N = input()
s = N[0]
for i in range(1, 4):
    if s == N[i]:
        continue
    print('DIFFERENT')
    exit()
print('SAME')
