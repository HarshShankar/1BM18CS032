import string
def check1(adja_list, source):
    queue1 = [source]
    visited = [source]
    while len(queue1) > 0:
        curr = queue1.pop()
        for i in adja_list[curr]:
            if i not in visited:
                visited.append(i)
                queue1.append(i)    
    return visited
n = int(input("Enter the number of nodes : "))
out_graphs1 = {}
for i in list(string.ascii_lowercase)[0:n]:
    print("Enter the nodes directed by node "+i, end=": ")
    out_graphs1[i] = [j for j in input().split()]
source = input("Enter the source node : ")
final = check1(out_graphs1, source)
if(final != []):
    print(final)
else:
    print("No nodes are accessible!")
