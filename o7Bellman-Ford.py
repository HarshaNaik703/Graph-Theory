""""
Bellman-Ford is applicable for directed graph, if you want to use it for undirected you must change the undirected graph into directed graph.
Algorithm
1. make distance array as infinity and add source node equal to 0
2. loop over n-1 times [ in the worst case , you will take n-1 edges to reach from first node to last node ]
3. loop over the edge list 
4. update the distance 
    if (distance[u] != 1e8 and distance[u] + dist < distance[v]):
                distance[v] = distance[u] + dist
5. repeat the step 3
6. repeat the step 2
"""

def Bellman_Ford(src, n,adj):
    distance = [1e8] *n
    distance[src] = 0
    for i in range(n-1):
        for ele in adj:
            u,v,dist = ele
            if (distance[u] != 1e8 and distance[u] + dist < distance[v]):
                distance[v] = distance[u] + dist
    return distance

n = int(input("Enter the number or vertices : "))
adj = []
while True:
    u = int(input("Enter the source node and -1 for exit : "))
    if (u == -1):
        break
    v = int(input("Enter the destination node : "))
    dist = int(input("Enter the destance between the node : "))
    adj.append([u,v,dist])
print(Bellman_Ford(0,n,adj))
    
