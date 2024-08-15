s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())
s3, e3 = map(int, input().split())
a1 = s1 * e1 / 10
a2 = s2 * e2 / 10
a3 = s3 * e3 / 10
print(int(a1+a2+a3))
