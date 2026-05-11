def DFS(node):
    visited[node] = True
    for item in adj[node]:
        if  visited[item] == False:
            DFS(item)
    stack.append(node)

def topological_sort(n):
    
    for i in range(n):
        if visited[i] == False:
            DFS(i)

n = int(input("give the number of the nodes : "))
adj = [[] for _ in range(n)]
for i in range(n):
    print(f"enter the connected node for {i} and -1 to end")
    while True:
        node = int(input(f"give the connected node {i} : "))
        if (node == -1):
            break
        adj[i].append(node)
        

visited = [False]*len(adj)

stack = []
topological_sort(n=n)

print(stack)
    


