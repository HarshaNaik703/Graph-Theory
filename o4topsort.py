def DFS(node, stack, visited):
    
    visited[node] = True
    for item in adj[node]:
        if  visited[item] == False:
            DFS(item, stack, visited)
    stack.append(node)

def topological_sort(n, adj):
    visited = [False]*len(adj)
    stack = []
    
    for i in range(n):
        if visited[i] == False:
            DFS(i, stack , visited)
            
    return stack[::-1]

n = int(input("give the number of the nodes : "))
adj = [[] for _ in range(n)]
for i in range(n):
    print(f"enter the connected node for {i} and -1 to end")
    while True:
        node = int(input(f"give the connected node {i} : "))
        if (node == -1):
            break
        adj[i].append(node)
        


print(topological_sort(n, adj))
    


