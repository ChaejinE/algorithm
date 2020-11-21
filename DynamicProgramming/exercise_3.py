"""
개미 전사
"""

n = int(input())
repo = [0] + list(map(int, input().split()))
d = [0 for i in range(n+1)]
d[1] = repo[1]
d[2] = max(repo[1], repo[2])

for i in range(3, n+1):
    d[i] = max(repo[i] + d[i-2], d[i-1])

print(d[n])
