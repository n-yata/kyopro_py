S = input()
N = int(S)
fl = False
if '3' in S:
    fl = True
if N % 3 == 0:
    fl = True

print("YES" if fl else "NO")
