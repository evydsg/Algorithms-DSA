def minValueNode(root):

    current = root

    while current and current.left:
        current = current.left
    
    return current