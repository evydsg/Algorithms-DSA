from typing import Optional

# assuming TreeNode is defined as:
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minValueNode(self, node: Optional['TreeNode']) -> Optional['TreeNode']:
        """Return the leftmost (minimum) node in the given subtree."""
        if node is None:
            return None
        current = node
        while current.left:
            current = current.left
        return current

    def deleteNode(self, root: Optional['TreeNode'], key: int) -> Optional['TreeNode']:
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # node to delete found
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            # two children: replace with inorder successor
            successor = self.minValueNode(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root