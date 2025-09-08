def minValueNode(root):
    if root.left is None:
        return root

    return minValueNode(root.left)