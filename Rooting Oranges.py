from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        directions = [[1,0], [-1,0], [0, 1], [0,-1]]
        minutes = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                    visited.add((row, col))
        
        if len(queue) == 0: #No rotten fruit
            return -1
        
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if(min(r, c) < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] == 0):
                        continue
                    
                    if grid[r][c] == 1:
                        grid[r][c] = 2
                        print("Start of minute layer, queue:", list(queue), "minutes:", minutes)
                
                    queue.append((r, c))
                    visited.add((r, c))

            minutes += 1
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        
        return minutes

Solution.orangesRotting([[1,1,0],[0,1,1],[0,1,2]])