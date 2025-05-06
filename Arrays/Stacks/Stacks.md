
# 🥞 Stacks – Data Structure

A **stack** is a linear data structure that allows elements to be **added** or **removed** only from **one end** — called the **top**.

---

## 📌 Real-World Analogy

Think of a **stack of plates**:

![Stack Data Structure](assets/stack_diagram.png)


You can:
- Add a plate to the **top**
- Remove a plate from the **top**
- You **cannot** insert/remove from the middle

---

## ⚙️ Stack Characteristics

- **Dynamic** structure (grows/shrinks as needed)
- **LIFO**: Last In, First Out
- Can be implemented using a dynamic array (like a list in Python)

---

## 🔁 Operations

### 1. Push – Add to the top

**Pseudocode:**
```python
def push(self, n):
    self.stack.append(n)
````

**Visual Example (pushing 1, 2, 3, 4):**

```
Push(1)  -> [1]
Push(2)  -> [1, 2]
Push(3)  -> [1, 2, 3]
Push(4)  -> [1, 2, 3, 4] <- Top
```

🕒 **Time Complexity**: `O(1)`

---

### 2. Pop – Remove from the top

**Pseudocode:**

```python
def pop(self):
    return self.stack.pop()
```

✅ Always check if the stack is empty before popping.

**Visual Example:**

```
Before: [1, 2, 3, 4] <- Top
Pop()  -> returns 4

After:  [1, 2, 3] <- Top
```

🕒 **Time Complexity**: `O(1)`

---

### 3. Peek – View the top without removing

**Pseudocode:**

```python
def peek(self):
    return self.stack[-1]
```

**Visual Example:**

```
Stack: [1, 2, 3, 4]
Peek() -> returns 4
```

🕒 **Time Complexity**: `O(1)`

---

## 🧠 Use Cases

* Undo/Redo functionality
* Reversing strings
* Expression parsing
* Navigation history (browser back/forward)

---

## ⏱️ Time Complexity Summary

| Operation | Time Complexity | Notes                                |
| --------- | --------------- | ------------------------------------ |
| Push      | `O(1)`          | Add to top                           |
| Pop       | `O(1)`          | Remove from top (check if not empty) |
| Peek      | `O(1)`          | View top without removing            |

---

