S = input()
N = int(input())
cnt = 0
for i in range(len(S)):
    for j in range(len(S)):
        cnt += 1
        if cnt != N:
            continue
        print(S[i] + S[j])
        exit()
