class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(row, col):
            count = 0
            if min(row, col) < 0 or row >= rows or col >= cols or (row, col) in visited or grid[row][col] == 0:
                return 0 
            
            visited.add((row, col))

            if grid[row][col] == 1:
                count += 1

            for dr, dc in directions:
                count += dfs(row + dr, col + dc)
            
            return count

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_area = max(dfs(row, col), max_area)
        
        return max_area