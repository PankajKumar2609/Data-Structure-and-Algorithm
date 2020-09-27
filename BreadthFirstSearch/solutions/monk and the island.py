from collections import defaultdict
from queue import Queue as q

class node:
    def __init__(self, value):
        self.value = value
        self.count = float('inf')
        self.p = value
        self.visited = 'green'

class graph:
    def __init__(self, vertex):
        self.vertices = vertex
        self.store = defaultdict(list)
        self.node={}
        self.data=q()

    def add_edge(self, u, v):
        self.store[u].append(v)
        self.store[v].append(u)
        if u not in self.node:
            self.node[u]=node(u)
        if v not in self.node:
            self.node[v]=node(v)

    def find(self):
        self.data.put(self.node[1])
        self.node[1].count=0
        while self.data.qsize()!=0:
            element = self.data.get()
            
            for i in self.store[element.value]:
                if self.node[i].visited == 'green':
                    self.data.put(self.node[i])
                    if self.node[i].count>self.node[element.value].count+1:
                        self.node[i].p = element.value
                        self.node[i].visited = 'blue'
                        self.node[i].count=self.node[element.value].count+1
                elif self.node[i].visited == 'blue':
                    if self.node[i].count>self.node[element.value].count+1:
                        self.node[i].p = element.value
                        self.node[i].visited = 'blue'
                        self.node[i].count=self.node[element.value].count+1
            element.visited = 'black'
        return self.node[self.vertices].count

for i in range(int(input())):
    
    n,m=map(int,input().split())
    g=graph(n)
    for j in range(m):
        u,v=map(int,input().split())
        g.add_edge(u,v)
    print(g.find())

