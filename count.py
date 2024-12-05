def dfs(v, visited, parent, graph):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]: 
            if dfs(neighbor, visited, v, graph):
                return True
        elif parent != neighbor: 
            return True
    return False

def has_cycle(graph):
    visited = [False] * len(graph)
    for i in range(len(graph)):
        if not visited[i]: 
            if dfs(i, visited, -1, graph):
                return True
    return False

graph = {
    0: [1, 2, 3, 6],
    1: [0, 2, 4, 7],
    2: [0, 1, 5, 8],
    3: [0, 4, 5, 6],
    4: [1, 3, 5, 7],
    5: [2, 3, 4, 8],
    6: [0, 3, 7, 8],
    7: [1, 4, 6, 8],
    8: [2, 5, 6, 7]  
}

print(has_cycle(graph))  
