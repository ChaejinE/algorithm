"""
1 로 만들기
"""

num = int(input())

count = 0
d = [0 for _ in range(30001)]

for i in range(2, num+1):
    d[i] = d[i-1] + 1
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)

print(d[1:num])
print('result', d[num])
