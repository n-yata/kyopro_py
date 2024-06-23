N, A, B = map(int, input().split())
D = list(map(int, input().split()))
d_set = set()
for d in D:
    d_set.add(d % (A+B))
d_list = list(sorted(d_set))

if len(d_list) == 1:
    print("Yes")
    exit()

for i in range(len(d_list)):
    d1 = d_list[i]
    d2 = d_list[(i+1) % len(d_list)]
    if (d2 - d1) % (A+B) > B:
        print("Yes")
        exit()
print("No")
