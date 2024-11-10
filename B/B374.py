s = input()
t = input()
if s == t:
    print(0)
    exit()
if len(s) >= len(t):
    for i in range(len(s)):
        if i >= len(t):
            print(i+1)
            exit()
        if s[i] == t[i]:
            continue
        print(i+1)
        exit()
else:
    for i in range(len(t)):
        if i >= len(s):
            print(i+1)
            exit()
        if t[i] == s[i]:
            continue
        print(i+1)
        exit()