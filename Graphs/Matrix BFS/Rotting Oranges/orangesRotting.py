from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        directions = [[1,0], [-1,0], [0, 1], [0,-1]]
        minutes = 0
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        
        
        if fresh == 0: #No rotten fruit
            return 0
        
        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if(min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] == 2 or grid[r][c] == 0):
                        continue

                    grid[r][c] = 2
                    fresh -= 1  
                    queue.append((r, c))

            minutes += 1
        
        if fresh == 0:
            return minutes
        
        return -1