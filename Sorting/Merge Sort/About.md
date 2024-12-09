# Merge Sort Overview

Merge Sort is a **divide-and-conquer** sorting algorithm that divides the input array into smaller subarrays, sorts them, and then merges the sorted subarrays to produce the final sorted array. It is highly efficient and works well for large datasets.

## How It Works:
1. **Divide**: Recursively divide the array into two halves until each subarray contains a single element (or is empty).
2. **Conquer**: Sort the individual subarrays as they are merged back together.
3. **Merge**: Combine the sorted subarrays into a single sorted array by comparing elements from each subarray.

## Example:
**Input**: `[8, 4, 5, 7, 1, 3, 6, 2]`

1. **Divide**: Split into halves recursively:  
   `[8, 4, 5, 7]` and `[1, 3, 6, 2]`, then `[8, 4]`, `[5, 7]`, etc.

2. **Conquer**: Sort individual elements as they are merged:  
   - Merge `[8]` and `[4]` into `[4, 8]`.
   - Merge `[5]` and `[7]` into `[5, 7]`.

3. **Merge**: Combine sorted subarrays:  
   - Merge `[4, 8]` and `[5, 7]` into `[4, 5, 7, 8]`.
   - Similarly, merge `[1, 3, 6, 2]` into `[1, 2, 3, 6]`.
   - Finally, merge `[4, 5, 7, 8]` and `[1, 2, 3, 6]` into `[1, 2, 3, 4, 5, 6, 7, 8]`.

## Key Points:
- **Time Complexity**:
  - Worst Case: `O(n log n)`
  - Best Case: `O(n log n)`
  - Average Case: `O(n log n)`
- **Space Complexity**: `O(n)` due to auxiliary space for merging.
- **Stable Sorting**: Maintains the relative order of equal elements.
- **Best Use Case**: Large datasets or when stability is required.

Merge Sort is highly efficient but requires additional memory for merging, which can be a limitation for very large datasets.
