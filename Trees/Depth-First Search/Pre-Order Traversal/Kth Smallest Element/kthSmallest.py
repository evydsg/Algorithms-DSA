class Solution:
    def __init__(self):
        self.count = 0
        self.result = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Base case: empty tree
        if root is None:
            return

        # Step 1: Traverse left subtree
        self.kthSmallest(root.left, k)

        # Step 2: Visit current node
        self.count += 1
        if self.count == k:
            self.result = root.val
            return self.result  # Found kth smallest

        # Step 3: Traverse right subtree
        self.kthSmallest(root.right, k)

        # Step 4: Return the result
        return self.result