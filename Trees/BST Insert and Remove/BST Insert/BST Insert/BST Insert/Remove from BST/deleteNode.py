def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        
        current = root
        parent = None

        while current:
            if current.val > key:
                parent = current
                current = current.left
            elif current.val < key:
                parent = current
                current = current.right
            else:
                if current.right is None and current.left is None: #Leaf Node
                    if parent:
                        if parent.left == current:
                            parent.left = None
                        else:
                            parent.right = None
                    else:
                        root = None
                elif current.left is None:
                    if parent:
                        if parent.left == current:
                            parent.left = current.right
                        else:
                            parent.right = current.right
                    else:
                        root = current.right
                elif current.right is None:
                    if parent:
                        if parent.left == current:
                            parent.left = current.left
                        else:
                            parent.right = current.left
                    else:
                        root = current.left
                else:
                    minNode = self.minValueNode(current.right)
                    current.val = minNode.val
                    current.right = self.deleteNode(current.right, minNode.val)
                break
        
        return root