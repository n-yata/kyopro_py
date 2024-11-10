from itertools import permutations

S = input()
for p in permutations(S):
    if "".join(p) == "ABC":
        print("Yes")
        exit()
print("No")