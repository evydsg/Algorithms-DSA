from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        directions = [[1, 0], [-1,0], [0, 1], [0, -1], [1,1], [-1,-1], [-1, 1], [1, -1]]
        shortest = 0

        if grid[0][0] != 0:
            return -1 
        
        shortest += 1
        visited.add((0,0))
        queue.append((0,0))

        while queue:
            
            for _ in range(len(queue)):
                row, col = queue.popleft()

                if row == rows-1 and col == cols-1:
                    return shortest
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if(min(r, c) < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] == 1):
                        continue
                
                    queue.append((r, c))
                    visited.add((r, c))
            
            shortest += 1