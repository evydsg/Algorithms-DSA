# 🟦 Matrix BFS (2D Grid)

## ✅ What is Matrix BFS?

**Breadth-First Search (BFS)** can run on a **matrix (2D grid)** and is most commonly used to find the **shortest path** in an **unweighted graph**.

In a grid, each cell is treated like a node in a graph, and edges exist between adjacent cells (usually 4-directional).

**Movement allowed:**

- Right, Left, Down, Up (no diagonals)

---

## 🎯 Problem

**Q:** Find the **length of the shortest path** from the **top-left** `(0, 0)` to the **bottom-right** `(ROWS-1, COLS-1)`.

- `0` = open cell
- `1` = blocked cell
- You cannot go out of bounds
- You cannot visit the same cell twice

---

## 🗺 Example Grid

```python
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]
```

---

# 🧭 Diagram 1 — Grid Layout

Legend:

- `S` = Start
- `E` = End
- `X` = Blocked (`1`)
- `0` = Open

```
   c0  c1  c2  c3
r0  S   0   0   0
r1  X   X   0   0
r2  0   0   0   X
r3  0   X   0   E
```

---

# ⚙️ BFS Setup (Initial Code)

We need:

- **ROWS, COLS** for bounds
- **visit set** to prevent revisits
- **queue (deque)** for level-order traversal

```python
from collections import deque

def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()

    queue.append((0, 0))
    visit.add((0, 0))
```

---

## ✅ Why BFS Works for Shortest Path

BFS explores **level by level**:

- All nodes at distance `0`
- Then all nodes at distance `1`
- Then `2`, `3`, ...

So the **first time you reach the target**, it’s guaranteed to be the shortest path.

---

# 🧭 Diagram 2 — Directions (4-way movement)

When at `(r, c)`:

```
        (r-1, c)
            ↑
(r, c-1) ← (r,c) → (r, c+1)
            ↓
        (r+1, c)
```

Code:

```python
neighbors = [
    [0, 1],   # right
    [0, -1],  # left
    [1, 0],   # down
    [-1, 0]   # up
]
```

---

# 🔄 BFS Core Logic (Level by Level)

We track `length` = distance from start.

### Key Pattern

- Process the queue **one level at a time**
- Each level adds +1 to `length`

```python
length = 0
while queue:
    for _ in range(len(queue)):
        r, c = queue.popleft()

        if r == ROWS - 1 and c == COLS - 1:
            return length

        neighbors = [[0,1], [0,-1], [1,0], [-1,0]]
        for dr, dc in neighbors:
            new_r, new_c = r + dr, c + dc

            if (min(new_r, new_c) < 0 or
                new_r == ROWS or
                new_c == COLS or
                (new_r, new_c) in visit or
                grid[new_r][new_c] == 1):
                continue

            queue.append((new_r, new_c))
            visit.add((new_r, new_c))

    length += 1
```

---

## ✅ Important Detail: Mark visited when ENQUEUED

```python
queue.append((new_r, new_c))
visit.add((new_r, new_c))
```

This ensures:

- No duplicates in the queue
- Each cell processed at most once
- More efficient BFS

---

# 🧩 Full BFS Code (Tied Together)

```python
from collections import deque

def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()

    queue.append((0, 0))
    visit.add((0, 0))

    length = 0

    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()

            # Goal check
            if r == ROWS - 1 and c == COLS - 1:
                return length

            neighbors = [[0,1], [0,-1], [1,0], [-1,0]]
            for dr, dc in neighbors:
                new_r, new_c = r + dr, c + dc

                # Invalid moves
                if (min(new_r, new_c) < 0 or
                    new_r == ROWS or
                    new_c == COLS or
                    (new_r, new_c) in visit or
                    grid[new_r][new_c] == 1):
                    continue

                queue.append((new_r, new_c))
                visit.add((new_r, new_c))

        length += 1

    return -1  # no path exists
```

---

# 🌊 Diagram 3 — BFS Level Expansion Example

We show the **distance number** BFS assigns (levels).

### Level 0

```
S  .  .  .
X  X  .  .
.  .  .  X
.  X  .  E
```

### Level 1

```
S  1  .  .
X  X  .  .
.  .  .  X
.  X  .  E
```

### Level 2

```
S  1  2  .
X  X  .  .
.  .  .  X
.  X  .  E
```

### Level 3

```
S  1  2  3
X  X  3  .
.  .  .  X
.  X  .  E
```

### Level 4

```
S  1  2  3
X  X  3  4
.  .  4  X
.  X  .  E
```

### Level 5

```
S  1  2  3
X  X  3  4
.  5  4  X
.  X  5  E
```

### Level 6 (Reached End 🎯)

```
S  1  2  3
X  X  3  4
.  5  4  X
.  X  5  6
```

✅ Shortest Path Length = **6**

---

# 🧠 Diagram 4 — BFS Flowchart

```
Start
  ↓
Initialize queue + visit
  ↓
length = 0
  ↓
While queue not empty:
    ↓
    Process all nodes in current level
        ↓
        If target found → return length
        ↓
        Add valid neighbors to queue
    ↓
    length += 1
  ↓
Return -1 (no path)
```

---

# ⏱ Complexity

## Time Complexity

Each cell is visited at most once.

If:

- `n` = rows
- `m` = columns

✅ **O(n × m)**

## Space Complexity

Worst case, the queue + visited set can store all cells.

✅ **O(n × m)**

---

# 🆚 BFS vs DFS in a Grid

| Feature | BFS | DFS |
| --- | --- | --- |
| Finds shortest path | ✅ Yes | ❌ Not guaranteed |
| Traversal style | Level by level | Deep first |
| Uses | Queue | Stack / recursion |
| Best for | Shortest path | Full exploration |