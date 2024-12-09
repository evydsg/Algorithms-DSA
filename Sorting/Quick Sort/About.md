# Quick Sort Overview

Quick Sort is a **divide-and-conquer** sorting algorithm that selects a "pivot" element, partitions the array around the pivot, and recursively sorts the subarrays. It is one of the most efficient sorting algorithms in practice due to its average-case performance.

## How It Works:
1. **Pivot Selection**: Choose an element from the array as the pivot. The choice of pivot can vary (e.g., first element, last element, random, or median).
2. **Partitioning**: Rearrange the array such that all elements less than the pivot are on its left and all elements greater than the pivot are on its right.
3. **Recursive Sorting**: Recursively apply the same steps to the left and right subarrays.

## Example:
**Input**: `[8, 4, 7, 3, 5, 6, 2]`

1. Choose a pivot (e.g., `5`).
2. Partition:
   - Elements less than `5`: `[4, 3, 2]`
   - Pivot: `5`
   - Elements greater than `5`: `[8, 7, 6]`
3. Recursively sort `[4, 3, 2]` and `[8, 7, 6]`:
   - `[4, 3, 2]` → `[2, 3, 4]`
   - `[8, 7, 6]` → `[6, 7, 8]`
4. Combine: `[2, 3, 4] + [5] + [6, 7, 8] = [2, 3, 4, 5, 6, 7, 8]`

## Key Points:
- **Time Complexity**:
  - Best Case: `O(n log n)` (balanced partitioning)
  - Worst Case: `O(n^2)` (highly unbalanced partitioning, e.g., sorted input)
  - Average Case: `O(n log n)`
- **Space Complexity**: `O(log n)` for recursion (in-place sorting).
- **Unstable Sorting**: May not maintain the relative order of equal elements.
- **Best Use Case**: Large datasets with no strict stability requirements.

Quick Sort is preferred for its speed and efficiency, but care must be taken to select a good pivot to avoid the worst-case scenario.
