def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]

# Example adjacency list representing a DAG
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

print("Topological Sort:", topological_sort(graph))
