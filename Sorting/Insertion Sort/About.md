# Insertion Sort Overview

Insertion Sort is a simple and intuitive sorting algorithm that builds the final sorted array one element at a time. It works by dividing the list into two parts: the sorted portion and the unsorted portion. Initially, the sorted portion contains just the first element.

## How It Works:
1. Start with the second element (index 1) as the "key" and compare it to the elements in the sorted portion to its left.
2. Shift elements in the sorted portion one position to the right to make space for the key if they are larger than the key.
3. Insert the key into its correct position within the sorted portion.
4. Repeat the process for all elements until the entire array is sorted.

## Example:
**Input**: `[5, 3, 4, 1, 2]`

1. Start with the second element `3` and compare it with `5`. Insert `3` before `5`.  
   **Array**: `[3, 5, 4, 1, 2]`

2. Take `4` and insert it between `3` and `5`.  
   **Array**: `[3, 4, 5, 1, 2]`

3. Take `1` and insert it at the beginning.  
   **Array**: `[1, 3, 4, 5, 2]`

4. Take `2` and insert it after `1`.  
   **Array**: `[1, 2, 3, 4, 5]`

## Key Points:
- **Time Complexity**: 
  - Worst Case: `O(n^2)` (repeated shifting of elements). 
  - Best Case: `O(n)` (nearly sorted arrays).
- **Space Complexity**: `O(1)` (in-place sorting).
- **Best Use Case**: Small datasets or nearly sorted arrays.
