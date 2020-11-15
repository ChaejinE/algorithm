"""
전보
"""
import sys
import heapq

input = sys.stdin.readline
INF = 1e9
n, m, city = list(map(int, input().split()))

graph = [[] for i in range(n+1)]

for i in range(1, m+1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

times = [INF for i in range(n+1)]


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    times[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if dist < times[now]:
            continue

        for city, cost in graph[now]:
            cost += dist
            if cost < times[city]:
                times[city] = cost
                heapq.heappush(q, (cost, city))


dijkstra(city)

count = 0
max_time = 0
for idx, i in enumerate(times):
    if i == 0 or i == INF:
        continue

    count += 1
    max_time = i if max_time < i else max_time

print(count, max_time)
