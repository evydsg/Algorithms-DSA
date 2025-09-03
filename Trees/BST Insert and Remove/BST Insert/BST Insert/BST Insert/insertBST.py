class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            root = TreeNode(val)
            return root
        
        current = root

        while current:
            if current.val < val:
                if current.right is None:
                    current.right = TreeNode(val)
                    break
                
                current = current.right
            else:
                if current.left is None:
                    current.left = TreeNode(val)
                    break
                
                current = current.left
        
        return root