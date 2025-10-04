alf = "abcdefghijklmnopqrstuvwxyz"
s = input()
for a in alf:
    if a not in s:
        print(a)
        exit()
