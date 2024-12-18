# 74. Search a 2D Matrix

## Problem

You are given an `m x n` integer matrix `matrix` with the following two properties:

1. Each row is sorted in non-decreasing order.  
2. The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if the target exists in the matrix or `false` otherwise.

You must write a solution with **O(log(m * n))** time complexity.

---

## Examples

### **Example 1**

**Input:**  
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]] target = 3

**Output:**  
true

---

### **Example 2**

**Input:**  
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]] target = 13


**Output:**  
false
