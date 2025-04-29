class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        for index in range(len(nums) - 1):
            if nums[index] != nums[index + 1]:
                nums[k] = nums[index]
                k += 1
            
        nums[k] = nums[len(nums)- 1]
        k += 1
        return k