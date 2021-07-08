# DFS implementation in Python
# DFS is a recursive algorithm that uses the concept of backtracking
# 1) we will start by putting any one of the graph's vertex on top of the stack.
# 2) after that take the top item of the stack and add it to the visited list of the vertex
# 3) next, create a list of that adjacent node of the vertex. Add the ones which arent in the visited list of vertexes to the top of the stack
# 4) Lastly, keep repeating steps 2 and 3 until the stack is empty

# using a python dictionary to ac as an adjacency list
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

"""
In the above code, first, we will create the graph for which we will use the depth-first search.
After creation, we will create a set for storing the value of the visited nodes to keep track of the 
visited nodes of the graph.
"""
# set to keep track of visited nodes of graph
visited = set()

# function for depth-first search -> recursive
def dfs(visited, graph, node):
    """
    Function with the parameters as visited nodes, the graph itself, and the node respectively
    This function will check whether any node of the graph is visited or not.
    If not, then we will print the node and add it to the visited set of nodes.
    Then we will go to the neighboring node of the graph and again call the dfs function to use the neighbor parameter

    Runtime -> O(V+E) -> time complexity because v is the number of nodes and e is the number of edges
    Space Complexity -> O(V)
    """
    # if the current node passed in is not in the visited stack
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

# driver code

"""
At last we run the driver code which prints the final result of DFS by calling the DFS the first time with the starting vertex of the graph
"""
print("The following is the depth first search")
dfs(visited, graph, '5')