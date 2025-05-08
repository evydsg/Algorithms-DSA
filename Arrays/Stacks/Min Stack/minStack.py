class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            current_min = min(self.min_stack[-1], val)
            self.min_stack.append(current_min)
        
        self.main_stack.append(val)
        return

    def pop(self) -> None:
        self.main_stack.pop()
        self.min_stack.pop()

        return 
        
    def top(self) -> int:
        return self.main_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]