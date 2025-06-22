n = int(input())
s = input()
parts = s.split("/")
if len(parts) != 2:
    print("No")
    exit()
if parts[0] != "" and parts[0].count("1") == 0:
    print("No")
    exit()
if parts[1] != "" and parts[1].count("2") == 0:
    print("No")
    exit()
if len(parts[0]) == len(parts[1]):
    print("Yes")
else:
    print("No")
