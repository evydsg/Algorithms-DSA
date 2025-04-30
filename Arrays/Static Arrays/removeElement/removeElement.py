class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        k, index = 0, 0

        while index < len(nums):
            while index < len(nums) and nums[index] != val:
                nums[k] = nums[index]
                k += 1
                index += 1
            
            index += 1
        
        return k