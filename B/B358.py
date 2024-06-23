N, A = map(int, input().split())
T = list(map(int, input().split()))
sec = 0
idx = 0
while idx <= N-1:
    if sec >= T[idx]:
        sec += A
        idx += 1
        print(sec)
        continue
    sec += 1
