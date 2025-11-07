# 🌳 In-Order Traversal (DFS)

### Traversal Order

**Left → Root → Right**

### Key Points

* Visits nodes in **sorted order** (for Binary Search Trees).
* Can be implemented **recursively** or **iteratively**.
* Part of **Depth-First Search (DFS)**.

---

## 🧩 Recursive Approach

```python
def inorder(root):
    if not root:
        return
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)
```

### Explanation

1. Traverse the **left** subtree.
2. Visit the **root** node.
3. Traverse the **right** subtree.

---

## ⚙️ Iterative Approach

```python
def inorder_iterative(root):
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.val)
        current = current.right
```

### 🧠 Step-by-Step

* Use a **stack** to simulate recursion.
* Keep going **left** until `None`.
* **Pop** from the stack (visit node).
* Move **right** after visiting.

---

### ⏱️ Complexity

| Type      | Complexity                        |
| --------- | --------------------------------- |
| **Time**  | O(n) — every node is visited once |
| **Space** | O(n) — stack holds nodes          |

---

# 🔍 Depth-First Search (DFS)

**Depth First Search (DFS)** is one of the most common algorithms in coding interviews. It’s used to traverse **trees** and **graphs**.

When applied to trees, the idea is simple:

* Pick a direction (e.g., **left**).
* Keep going **as deep as possible** until you reach `None`.
* Then **backtrack** and explore the right side.

This is the essence of DFS — we go **deep before wide**.

---

## 🌲 DFS Traversal Types

There are **three main DFS traversals** for binary trees:

1. **Inorder** → Left → Root → Right
2. **Preorder** → Root → Left → Right
3. **Postorder** → Left → Right → Root

> DFS is most naturally implemented using **recursion**,
> but can also be done **iteratively** using a stack.

---

# 🧮 In-Order Traversal (Detailed View)

An **inorder traversal** recursively visits:

1. All nodes in the **left subtree**
2. The **current (parent)** node
3. All nodes in the **right subtree**

Here’s the recursive implementation again:

```python
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
```

---

### 🧩 Example Output

If the tree structure is a **BST**:

```
        5
       / \
      3   7
     / \  / \
    2  4 6  8
```

Then the **inorder traversal** prints:

```
[2, 3, 4, 5, 6, 7, 8]
```

---

### 💡 Why Sorted?

Because of the **BST property**:

* All nodes in the **left subtree** are smaller.
* All nodes in the **right subtree** are larger.

We won’t hit the base case until we reach the **leftmost (smallest)** node. Then we move up and visit parent nodes in ascending order.

---

> 🖼️ **Visual Reference:**
> [In-Order Traversal Diagram](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/e8717d2e-69c7-4ec2-ce9c-6d8753d3cc00/sharpen=1)
>
> The numbers in blue represent the order in which the nodes are visited.