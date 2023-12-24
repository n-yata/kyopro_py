n = int(input())
while(True):
    s = str(n)
    x = int(s[0])
    y = int(s[1])
    z = int(s[2])
    if(x*y == z):
        print(s)
        break
    n += 1