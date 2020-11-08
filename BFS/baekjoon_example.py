"""
미로탐색 - 영훈
"""
from collections import deque
import time

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    return graph[n-1][m-1]


start = time.time()
print(bfs(0, 0))
print(f"BFS time : {time.time() - start} sec")


def dfs(x, y):
    if x == n-1 and y == m-1:
        return

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if graph[nx][ny] == 0:
            continue

        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            dfs(nx, ny)

    return graph[n-1][m-1]


start = time.time()
print(dfs(0, 0))
print(f"DFS time : {time.time() - start} sec")
