# Sort Colors

**Solved**

You are given an array `nums` consisting of `n` elements where each element is an integer representing a color:

- `0` represents **red**
- `1` represents **white**
- `2` represents **blue**

Your task is to sort the array **in-place** such that elements of the same color are grouped together and arranged in the order:  
**red (0)** → **white (1)** → **blue (2)**.

You must **not** use any built-in sorting functions to solve this problem.

---

## Example 1

**Input:**
```python
nums = [1,0,1,2]
````

**Output:**

```python
[0,1,1,2]
```

---

## Example 2

**Input:**

```python
nums = [2,1,0]
```

**Output:**

```python
[0,1,2]
```

---

## Constraints

* `1 <= nums.length <= 300`
* `0 <= nums[i] <= 2`

