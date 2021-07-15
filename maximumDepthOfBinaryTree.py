"""
Given the root of a binary tree, return its maximum depth
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest node

Input = root = [3, 9, 20, null, null, 15, 7]
output = 3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# o(n) -> time and worst case for space o(h)
def maxDepth(root):
    if not root:
        return 0
    
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


def iterativeMaxDepth(root):
    # preorder dfs
    stack = [[root, 1]]
    result = 0
    while stack:
        node, depth = stack.pop()

        if node:
            result = max(result, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    
    return result

import collections

def bfsMaxDepth(root):
    if not root:
        return 0
    level = 0
    q = collections.deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level

        