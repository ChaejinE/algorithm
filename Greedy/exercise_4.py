"""
1이 될 때까지
"""
n, k = map(int, input().split())

count = n % k

while True:
    n //= k
    count += 1

    if n == 1:
        break

print(count)
