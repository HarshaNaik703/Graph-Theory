
n = int(input("give the number of the nodes : "))
adj = [[] for _ in range(n)]
for i in range(n):
    print(f"enter the connected node for {i} and -1 to end")
    while True:
        node = int(input(f"give the connected node {i} : "))
        if(node == -1):
            break
        weight = int(input(f"wieght of the node {i} "))
        temp = [node,weight]
        adj[i].append(temp)
        

def shortest_path(src):
    sp = [-1] * n
    sp[src] = 0
    topo_sort=topological_sort(n, adj)

def DFS(node, stack, visited):
    visited[node] = True
    for item in adj[node]:
        if  visited[item[0]] == False:
            DFS(item[0], stack, visited)
    stack.append(node)

def topological_sort(n, adj):
    visited = [False]*len(adj)
    stack = []
    for i in range(n):
        if visited[i] == False:
            DFS(i, stack , visited)
    return stack[::-1]


