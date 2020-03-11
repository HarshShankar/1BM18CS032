from collections import defaultdict
class graph:
        def __init__(self):
                self.graph=defaultdict(list)
        def addEdge(self,u,v):
                self.graph[u].append(v)
        def dfsUtil(self,s,visited ):
                stack=[]
                stack.append(s)
                while stack:
                    r=stack.pop()
                    if (visited[r]==False):
                        print(r,end=" ")
                        visited[r]=True

                    for i in self.graph[r]:
                        if (visited[i]==False):
                            stack.append(i)

        def dfs(self):
                V=len(self.graph)

                visited=[False]*(V)

                for i in range(V):
                    if(visited[i]==False):
                        self.dfsUtil(i,visited)

g=graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

g.dfs()
