# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.sum = 0

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        # Add current node's value
        self.sum += root.val

        # Check if we are at a leaf and the path sum matches
        if root.left is None and root.right is None and self.sum == targetSum:
            return True

        # Explore left subtree
        if self.hasPathSum(root.left, targetSum):
            return True

        # Explore right subtree
        if self.hasPathSum(root.right, targetSum):
            return True

        # Backtrack
        self.sum -= root.val

        return False