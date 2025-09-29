"""
Understand
- Remove all the values that are equal to val in place
- No extra memory allowed

Match
- Array Traversal and pointer

Plan
- Initialize variable to return number of elements that we didn't remove
- Iterate through input array
    - Compare current value with val to return
        - Not equal
            - Array at index k is equal to current number
            - Increment array
- Return k

Evaluate
- Time Complexity: O(n)
- Space Complexity: O(1)
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        
        return k