def is_kaibun(v):
    str_v = str(v)
    if str_v == str_v[::-1]:
        return True
    return False


N = int(input())
ans = 1
for t in range(1, 1_000_001):
    v = t**3
    if v > N:
        break
    if is_kaibun(v):
        ans = v
print(ans)
