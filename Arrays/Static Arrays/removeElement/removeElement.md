# 27. Remove Element

**Difficulty**: Easy  
**Topics**: Arrays, Two Pointers  
**Companies**: Common FAANG question

---

## Problem Statement

Given an integer array `nums` and an integer `val`, remove **all occurrences** of `val` in-place. The **order of the elements may be changed**. Then return the **number of elements** in `nums` which are **not equal to** `val`.

---

## Requirements

Let the number of elements in `nums` that are not equal to `val` be `k`. To get accepted, your solution must:

- Modify the array `nums` such that the first `k` elements of `nums` contain the elements that are **not equal to** `val`.
- The remaining elements in `nums` **do not matter** (they can be anything).
- Return `k`.

---

## Custom Judge

The judge will test your solution using the following logic:

```java
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer (length == k), sorted and without `val`.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort only the first k elements
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
