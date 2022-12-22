import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
distance = [INF] * (n+1)
visited = [False] * (n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    distance[start] = 0 
    heapq.heappush(q,(0,start))
    while q:
        dist, now_node = heapq.heappop(q)
        if distance[now_node] < dist: continue
        for next, weight in graph[now_node]:
            cost = dist + weight
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q,(cost,next))

dijkstra(start)
print(distance[end])