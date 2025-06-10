# 📦 Implement Stack Using Queues

## 📝 Problem Statement

Design a **stack** using only **two queues**. The stack must support typical LIFO operations:

### Required Methods:

* `push(x)` – Push element `x` to the top of the stack.
* `pop()` – Removes and returns the element on the top of the stack.
* `top()` – Returns the top element without removing it.
* `empty()` – Returns `True` if the stack is empty, `False` otherwise.

> Only standard **queue operations** are allowed:

* `push to back`
* `pop from front`
* `peek at front`
* `size`
* `isEmpty`

---

## 🛠️ Approach

We use **two queues**:

* `q1`: Main queue to maintain the stack order.
* `q2`: Temporary queue used during the `push` operation to reorder elements.

When pushing a new element:

1. Push to `q2`.
2. Move all elements from `q1` to `q2` to simulate LIFO order.
3. Swap the names of `q1` and `q2`.

This keeps the **most recently added element** at the **front of `q1`**, emulating a stack.

---

## 🧪 Example

```text
Input:  ["MyStack", "push", "push", "top", "pop", "empty"]
        [[],       [1],    [2],    [],    [],     []]

Output: [null, null, null, 2,     2,     false]
```

---

## 🧑‍💻 Python Code

```python
from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1
```

---

## ⏱️ Time Complexity

| Operation | Time Complexity |
| --------- | --------------- |
| `push()`  | O(n)            |
| `pop()`   | O(1)            |
| `top()`   | O(1)            |
| `empty()` | O(1)            |

---

## ✅ Constraints

* `1 <= x <= 9`
* Max 100 calls to `push`, `pop`, `top`, and `empty`
* All `pop` and `top` calls are guaranteed to be valid (stack not empty)
