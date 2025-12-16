# 🌳 Heaps: Push and Pop Operations

A **heap** allows us to efficiently manage elements based on priority.

- The **minimum (Min Heap)** or **maximum (Max Heap)** value is always stored at the **root**
- Reading the root takes **O(1)** time
- Inserting (push) and removing (pop) take **O(log n)** time

---

## ⏱ Time Complexity Overview

| Operation | Time Complexity |
| --- | --- |
| Get Min / Max | **O(1)** |
| Push | **O(log n)** |
| Pop | **O(log n)** |

---

## 📌 Key Reminder

Heaps must always satisfy **two properties**:

1. **Structure Property**
    - The heap is a **complete binary tree**
    - Nodes are filled **left to right**
2. **Order Property**
    - **Min Heap**: Parent ≤ Children
    - **Max Heap**: Parent ≥ Children

---

# ➕ Push Operation (Min Heap)

### Goal

Insert a new value **while keeping both heap properties intact**.

### Steps

1. Add the new value to the **end of the heap**
2. Compare it with its parent
3. **Swap upward (percolate / bubble up)** until the order property is restored

---

### 🔍 Example: Pushing `17`

Initial heap (array representation):

```
[14, 19, 16, 21, 26, 19, 68, 65, 30]

```

- Insert `17` at index **10**
- Compare with parent `26` → swap
- Compare with parent `19` → swap
- Compare with parent `14` → stop (heap property restored)

---

### 🧠 Push Code (Min Heap)

```python
def push(self, val):
    self.heap.append(val)
    i = len(self.heap) - 1

    # Percolate up
    while i > 1 and self.heap[i] < self.heap[i // 2]:
        self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
        i = i // 2

```

📌 `//` is **floor division**, used because heap indices must be integers.

---

### ⏱ Push Complexity

- Tree height = **log n**
- Worst-case swaps = height of tree
    
    ✅ **O(log n)**
    

---

## 🔄 Max Heap Push

Same logic as Min Heap, **but comparisons are reversed**:

- Swap when `child > parent`

---

# ➖ Pop Operation (Min Heap)

### Goal

Remove the **minimum element (root)** while keeping the heap valid.

---

## ❌ The Wrong Way

- Removing root and replacing it with the smaller child
- ❌ Breaks the **structure property**
- Leads to missing nodes in the tree

---

## ✅ The Correct Way (Heapify Down)

### Steps

1. Save the root value (this is what we return)
2. Move the **last element** to the root
3. **Percolate down (heapify)**:
    - Swap with the smaller child
    - Continue until the order property is restored

---

### 🧠 Pop Code (Min Heap)

```python
def pop(self):
    if len(self.heap) == 1:
        return None
    if len(self.heap) == 2:
        return self.heap.pop()

    res = self.heap[1]
    self.heap[1] = self.heap.pop()
    i = 1

    # Percolate down
    while 2 * i < len(self.heap):
        if (2 * i + 1 < len(self.heap) and
            self.heap[2 * i + 1] < self.heap[2 * i] and
            self.heap[i] > self.heap[2 * i + 1]):
            self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]
            i = 2 * i + 1
        elif self.heap[i] > self.heap[2 * i]:
            self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
            i = 2 * i
        else:
            break

    return res

```

---

### 🧠 Why This Works

- Moving the last element preserves the **complete tree**
- Percolating down restores the **order property**
- A node can have:
    - No children
    - Only a **left child**
    - Two children
        
        ⚠️ A right-only child is impossible in a heap
        

---

### ⏱ Pop Complexity

- At most one swap per level
- Height of heap = **log n**
    
    ✅ **O(log n)**
    

---

## 🔄 Max Heap Pop

Same process, but:

- Swap with the **larger child**
- Maintain `parent ≥ children`

---

# 🧾 Final Summary

| Operation | Explanation |
| --- | --- |
| Get Min / Max | Read root |
| Push | Insert → bubble up |
| Pop | Replace root → heapify down |
| Efficiency | Balanced tree → log height |