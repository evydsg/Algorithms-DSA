class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        result = len(students)
        count = Counter(students)

        for s in sandwiches:
            if count[s] > 0:
                result -= 1
                count[s] -=1
            else:
                return result
        
        return result