graph1 = {
    'A': ['B','C'],
    'B': ['E','D'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs_stack(graph, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited

path = dfs_stack(graph1, 'A')
print(" -> ".join(path))
