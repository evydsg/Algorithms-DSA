class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        inorder = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            inorder.append(current.val)
            current = current.right
        
        return inorder

class Solution:
    def __init__(self):
        self.inorder = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        self.inorderTraversal(root.left)
        self.inorder.append(root.val)
        self.inorderTraversal(root.right)
        
        return self.inorder