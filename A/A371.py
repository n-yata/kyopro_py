s = list(input().split())
if s[0] == s[1] == "<":
    print("BC"[s[2] == ">"])
elif s[0] == s[1] == ">":
    print("BC"[s[2] == "<"])
else:
    print("A")