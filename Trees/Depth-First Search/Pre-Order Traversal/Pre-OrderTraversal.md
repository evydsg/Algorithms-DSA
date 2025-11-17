### 🧠 **Depth-First Search (Pre-Order Traversal)**

### **Traversal Order**

`root → left → right`

In a **pre-order traversal**, the algorithm visits the parent node first, then the left subtree, and finally the right subtree.

---

### **Recursive Implementation**

```python
def preOrder(root):
    if not root:
        return

    print(root.val)
    preOrder(root.left)
    preOrder(root.right)

```

---

### **Iterative Implementation (Using Stack)**

```python
def preOrder(root):
    if not root:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.val)

        # Push right first so left is processed next
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

```

🧩 **Explanation:**

- A stack is used to simulate recursion.
- The right child is pushed first so that the left child is processed before the right (LIFO behavior).

---

### **Example Output**

If the binary tree is structured as below:

```
       4
      / \
     3   6
    /   / \
   2   5   7

```

➡️ **Pre-order Traversal Result:**

`[4, 3, 2, 6, 5, 7]`

[In-order Traversal](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/9388095e-8f09-4725-fc1d-27988a291c00/sharpen=1)

📘 [In-order Traversal](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/9388095e-8f09-4725-fc1d-27988a291c00/sharpen=1)