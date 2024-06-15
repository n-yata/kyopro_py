
N, K = map(int, input().split())
A = list(map(int, input().split()))

empty_sheets = K
start_count = 0

for a in A:
    if empty_sheets < a:
        start_count += 1
        empty_sheets = K
    empty_sheets -= a

start_count += 1
print(start_count)
