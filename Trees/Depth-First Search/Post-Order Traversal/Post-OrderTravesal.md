# 🌲 Post-Order Traversal (DFS)

### 🧭 Definition

Post-order traversal visits nodes in the following order:

> Left → Right → Root
> 

It’s typically used for deleting trees, evaluating expressions, or when a parent’s operation depends on its children.

---

## 🧩 Recursive Approach

```python
def postorder(root):
    if not root:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.val)

```

### ✅ Steps

1. Visit the left subtree
2. Visit the right subtree
3. Visit the root node

---

## ⚙️ Iterative Approach (Using One Stack)

```python
def postorder(root):
    if not root:
        return []

    stack = []
    result = []
    last_visited = None
    current = root

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek = stack[-1]
            # Go right if possible and not yet visited
            if peek.right and last_visited != peek.right:
                current = peek.right
            else:
                result.append(peek.val)
                last_visited = stack.pop()

    return result

```

### 🧠 Logic

- Traverse left as much as possible
- Peek at the top of the stack
    - If the right child exists and hasn’t been visited, go right
    - Otherwise, process (visit) the current node

---

## ⏱️ Complexity Analysis

| Type | Complexity | Explanation |
| --- | --- | --- |
| **Time** | `O(n)` | Each node is visited exactly once |
| **Space** | `O(n)` | Stack stores up to all nodes in the worst case |

---

## 🌳 Example

For the tree:

```
      1
     / \
    2   3
   / \
  4   5

```

**Output (Post-order):**

```
[4, 5, 2, 3, 1]

```