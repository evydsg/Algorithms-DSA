# 🌿 Recursion (Two-Branch)

A more common case of recursion is **multi-branch recursion**, where a function makes more than one recursive call. A classic example is the **Fibonacci sequence**.

---

## 🧠 What is the Fibonacci Sequence?

- A series of numbers where each number is the sum of the two preceding ones.
- Starts with:  
  `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...`

---

## 🧾 Mathematical Definition

- **Base cases**:
  - `F(0) = 0`  
  - `F(1) = 1`
- **Recursive case**:  
  - `F(n) = F(n - 1) + F(n - 2)`

---

## 🧮 Recursive Formula (Recurrence Relation)

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
````

* This is a **two-branch recursive function**, since it calls itself twice.
* Each call breaks the problem down further until it hits a base case (`n = 0 or 1`).
* Once the base case is reached, the results "bubble up" to compute the final answer.

---

## 🌳 Visualizing Recursion as a Tree

To calculate `fibonacci(5)`:

* `fibonacci(5)` calls:

  * `fibonacci(4)` + `fibonacci(3)`

    * `fibonacci(4)` → `fibonacci(3)` + `fibonacci(2)`
    * ...
* This continues recursively until we reach base cases.
* Once all base cases return, we add up the results going back up the tree.
* Final result: `fibonacci(5) = 5`

---

## ⏱ Time & Space Complexity

### 🕒 Time Complexity

* The recursion tree doubles at each level.
* Number of calls:

  ```
  1 + 2 + 4 + 8 + ... + 2^n ≈ 2^(n+1) - 1
  ```
* **Time Complexity: `O(2^n)`**

### 💾 Space Complexity

* The space used is proportional to the **maximum height of the recursion tree**.
* Since the deepest call chain is `n`, the **space complexity is `O(n)`** (due to the call stack).

---

## ✅ Key Takeaways

* Two-branch recursion is **inefficient for large `n`** due to repeated calculations.
* Can be optimized with **memoization** or **dynamic programming**.
* Fibonacci is an excellent case for understanding recursive call trees and exponential time complexity.

