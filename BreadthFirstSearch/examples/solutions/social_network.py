from collections import defaultdict, deque

n,m = map(int,input().split())
graph = defaultdict(list)
for i in range(m):
    v,u = map(int,input().split())
    graph[v].append(u)
    graph[u].append(v)


for i in range(int(input())):
    s,d=map(int,input().split())
    q=deque()
    q.append(s)
    visited=[False]*(n+1)
    visited[s]=True
    count = 0
    while len(q)!=0:
        if not d:
            print(len(q))
            break
        if count:
            count-=1
        element = q.popleft()
        
        for i in graph[element]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
        if not count:
            d-=1
            count = len(q)
    else:
        print(0)
        
