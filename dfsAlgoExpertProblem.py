"""
You are given a Node Class that has a name and an array of optional children nodes.
When put together, nodes form an acyclic tree-like structure.
A graph is acyclic if it has no cycles.

Implement the 'depth-first search' method on the Node Class:
- which takes in an empty array
- traverses the tree using the depth-first search approach. (Specifically navigating from left to right)
- stores all the nodes' names in the input array
- returns the array
"""

# Given Node Class


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # add the current node to the array
        # the array stands for the visited nodes
        # first round will add the root node because it is now visited
        array.append(self.name)

        # Then we will go to the neighboring node of the graph and again call the dfs function to use the neighbor parameter
        for child in self.children:
            child.depthFirstSearch(array)

        # return the array of visited nodes
        return array
