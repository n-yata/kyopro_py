n = int(input())
d = list(map(int,input().split()))
cnt = 0
for i in range(1,n+1):
    x = d[i-1]
    for j in range(1,x+1):
        s = str(i)+str(j)
        fl = True
        for k in range(len(s)-1):
            if(s[k] != s[k+1]): fl = False
        if fl: cnt += 1
print(cnt)