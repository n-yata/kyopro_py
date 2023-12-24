b = int(input())
cnt = 1
fl = True
while True:
    n = cnt**cnt
    if b < n: break
    if b == n:
        print(cnt)
        fl = False
        break
    cnt += 1
if fl: print(-1)