"""Alogrith
    1. Appy topological sort and store the elements in the array
    2. make distance of the source node to 0
    3. go through the array and do the following operations
    4. pop the element of the array
    5. go through the adjecent nodes of the popped element and update the weight of the shortest_distance array such 
    that if the distance of the popped element + weight of the current element is less than distance of the current 
    element, then update the distance of the shortest_distance array
    6. repeat the process 3 until array becomes empty 
"""



def shortest_path(src):
    sd = [1e9] * n
    sd[src] = 0
    topo_sort=topological_sort(n, adj)
    while len(topo_sort) != 0 :
        node = topo_sort.pop()
        for list in adj[node] : 
            curr = list[0]
            weight = list[1]
            if (sd[node] + weight < sd[curr]) :
                sd[curr] = weight + sd[node]
    return sd 
            
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
    return stack

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
        
node = int(input("Enter the source vertix : "))
print(shortest_path(node))



