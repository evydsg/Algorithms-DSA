"""
Understand: 
    - Find the node that equals to value
    - Once you find, return the true
    - If not found, return Null

Match
    - Binary Search Tree

Plan
1. Recursive
    - Check if node is Null
        Yes, return Null
    
    - Compare if current node is less than value
        - Call the function passing the right Tree
    - Compare if current node is greater than value
        - Call the function passing the left Tree
    - Return Tree

Evaluate
- Time Complexity: O(logn) if balanced, else O(N)
- Space Complexity: O(logn) if balanced else O(N)

Plan 
2. Iterative
- Check if root is None
    - Return None
- Initialize pointer to start at current node
- Iterate through the tree while pointer is not none
- Compare if the current node is less than value
    - Assign right Tree
- Compare if the current node is greater than value
    - Assign left Tree
- Compare if root is the same as value
    - Return Current Tree
- Return Current

Evaluate
- Time Complexity: O(logn) if balanced else O(N)
- Space Complexity: O(1) we are only using pointers
"""
def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if self.root is None:
        return None
    
    if self.root.val < val:
        return self.searchBST(root.right, val)
    elif self.root.val > val:
        return self.searchBST(root.left, val)
    else:
        return self.root

def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        current = root

        while current:
            if current.val < val:
                current = current.right
            elif current.val > val:
                current = current.left
            else:
                return current
        
        return current