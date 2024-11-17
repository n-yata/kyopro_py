N = int(input())
QR = []
for i in range(N):
    QR.append(list(map(int, input().split())))

Q = int(input())
for i in range(Q):
    t, d = map(int, input().split())
    q, r = QR[t - 1]

    amari = d % q
    if amari == r:
        print(d)
    else:
        N = d // q
        if amari > r:
            N += 1

        print(N * q + r)
