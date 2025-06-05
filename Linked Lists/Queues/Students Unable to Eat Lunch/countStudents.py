from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        students = deque(students)
        sandwiches = deque(sandwiches)
        
        
        while len(students) > 0:
            if students[0] == sandwiches[0]:
                sandwiches.popleft()
                students.popleft()
                count = 0
            else:
                first_student = students.popleft()
                students.append(first_student)
                count += 1

                if count == len(students):
                    break
            
        return len(students)