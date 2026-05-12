def DFS(node):
    if visited[node] == True:
        return False
    visited[node] = True
    print(f"{node}\t ")
    for item in adj[node]:
        DFS(item)
    
n = int(input("give the number of the nodes : "))
adj = [[] for _ in range(n)] # avoid writing [[]] * n, it will create a referances
for i in range(n):
    print(f"enter the connected node for {i} and -1 to end")
    while True:
        node = int(input(f"give the connected node {i} : "))
        if(node == -1):
            break
        adj[i].append(node)

visited = [False]*len(adj)
node=0
DFS(node)
