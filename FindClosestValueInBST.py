class BST:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree: BST, target: int):
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree: BST, target: int, closest: int):
    currentNode = tree
    while currentNode is not None:
        # if our target value is farther away from closest than it is from tree value, then we update
        # closest to be the trees value
        # checking to see if the current node value that we are at has a closer value to the target
        # than our current closest node does
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        # if the target number we want to find is less than the current node's value,
        # set the currentNode to the left since that means the current node will have a smaller value and
        # it could become closer to the target value
        if target < currentNode.value:
            currentNode = currentNode.left
        # if the target number we want to find is greater than the current node's value,
        # set the currentNode to the right since that means the current node will have a bigger value and
        # it could become closer to the target value
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest

root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

closestValue = findClosestValueInBst(root, 12)