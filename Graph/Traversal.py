from collections import deque

def bfs(graph, start):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    queue = deque()
    
    visited[start] = True
    queue.append(start)
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        
        for i in range(num_nodes):
            if graph[node][i] and not visited[i]:
                visited[i] = True
                queue.append(i)
    
    print()

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")
    
    for i in range(len(graph)):
        if graph[start][i] and not visited[i]:
            dfs(graph, i, visited)

# Example adjacency matrix
graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

"""
A:B,C
B:D,E
C:A
D:F
E:B,F

"""

start_node = 0  # Starting node for BFS and DFS

print("BFS Traversal:", end=" ")
bfs(graph, start_node)

visited = [False] * len(graph)
print("DFS Traversal:", end=" ")
dfs(graph, start_node, visited)
