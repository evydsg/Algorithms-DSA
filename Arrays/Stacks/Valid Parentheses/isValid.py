class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'(': ')', '{' : '}', '[': ']'}
        stack = []

        for character in s:
            if character in valid:
                stack.append(character)
            elif len(stack) != 0 and character == valid[stack[-1]]:
                stack.pop()
            else:
                return False
        
        if len(stack) == 0:
            return True
        return False