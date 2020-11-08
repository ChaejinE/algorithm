"""
음료수 얼려먹기 ver. BFS
"""
from collections import deque
import time

n, m = list(map(int, input().split()))

start_point = [1, 1]

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    q = deque([])
    q.append((x, y))
    if graph[x][y] == 0:
        while q:
            x, y = q.popleft()
            graph[x][y] = 1
            for idx in range(4):
                nx = x + dx[idx]
                ny = y + dy[idx]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if graph[nx][ny] == 1:
                    continue

                elif graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    q.append((nx, ny))
        return True
    return False

start = time.time()
result = 0
for i in range(n):
    for j in range(m):
        if bfs(i, j) == True:
            result += 1

print(result)
print(f"time : {time.time() - start} sec")
