class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(index):
            if index == len(nums):  # Full subset reached
                result.append(subset.copy())
                return

            # Include element
            subset.append(nums[index])
            backtrack(index + 1)

            # Exclude element (backtrack)
            subset.pop()
            backtrack(index + 1)

        backtrack(0)
        return result