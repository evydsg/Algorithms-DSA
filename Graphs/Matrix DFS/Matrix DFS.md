# Matrix DFS

## Overview

To traverse all positions within a matrix, we can use Depth First Search (DFS), similar to how we would traverse a tree. In a matrix, we can move in all four directions: up, down, left, and right. Sometimes diagonal movement is possible, but this guide focuses on the four cardinal directions for simplicity.

---

## Problem Example

**Question:** Count the unique paths from the top left to the bottom right. A single path may only move along 0's and can't visit the same cell more than once.

```python
matrix = [[0,0,0,0],
          [1,1,0,0],
          [0,0,0,1],
          [0,1,0,0]]
```

**Visual Representation:**

```
     0   1   2   3  (columns)
   ┌───┬───┬───┬───┐
 0 │ S │ 0 │ 0 │ 0 │  S = Start (0,0)
   ├───┼───┼───┼───┤
 1 │ X │ X │ 0 │ 0 │  X = Blocked (1's)
   ├───┼───┼───┼───┤
 2 │ 0 │ 0 │ 0 │ X │  E = End/Goal (3,3)
   ├───┼───┼───┼───┤
 3 │ 0 │ X │ 0 │ E │
   └───┴───┴───┴───┘
(rows)
```

---

## Approach

This problem is similar to backtracking. Since DFS is recursive in nature, we'll use recursion to explore all possible paths. We need to:

1. Try every path using backtracking (since we might reach dead ends)
2. Keep count of valid paths from each vertex
3. Ensure we don't visit the same cell twice in a single path

**Movement Pattern:**

```
From any cell (r, c), we can move in 4 directions:

              ↑
         (r-1, c)

    ← (r, c-1)  [r,c]  (r, c+1) →

         (r+1, c)
              ↓
```

---

## Base Cases

### 1. A Unique Path Does NOT Exist

Return `0` when any of these conditions are met:

- **Out of bounds**: Either row `r` or column `c` becomes negative, or exceeds the matrix dimensions
    - We need both valid `r` AND valid `c` to continue searching
    - Cannot perform search on `matrix[-1][3]`
- **Already visited**: The coordinate has been visited in the current path
    - Prevents counting the same path multiple times
- **Blocked cell**: The current coordinate contains a `1`
    - We can only move through `0`'s

**Base Case Visualization:**

```
Invalid moves from position (1,2):

     0   1   2   3
   ┌───┬───┬───┬───┐
 0 │   │   │ V │   │  ↑ Going up to (0,2) - already visited! Return 0
   ├───┼───┼───┼───┤
 1 │ X │ X │ * │   │  * = Current position (1,2)
   ├───┼───┼───┼───┤  ← Going left to (1,1) - blocked (X)! Return 0
 2 │   │   │   │ X │
   ├───┼───┼───┼───┤
 3 │   │ X │   │ E │
   └───┴───┴───┴───┘

Out of bounds example from (0,0):
- Going up: (-1, 0) → r < 0, invalid! Return 0
- Going left: (0, -1) → c < 0, invalid! Return 0
```

### 2. A Unique Path DOES Exist

Return `1` when:

- We reach the bottom-right corner (`matrix[ROWS-1][COLS-1]`)
- This indicates we've found a complete valid path from `matrix[0][0]` to the destination

```
Success condition:

     0   1   2   3
   ┌───┬───┬───┬───┐
 0 │   │   │   │   │
   ├───┼───┼───┼───┤
 1 │   │   │   │   │
   ├───┼───┼───┼───┤
 2 │   │   │   │   │
   ├───┼───┼───┼───┤
 3 │   │   │   │ ✓ │  ← When r == ROWS-1 and c == COLS-1, return 1
   └───┴───┴───┴───┘
```

---

## Implementation

### Key Data Structure: Hash Set for Visited Tracking

- **Why hash set?** Provides O(1) time for insertion and lookup
- **Alternative:** 2D boolean array of same size as grid
- **Purpose:** Ensures we don't visit a coordinate more than once in a single path

### Algorithm Steps

At any coordinate `(r, c)`:

1. Add current coordinate to visited set
2. Recursively perform DFS on all four neighbors:
    - `(r+1, c)` - down
    - `(r-1, c)` - up
    - `(r, c+1)` - right
    - `(r, c-1)` - left
3. Sum up all valid paths returned from recursive calls
4. **Backtrack:** Remove current coordinate from visited set
    - Allows exploring different paths through this cell

**Backtracking Visualization:**

```
When at cell (0,1), visited set contains: {(0,0), (0,1)}

     0   1   2   3
   ┌───┬───┬───┬───┐
 0 │ V │ V │ ? │ ? │  V = Visited (in set)
   ├───┼───┼───┼───┤  ? = Not yet explored
 1 │ X │ X │ ? │ ? │
   ├───┼───┼───┼───┤
 2 │ ? │ ? │ ? │ X │
   ├───┼───┼───┼───┤
 3 │ ? │ X │ ? │ E │
   └───┴───┴───┴───┘

After exploring paths from (0,1) and returning:
- Remove (0,1) from visited set
- visited = {(0,0)} only
- Now (0,1) can be visited again via different path!
```

### Code

```python
# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

# Count paths (backtracking)
def dfs(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])

    # Base case: Invalid path
    if (min(r, c) < 0 or
        r == ROWS or c == COLS or
        (r, c) in visit or grid[r][c] == 1):
        return 0

    # Base case: Reached destination
    if r == ROWS - 1 and c == COLS - 1:
        return 1

    # Mark as visited
    visit.add((r, c))

    # Explore all four directions
    count = 0
    count += dfs(grid, r + 1, c, visit)  # Down
    count += dfs(grid, r - 1, c, visit)  # Up
    count += dfs(grid, r, c + 1, visit)  # Right
    count += dfs(grid, r, c - 1, visit)  # Left

    # Backtrack: Remove from visited
    visit.remove((r, c))
    return count
```

---

## Visual Walkthrough

### Step 1: Finding First Unique Path

The algorithm explores from (0,0), marking cells as visited:

```
Step-by-step exploration (numbers show order visited):

     0   1   2   3
   ┌───┬───┬───┬───┐
 0 │ 1 │ 2 │ 3 │ 4 │  Path goes right along top row
   ├───┼───┼───┼───┤
 1 │ X │ X │ 7 │ 5 │  Then down the right column
   ├───┼───┼───┼───┤
 2 │ 9 │ 8 │ 6 │ X │  Hits blocked cell, backtracks
   ├───┼───┼───┼───┤
 3 │   │ X │10 │11 │  Finds path through (3,2) to goal
   └───┴───┴───┴───┘

First Valid Path: (0,0)→(0,1)→(0,2)→(0,3)→(1,3)→(2,2)→(2,1)→(2,0)→(3,0)→(3,2)→(3,3)
```

Wait, let me recalculate this path more carefully...

Actually, a simpler valid path:

```
     0   1   2   3
   ┌───┬───┬───┬───┐
 0 │ 1 │ 2 │ 3 │ 4 │
   ├───┼───┼───┼───┤
 1 │ X │ X │ 6 │ 5 │
   ├───┼───┼───┼───┤
 2 │   │   │ 7 │ X │
   ├───┼───┼───┼───┤
 3 │   │ X │ 8 │ 9 │  ✓ GOAL REACHED
   └───┴───┴───┴───┘

Path 1: (0,0)→(0,1)→(0,2)→(0,3)→(1,3)→(1,2)→(2,2)→(3,2)→(3,3) ✓
```

### Step 2: Backtracking to Find Another Path

After finding the first path, algorithm backtracks and explores alternatives:

```
Alternative path exploration:

     0   1   2   3
   ┌───┬───┬───┬───┐
 0 │ 1 │ 2 │   │   │  Start same, then go different direction
   ├───┼───┼───┼───┤
 1 │ X │ X │ 3 │   │
   ├───┼───┼───┼───┤
 2 │ 6 │ 5 │ 4 │ X │
   ├───┼───┼───┼───┤
 3 │ 7 │ X │ 8 │ 9 │  ✓ GOAL REACHED
   └───┴───┴───┴───┘

Path 2: (0,0)→(0,1)→(1,2)→(2,2)→(2,1)→(2,0)→(3,0)→(3,2)→(3,3) ✓
```

**Result:** Function returns `2`, indicating there are **2 unique paths** from (0,0) to (3,3).

---

## Complexity Analysis

### Time Complexity: O(4^(n×m))

**Breakdown:**

- **Worst case:** Visit every coordinate in the grid → O(n × m) where n = rows, m = columns
- **At each coordinate:** We can move in 4 directions
- **Each neighbor:** Also has 4 directional options
- **Decision tree structure:**
    - Branching factor: 4 (four children per node)
    - Tree height: n × m (size of matrix)
    - Total: O(4^(n×m))

**Decision Tree Visualization:**

```
Each node represents a cell position, with 4 possible moves:

                    (0,0)
                      |
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓             ↓
      (1,0)         (−1,0)        (0,1)         (0,−1)
       |              X             |              X
    ┌──┼──┐                     ┌──┼──┐
    ↓  ↓  ↓  ↓                  ↓  ↓  ↓  ↓
   ... ... ...                ... ... ...

Each cell has 4 branches → branching factor = 4
Maximum depth = n × m cells

Total nodes in worst case = 4^(n×m)

Note: X marks invalid moves (out of bounds, visited, or blocked)
      Actual branches are pruned by base cases
```

### Space Complexity: O(n × m)

**Components:**

1. **Recursive call stack:** O(n × m) in worst case
2. **Visited hash set:** O(n × m) maximum size

**Total:** O(n × m)

**Space Usage Visualization:**

```
Call Stack (worst case path length):
┌─────────────────┐
│ dfs(3,3) ← Top  │  ← Currently executing
├─────────────────┤
│ dfs(3,2)        │
├─────────────────┤
│ dfs(2,2)        │
├─────────────────┤
│ dfs(1,2)        │
├─────────────────┤
│ dfs(0,2)        │
├─────────────────┤
│ dfs(0,1)        │
├─────────────────┤
│ dfs(0,0) ← Base │  ← Initial call
└─────────────────┘
Max depth = n × m cells

Visited Set (at deepest point):
visit = {(0,0), (0,1), (0,2), (1,2), (2,2), (3,2), (3,3)}
Max size = n × m cells (if path visits all cells)
```

---

## Key Takeaways

1. **Matrix DFS** extends tree DFS to 2D grids with directional movement
2. **Backtracking** is essential for exploring all possible paths
3. **Visited tracking** prevents infinite loops and duplicate path counting
4. **Must remove from visited set** during backtracking to allow alternative paths
5. **Exponential time complexity** due to exploring all possible path combinations
6. **Hash set** provides optimal O(1) operations for visited tracking