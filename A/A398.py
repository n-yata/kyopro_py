n = int(input())
half = int(n / 2)
if n % 2 == 0:
    print(("-" * (half - 1)) + "==" + ("-" * (half - 1)))
else:
    print(("-" * half) + "=" + ("-" * half))
