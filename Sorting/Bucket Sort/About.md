# Bucket Sort Algorithm

Bucket Sort is a comparison-free sorting algorithm that divides an array into several buckets and then sorts these buckets individually. It is particularly useful when the input is uniformly distributed over a range.

---

## How Bucket Sort Works

1. **Create Buckets**: Divide the range of input data into a fixed number of buckets.
2. **Distribute Elements**: Place each element into the appropriate bucket based on its value.
3. **Sort Individual Buckets**: Sort each bucket, usually using another sorting algorithm like Insertion Sort.
4. **Concatenate Buckets**: Merge all sorted buckets to form the final sorted array.

---

## Steps of Bucket Sort

1. **Initialization**:
   - Determine the number of buckets.
   - Create empty buckets.

2. **Distribution**:
   - Distribute elements into buckets based on a hashing or mapping function.

3. **Sorting**:
   - Sort elements in each bucket.

4. **Concatenation**:
   - Concatenate all the buckets to get the sorted array.

5. **Stable**:
   - It is not stable


---

## Example of Bucket Sort

### Input
```text
Array: [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
Number of Buckets: 5
