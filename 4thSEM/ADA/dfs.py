from collections import defaultdict
class graph:
        def __init__(self):
                self.graph=defaultdict(list)
        def addedge(u,v):
                self.graph[u].append(v)
        def dfs_start(self,s):
                visited=[False]*(len(graph))
                visited[s]=True
                stack=[]
                stack.append(s)
                dfs(stack)
        def dfs(self,s):
                k=graph[s[-1][0]]
                if(k==[]):
                        s.pop(-1)
                        dfs(s)
                if(visited[k]== False ):
                        stack.append(k)
                        visited[k]=True
                                               
