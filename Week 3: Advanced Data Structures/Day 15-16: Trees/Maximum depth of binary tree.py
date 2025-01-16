"""# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(self, root):
    if root is None:
        return 0

    leftdepth = self.maxDepth(root.left)
    rightdepth = self.maxDepth(root.right)

    return 1 + max(leftdepth, rightdepth)


root = [3, 9, 20, "", "", 15, 7]
print(maxDepth(root))
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    if root is None:
        return 0

    leftdepth = maxDepth(root.left)
    rightdepth = maxDepth(root.right)

    return 1 + max(leftdepth, rightdepth)


# Building BTree
def buildTree(values):
    if not values:
        return None

    def inner(index):
        if index < len(values) and values[index] != "":
            node = TreeNode(values[index])
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
            return node
        return None

    return inner(0)


values = [3, 9, 20, "", "", 15, 7]


root = buildTree(values)
print("Maximum Depth:", maxDepth(root))
