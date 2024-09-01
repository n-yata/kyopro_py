N = int(input())

if N <= 59:
    print('Bad')
elif 60 <= N and N <= 89:
    print('Good')
elif 89 <= N and N <= 99:
    print('Great')
else:
    print('Perfect')
