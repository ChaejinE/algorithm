"""
효율적인 화폐구성
"""

n, m = map(int, input().split())
coins = [int(input()) for i in range(n)]

d = [10001 for _ in range(10001)]

for coin in coins:
    d[coin] = 1

for i in range(4, m+1):
    for coin in coins:
        d[i] = min(d[i], d[i-coin] + 1)

if d[m] < 10001:
    print(d[m])
else:
    print(-1)
