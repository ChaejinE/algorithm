"""
미로탈출 Ver. DFS
"""
import time

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return None

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
print(f"time : {time.time() - start} sec")
