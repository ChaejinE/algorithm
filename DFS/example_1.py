"""
음료수 얼려 먹기
"""
import copy
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

temp = copy.deepcopy(graph)

'''첫번째 방법'''


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1  # 방문처리
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

''' 두번째 방법 '''

graph = temp

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                continue

            if graph[nx][ny] == 0:
                dfs(nx, ny)
                graph[nx][ny] = 1
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
