class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]

        for color in nums:
            count[color] += 1
        
        index = 0

        for ptrC in range(len(count)):
            for color in range(count[ptrC]):
                nums[index] = ptrC
                index += 1