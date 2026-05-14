""""
Dijkstra's Algorithm for finding the stortest path among the graph
It can be implemented using set, priority queue(min  heap) and queue.
set is the fastest and min  heap is second fastest.
Algorithm
1. create a distance list and put the value of the source node equal to 0
2. put the source distance with node  into min heap
3. go through the min heap
4. get the neighbours of the node and relax the node and put the nodes into min heap with updated value of distance in shortest_distance list   if the value of the distance list changed
5. repeat the step 3 until min heap becomes empty

** It doesn't work on negative cycled 
"""

from heapq import heapify, heappop, heappush


def Dijkstra(src, n, adj):
    distance = [int(1e8)] * n
    distance[src] = 0
    for i in range(n-1):
        for u, v, dist in adj:
            if (distance[u] != int(1e8) and distance[u] + dist < distance[v]):
                distance[v] = distance[u] + dist
    for u, v, dist in adj:
        if (distance[u] != int(1e8) and distance[u] + dist < distance[v]):
            return [-1]
    return distance
    
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
print(Dijkstra(node, n, adj))
