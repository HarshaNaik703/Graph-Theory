from collections import deque

from collections import deque


def BFS(node):

    print("Starting from", node)

    queue = deque()

    queue.append(node)

    visited[node] = True

    while queue:

        current = queue.popleft()

        print(current)

        for item in adj[current]:

            if not visited[item]:

                visited[item] = True

                queue.append(item)
        

n = int(input("give the number of the nodes : "))
# avoid writing [[]] * n, it will create a referances
adj = [[] for _ in range(n)]
for i in range(n):
    print(f"enter the connected node for {i} and -1 to end")
    while True:
        node = int(input(f"give the connected node {i} : "))
        if (node == -1):
            break
        adj[i].append(node)

visited = [False]*len(adj)
node = 0
BFS(node)
