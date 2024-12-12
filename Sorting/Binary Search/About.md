# Binary Search Algorithm on Arrays

Binary Search is an efficient searching algorithm that works on sorted arrays by repeatedly dividing the search interval in half. It is based on the divide-and-conquer strategy.

---

## Key Features of Binary Search

- **Precondition**: The array must be sorted.
- **Efficiency**: Operates in O(log n) time complexity.
- **Methodology**: Compares the target value to the middle element, then narrows down the search space.

---

## How Binary Search Works

1. **Initialization**:
   - Define two pointers: `low` (start of the array) and `high` (end of the array).

2. **Iterative/Recursive Search**:
   - Calculate the middle index: `mid = low + (high - low) // 2`.
   - Compare the target value with `arr[mid]`:
     - If `arr[mid] == target`: Target found, return the index.
     - If `arr[mid] < target`: Narrow the search to the right half (`low = mid + 1`).
     - If `arr[mid] > target`: Narrow the search to the left half (`high = mid - 1`).

3. **Repeat**:
   - Continue until `low > high` or the target is found.

4. **Output**:
   - If the target is found, return its index.
   - If not found, return -1.

---

## Example of Binary Search

### Input
```text
Array: [2, 4, 7, 10, 15, 20, 25]
Target: 10
