

# 🧩 Concatenation of Array

You are given an integer array `nums` of length `n`. Create an array `ans` of length `2n` where:

* `ans[i] == nums[i]`
* `ans[i + n] == nums[i]`

for `0 <= i < n` (0-indexed).
Specifically, `ans` is the **concatenation of two** `nums` **arrays**.

Return the array `ans`.

---

## 📥 Input:

* An integer array `nums` of length `n`.

## 📤 Output:

* An integer array `ans` of length `2n` such that it is the result of concatenating `nums` with itself.

---

## 🧪 Examples:

### Example 1:

```java
Input: nums = [1,4,1,2]
Output: [1,4,1,2,1,4,1,2]
```

### Example 2:

```java
Input: nums = [22,21,20,1]
Output: [22,21,20,1,22,21,20,1]
```

---

## 📌 Constraints:

* `1 <= nums.length <= 1000`
* `1 <= nums[i] <= 1000`
