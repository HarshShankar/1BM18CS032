from collections import defaultdict
class graph:
        def __init__(self):
                self.graph=defaultdict(list)
        def addEdge(self,u,v):
                self.graph[u].append(v)
        def isCycleUtil(self,v,visited,recStack):
            
            visited[v]=True
            recStack[v]=True
            
            for neigh in self.graph[v]:
                if(visited[neigh]==False):
                    if self.isCycleUtil(neigh,visited,recStack)==True :
                        return True
                elif(recStack[neigh]==True):
                    return True

            recStack[v]=False
            return False
        def Cycle(self):
            visited=[False]*(len(self.graph))
            recStack=[False]*(len(self.graph))
                                
            for i in self.graph:
                if(visited[i]==False):
                    if self.isCycleUtil(i,visited,recStack)== True:
                        return True
                else:
                    return False

g=graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

if g.Cycle()==1:
    print ("Graph has cycle")
else:
    print ("Graph has no cycle")

