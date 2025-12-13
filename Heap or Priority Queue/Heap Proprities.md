# Heap Properties

A **heap** is a specialized **tree-based data structure** commonly used to implement a **Priority Queue**.

A **Priority Queue** differs from a normal queue:

- A normal queue removes items in **FIFO** order (First In, First Out)
- A priority queue removes the element with the **highest priority**, regardless of insertion order

> Because heaps are the most common way to implement priority queues, the terms “heap” and “priority queue” are sometimes used interchangeably.
> 

---

## Types of Heaps

### 🔹 Min Heap

- The **smallest value** is always at the **root**
- The smallest value has the **highest priority**

### 🔹 Max Heap

- The **largest value** is always at the **root**
- The largest value has the **highest priority**

![Image](https://media.geeksforgeeks.org/wp-content/uploads/20241104005325856119/min-heap-1.webp?utm_source=chatgpt.com)

![Image](https://static-assets.codecademy.com/Courses/CS102-Data-Structures-And-Algorithms/Heaps/Max-Heap-As-Array-Diagram.svg?utm_source=chatgpt.com)

> In this lesson, we focus on min heaps, but the logic is identical for max heaps—only the comparison direction changes.
> 

---

## Heap Properties

For a binary tree to qualify as a **heap**, it must satisfy **two properties**.

---

### 1️⃣ Structure Property (Complete Binary Tree)

A binary heap must be a **complete binary tree**:

- Every level is **fully filled**
- Except possibly the **last level**
- Nodes on the last level are filled **left to right**, with no gaps

![Image](https://deen3evddmddt.cloudfront.net/uploads/content-images/what-is-complete-binary-tree.webp?utm_source=chatgpt.com)

![Image](https://gtl.csa.iisc.ac.in/dsa/img158.gif?utm_source=chatgpt.com)

✔ This structure keeps the tree compact and balanced

❌ Missing nodes in the middle are **not allowed**

---

### 2️⃣ Order Property

### Min Heap Order Property

- Every **parent ≤ its children**
- All descendants are **greater than or equal to** their ancestors

### Max Heap Order Property

- Every **parent ≥ its children**

![Image](https://media.geeksforgeeks.org/wp-content/uploads/20241105101737867907/min-heap-1.webp?utm_source=chatgpt.com)

![Image](https://static-assets.codecademy.com/Courses/CS102-Data-Structures-And-Algorithms/Heaps/Max-Heap-As-Array-Diagram.svg?utm_source=chatgpt.com)

📌 Notes:

- The property is **recursive** (applies at every subtree)
- Heaps **can contain duplicate values**
- Unlike Binary Search Trees, heaps are **not sorted**

---

## Heap Implementation

Although heaps are **conceptually trees**, they are **implemented using arrays**.

Why?

- Heaps are complete binary trees
- No pointers are needed
- Parent/child relationships can be calculated using math

---

## Array Representation of a Heap

We store heap elements using **level-order traversal** (Breadth-First Search):

- Top → bottom
- Left → right
- No gaps

![Image](https://www.cse.hut.fi/en/research/SVG/TRAKLA2/tutorials/heap_tutorial/KekoTRAKLA-89_1.gif?utm_source=chatgpt.com)

![Image](https://media.geeksforgeeks.org/wp-content/uploads/20240507172156/Level-Order-Traversal-of-Binary-Tree-768.webp?utm_source=chatgpt.com)

We use an array of size **n + 1**, where:

- `n` = number of nodes
- Index `0` is unused

This approach is called **one-based indexing**.

---

## One-Based Indexing

We start storing values at **index 1**, not index 0.

### Why?

For a node at index `i`:

```
Left Child  = 2 * i
Right Child = 2 * i + 1
Parent      = i // 2

```

![Image](https://www.cse.hut.fi/en/research/SVG/TRAKLA2/tutorials/heap_tutorial/KekoTRAKLA-89_1.gif?utm_source=chatgpt.com)

![Image](https://i.imgur.com/VHtiUsL.png?utm_source=chatgpt.com)

These formulas work **only because**:

- The tree is complete
- The array is filled contiguously
- Indexing starts at 1

❌ Starting at index 0 would break the math (e.g., `2 * 0 = 0`).

---

## Example: Finding Parent and Children

If a node with value **19** is stored at index `i`:

- Parent → `i // 2`
- Left child → `2 * i`
- Right child → `2 * i + 1`

![Image](https://media.geeksforgeeks.org/wp-content/uploads/20250324101433667420/Representation-of-a-Binary-Heap.webp?utm_source=chatgpt.com)

![Image](https://www.cs.dartmouth.edu/~cs10/notes/14/img/heap-example.png?utm_source=chatgpt.com)

The blue numbers above nodes represent their **array indices**.

---

## Heap Initialization (Code)

```python
class Heap:
    def __init__(self):
        self.heap = [0]  # index 0 is unused

```

This setup enables:

- Clean math for parent/child access
- Efficient insert and remove operations

---

### ✅ Quick Summary (Great for Interviews)

- Heap = tree-based structure for priority queues
- Two types: **Min Heap** and **Max Heap**
- Must satisfy:
    - **Structure Property** (complete binary tree)
    - **Order Property**
- Implemented using an **array**
- Uses **one-based indexing** for easy calculations