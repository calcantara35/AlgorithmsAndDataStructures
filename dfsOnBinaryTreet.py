# A binary tree is a special kind of graph in which each node can have only two children or no child
# Another important property of a binary tree is that the value of the LEFT child will be less than or equal to
# the current node's value
# Similarly, the value in the right child is greater than the current node's value

# Need to create a binary tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """
        Ensures that the properties of binary trees are satisified no matter in what order we insert the values
        """
        if value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
            else:
                self.value = value

# Now create a root node object and insert values in it to construct a binary tree


root = Node(7)
root.insert(2)
root.insert(25)
root.insert(9)
root.insert(80)
root.insert(1)
root.insert(5)
root.insert(15)
root.insert(8)

# implementing dfs for a binary tree


def dfs(root):
    """
        Recursive function that takes as input the root node and displays all the values in the tree in the
        "Depth-First Search" order
        This is also called the "preorder travseral" of a binary tree
    """
    if root is None:
        return
    else:
        print(root.value, end=" ")
        dfs(root.left)
        dfs(root.right)


# we can now call this method and pass the root node object we just created.
dfs(root)
