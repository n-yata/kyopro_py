n = int(input())
s = input()
fl = 0
for i in range(n-1):
    if(s[i] == 'a' and s[i+1] == 'b'):
        fl = 1
        break
    if(s[i] == 'b' and s[i+1] == 'a'):
        fl = 1
        break
print("Yes" if fl else "No")