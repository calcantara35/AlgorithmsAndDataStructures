"""
Breadth-First Search is an algorithm used for tree traversal on graphs or tree data structures. 
BFS can be easily implemented using recursion and data structures like dictionaries and lists

The algorithm:
1. Pick any node, visit the adjacent unvisited vertex, mar it as visited, display ti, and insert it in a queue
2. If there are no remaining adjacent vertices left, remove the first vertex from the queue
3. repeat step 1 and step 2 until the queue is empty or the desired node is found
"""
"""
# Graph visual:
#         A
#       /   \
#      B     C
#     / \     \
#    D   E  -> F
# """

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# List to keep track of visited nodes
visited = []
# A list that is used to keep track of nodes currently in the queue
queue = []

# time complexity -> O(V + E) where V is the number of vertices and E is the number of edges


def bfs(visited, graph, node):
    # appending the node to the visited and queue
    visited.append(node)
    queue.append(node)

    # While there are still elements in the queue...
    while queue:
        # return and remove the first element in the queue
        s = queue.pop(0)
        # now looping through the neighbors of the graph at position s
        # s is the element that was popped out of the queue
        for neighbor in graph[s]:
            # if the neighbor is not in the visited list, meaning it hasnt been visited yet
            if neighbor not in visited:
                # append that neighbor to the visited list and queue
                visited.append(neighbor)
                queue.append(neighbor)
    return visited


# debug here
result = bfs(visited, graph, 'A')
print(result)
