from collections import defaultdict
class graph:
    def __init__(self,vertices):
        self.V=vertices
    def transitiveclosure(self,adj):
        result=[i[:] for i in adj]
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    result[i][j]=result[i][j] or (result[i][k] and result[k][j])
        for i in range(self.V):
            for j in range(self.V):
                print(result[i][j],end=" ")
            print()
G=graph(4)
graph = [[1, 1, 0, 1], 
         [0, 1, 1, 0], 
         [0, 0, 1, 1], 
         [0, 0, 0, 1]]
G.transitiveclosure(graph)

