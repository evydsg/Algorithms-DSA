🔁 Recursion (One Branch)

Recursion can be a tricky concept at first, so don’t worry if it doesn’t click right away. Let’s break it down.

## 📌 What Is Recursion?

**Recursion** is when a function calls itself to solve smaller versions of a problem. A recursive function typically includes:

1. **Base case** – The stopping condition.
2. **Recursive case** – The part where the function calls itself with a smaller input.

Think of it like **a box inside a box inside another box**. The smallest box is the base case; the outer boxes are recursive steps.

---

## 🧠 One-Branch Recursion Example: Factorial

To compute `n!` (n factorial), we multiply all integers from `n` down to `1`.

**Mathematical formula:**

```
n! = n * (n - 1) * (n - 2) * ... * 1
```

**Example:**

```
5! = 5 * 4 * 3 * 2 * 1 = 120
```

Notice the recursive pattern:

```
5! = 5 * 4!
4! = 4 * 3!
...
```

### ✅ Base Case:

`n == 0` or `n == 1` → return `1`

### 🔁 Recursive Case:

`n * factorial(n - 1)`

---

## 🧪 Code Example

```python
# Recursive implementation of factorial
def factorial(n):
    # Base case
    if n <= 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)
```

### 🔍 What Happens When `factorial(5)` Is Called?

```text
factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1  ← base case reached
= 120
```

Once the base case is reached, the stack "unwinds" and each function call returns its result.

---

## ⏱ Time and Space Complexity

* **Time Complexity:** `O(n)`
  → `n` recursive calls, each doing `O(1)` work.

* **Space Complexity:** `O(n)`
  → Due to the call stack (not explicit data structures), `n` frames are on the stack.

---

## 🔁 Iterative Version

Recursion isn’t always necessary — many recursive problems can be solved iteratively.

```python
n = 5
res = 1

while n > 1:
    res *= n
    n -= 1

print(res)  # Output: 120
```

### 🧠 Iteration vs Recursion

| Feature     | Recursion                    | Iteration                      |
| ----------- | ---------------------------- | ------------------------------ |
| Structure   | Function calls itself        | Uses loops                     |
| Space usage | Higher (due to call stack)   | Lower (uses constant space)    |
| Simplicity  | Often elegant, but tricky    | Sometimes easier to understand |
| Performance | Slower due to stack overhead | Faster for simple tasks        |

---

## ✅ Key Takeaways

* Every recursive function must have a **base case**.
* Think of recursion as solving **sub-problems**, then combining the results.
* **Stack overflow** occurs if a recursive function has no base case.
* **Recursion is especially powerful for tree problems**, where iterative solutions can get messy.