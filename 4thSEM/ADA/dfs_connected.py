 
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

n = int(input("Enter number of vertices: "))
e = int(input("Enter the number of edges: "))
if(n == 0 or e == 0):
    print('Order-zero graph!')
    exit()
graph = {}
print("Enter the edges in the format [start] [end]")
for i in range(e):
    start, end = list(input("").split())
    if not graph.get(start):
        graph[start] = set([end])
    else:
        graph[start].add(end)
    if not graph.get(end):
        graph[end] = set([start])
    else:
        graph[end].add(start)

if len(dfs(graph, list(graph.keys())[0])) == n:
    print("Connected")
else:
    print("Not connected")
