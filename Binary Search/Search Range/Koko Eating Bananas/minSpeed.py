class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        #Define delimeters 
        left = 1 #Min number of bananas that he can eat per hour
        right = max(piles) # Max number of bananas that are in a pile, which mean it is the max
        result = right #Variable to return the speed

        while left <= right:
            middle = (left + right)//2
            hours = 0 #Variable to check if koko spent more time eating bananas than he needed

            for pile in piles:
                hours += math.ceil(pile/middle)

            if hours <= h:
                result = min(result, middle)
                right = middle - 1
            else:
                left = middle + 1
        
        return result
