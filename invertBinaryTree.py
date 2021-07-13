"""
Write a function that takes in a binary tree and inverts it. In other words, the function should swap every left node in the tree
for its corresponding right node
"""
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invertBinaryTree(tree):
    """
    Recursive function
    bfs approach
    O(n) time and O(d) space where d is the depth of the tree
    largest amount of calls being used up in the call stack is going
    to amount based on the depth of the tree
    """
    if tree is None:
        return

    tree.left, tree.right = tree.right, tree.left

    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

# takes in the root node of the binary tree
def invertBinaryTree2(tree):
    
    """
    Iterative solution. Using BFS to solve
    Runs in O(n) time and O(n) space
    because the queue and traversal
    """

    # put the root node in the queue
    queue = [tree]
    # bfs
    while queue:
        # first in first out
        current = queue.pop(0)
        # if we reach a leaf node we are done
        if current is None:
            continue
        # call swap helper function
        swap(current)
        queue.append(current.left)
        queue.append(current.right)


def swap(node):
    node.left, node.right = node.right, node.left


