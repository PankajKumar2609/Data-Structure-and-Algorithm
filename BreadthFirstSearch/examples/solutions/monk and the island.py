from collections import defaultdict, deque
import sys

for _ in range(int(input())):
    n,m = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for i in range(m):
        v,u = map(int, sys.stdin.readline().split())
        graph[v].append(u)
        graph[u].append(v)


    
        
    q=deque()
    q.append(1)
    visited=[False]*(n+1)
    distance = [float('inf')]*(n+1)
    distance[0]=0
    visited[1]=True
    distance[1]=0
    
    while len(q)!=0:
        element = q.popleft()
        for i in graph[element]:
            if not visited[i]:
                q.append(i)
                distance[i]=distance[element]+1
                visited[i] = True
            if i==n:
                print(distance[i])
                break
        if i==n:
            break

