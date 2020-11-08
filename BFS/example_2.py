"""
미로 탈출
"""
from collections import deque
import time

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0

dxdy = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def bfs(x, y):
    q = deque([])
    q.append((x, y))
    while q:
        x, y = q.popleft()
        print(x, y)
        for _dx, _dy in dxdy:
            nx = x + _dx
            ny = y + _dy
            if not(0 <= nx < n and 0 <= ny < m):
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                print('new', nx, ny)
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    return graph[n-1][m-1]

start = time.time()
print(bfs(0, 0))
print(f"time : {time.time() - start} sec")
