# adjacency list
graph = {
    'A': ['D', 'C', 'B'],
    'B': ['E'],
    'C': ['G', 'F'],
    'D': ['H'],
    'E': ['I'],
    'F': ['J']
}


def dfs(graph, node):
    """
       This method will accept a graph, and traverse through it using DFS.
       We will use a stack and a list to keep track of the visited nodes.
       We will begin at the root node, append it to the path and mark it as visited.
       Then we will add all of its neighbors to the stack.
       At each step, we will pop out an element from the stack and check if it has been visited.
       If it has not been visited, we will add it to the path and add all of its neighbors to the stack. 
    """
    if node is None or node not in graph:
        return "Invalid input"

    path = []
    stack = [node]

    while len(stack) != 0:
        s = stack.pop()
        if s not in path:
            path.append(s)

        if s not in graph:
            # leaf node
            continue

        for neighbor in graph[s]:
            stack.append(neighbor)

    return "  ".join(path)


# calling dfs method on node "A"
dfsPath = dfs(graph, 'A')

print(dfsPath)

# recursive dfs below


def recursiveDfs(graph, node, path=[]):
    """
    This is the way to do dfs in a recursive manner.
    Base case will be "if the leaf node has been visited, we need to backtrack"
    """
    if node not in path:
        path.append(node)

        if node not in graph:
            # back track, leaf node
            return path

        for neighbor in graph[node]:
            path = recursiveDfs(graph, neighbor, path)

    return path


graph2 = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': ['J']
}

path = recursiveDfs(graph2, 'A')

print("  ".join(path))
