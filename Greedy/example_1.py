"""
거스름돈
"""

# 내가 푼거
n = int(input())

count = 0
while True:
    if n % 500 == 0:
        n -= 500
        count += 1
    elif n % 100 == 0:
        n -= 100
        count += 1
    elif n % 50 == 0:
        n -= 50
        count += 1
    elif n % 10 == 0:
        n -= 10
        count += 1

    if n == 0:
        break

print(count)

# 동빛나 풀이
coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin
    n %= coin

print(count)
