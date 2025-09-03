
# 🌳 Binary Search Trees (BST)

## 📌 Binary Trees vs Binary Search Trees

- **Binary Tree**: A hierarchical data structure where each node has at most two children (left and right).
- **Binary Search Tree (BST)**: A special type of binary tree with an additional property:
  - All nodes in the **left subtree** are **smaller** than the root.
  - All nodes in the **right subtree** are **greater** than the root.
  - This property applies **recursively** to every node in the tree.

> Think of BSTs as analogous to a sorted array.

---

## 🎯 Motivation

- Searching in a BST takes **O(log n)** (like binary search on a sorted array).
- Unlike arrays, BSTs allow:
  - **Insertion** in O(log n)
  - **Deletion** in O(log n)
- In contrast, insertions/deletions in arrays take **O(n)**.

---

## 🔎 BST Search Algorithm

**Idea**: Similar to binary search:

- If the target is smaller → search left subtree.
- If the target is larger → search right subtree.
- If equal → target found.
- If we reach a null node → target does not exist.

### Example Tree

```

```
    2
   / \
  1   3
       \
        4
```

````

**Target = 3**

- Compare with root (2). Since 3 > 2, go right.
- Compare with node (3). Match found ✅.

---

## 📝 Implementation (Recursive)

```python
def search(root, target):
    if not root:
        return False

    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True
````

### Key Points

1. **Base Cases**

   * If node is `null` → return False (target not found).
   * If node value == target → return True.

2. **Recursive Calls**

   * If target > node → search right subtree.
   * If target < node → search left subtree.

---

## 🕒 Time Complexity

* **Balanced BST**:

  * Height ≈ log n
  * Search, insert, delete = **O(log n)**
* **Skewed BST** (like a linked list):

  * Height ≈ n
  * Worst case operations = **O(n)**

---

## 📦 Space Complexity (Recursive)

* **Balanced BST**: O(log n) (due to recursion stack).
* **Skewed BST**: O(n).

---

## 📝 Implementation (Iterative)

```python
def search(root, target):
    current = root
    
    while current:
        if target > current.val:
            current = current.right
        elif target < current.val:
            current = current.left
        else:
            return True  # Target found
    return False  # Target not found
```

---

## 🕒 Time Complexity (Iterative)

* **Balanced BST**:

  * Height ≈ log n
  * Search, insert, delete = **O(log n)**
* **Skewed BST**:

  * Height ≈ n
  * Worst case operations = **O(n)**

---

## 📦 Space Complexity (Iterative)

* **O(1)** (no recursion stack used).

---

## 📊 Summary

* BSTs combine the **search efficiency** of sorted arrays with the **flexibility** of dynamic insertion and deletion.
* Performance depends heavily on whether the tree is **balanced** or **skewed**.

