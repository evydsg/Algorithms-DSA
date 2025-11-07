# 🌳 **94. Binary Tree Inorder Traversal**

**Difficulty:** 🟢 Easy
**Topics:** Binary Tree, Depth-First Search (DFS), Stack, Recursion
**Companies:** 🏢 Common interview question (Google, Amazon, Microsoft, etc.)

---

## 🧠 **Problem Statement**

Given the **root** of a binary tree, return the **inorder traversal** of its nodes' values.

---

## 🧾 **Examples**

### **Example 1**

```python
Input: root = [1, null, 2, 3]
Output: [1, 3, 2]
```

**Explanation:**
Inorder traversal visits nodes in the order: Left → Root → Right.

---

### **Example 2**

```python
Input: root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]
Output: [4, 2, 6, 5, 7, 1, 3, 9, 8]
```

**Explanation:**
The traversal starts from the leftmost node and visits all nodes in inorder sequence.

---

### **Example 3**

```python
Input: root = []
Output: []
```

---

### **Example 4**

```python
Input: root = [1]
Output: [1]
```

---

## ⚙️ **Constraints**

* The number of nodes in the tree is in the range **[0, 100]**
* Each node’s value is between **-100 ≤ Node.val ≤ 100**

---

✅ **Goal:**
Return a list of all nodes’ values in **inorder traversal** order — **Left → Root → Right**.
