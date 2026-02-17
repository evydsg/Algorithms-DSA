
# Max Area of Island

## Problem

You are given a 2D matrix `grid` where each cell is:

* `0` → water
* `1` → land

An **island** is a group of `1`s connected **horizontally or vertically** (NOT diagonally).

The **area of an island** = total number of land cells (`1`s) in that island.

All edges of the grid are surrounded by water.

### Goal

Return the **maximum area** of any island in the grid.
If there are no islands, return `0`.

---

## Example

### Input

```text
grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]
```

### Output

```text
6
```

### Explanation

Cells connect only **up, down, left, right**.

Diagonal connections do NOT count.

The largest connected group of `1`s contains **6 cells** → so the answer is `6`.

---

## Constraints

* `1 <= grid.length <= 50`
* `1 <= grid[i].length <= 50`

---

## Key Observations

This is a **graph traversal problem** disguised as a grid problem.

Each cell = a node.

We must:

1. Find a land cell (`1`)
2. Explore the entire island
3. Count its size
4. Keep the maximum


