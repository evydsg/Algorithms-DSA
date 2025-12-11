# 🌈 Backtracking (Explained Like You’re 5 With Cartoons)

## 🌳 The Tree Problem

Imagine you have a tree made of numbers:

```
      4
     / \
    0   1
       / \
      3   2

```

You want to walk from the **top**🌟 to a **leaf**🍃

without stepping on a number that is **0** ❌.

If you step on a 0 → *no good* 😕

If you reach a leaf safely → *you win!* 🎉

---

# 🪜 How We Walk Through the Tree

1. Start at the root 🌟
2. If the number is **0** → stop and go back ❌🔙
3. If you're at a leaf 🍃 → yay, path found! 🎉
4. Try going **left**⬅️
5. If that doesn’t work, try going **right**➡️
6. If both don’t work → go back up again 🔙

This is exactly what the code does.

---

## 🧠 Code (Simple Version)

```python
def canReachLeaf(root):
    if not root or root.val == 0:  # ❌ hit a wall
        return False

    if not root.left and not root.right:  # 🍃 leaf found
        return True

    if canReachLeaf(root.left):  # ⬅️ try left
        return True
    if canReachLeaf(root.right):  # ➡️ try right
        return True

    return False  # no path found 😕

```

---

# 🎒 Building the Path (Writing Your Steps)

Imagine you have a little notebook 📒.

Every time you step on a number:

- You **write it down** ✍️

If you go the wrong way:

- You **erase it** 🧽 because you're not using that path anymore.

This is backtracking!

---

## 🧠 Code (Building the Path)

```python
def leafPath(root, path):
    if not root or root.val == 0:
        return False

    path.append(root.val)  # ✍️ write the number

    if not root.left and not root.right:  # 🍃 reached leaf
        return True

    if leafPath(root.left, path):  # ⬅️ try left
        return True

    if leafPath(root.right, path):  # ➡️ try right
        return True

    path.pop()  # 🧽 erase last number (backtrack)
    return False

```

---

# 📏 Time & Space (Cartoon Version)

### 🕒 Time Complexity — **O(n)**

You may need to check **all nodes** in the tree.

It's like exploring every room in a house 🏠.

### 🧠 Space Complexity — **O(h)**

You only remember the steps from the top to where you are now.

Like a small backpack 🎒 carrying your path.

# Backtracking

Backtracking is an algorithmic technique that has a lot of overlap with **Depth-First Search (DFS)**. It uses a **brute-force strategy**, trying all possible solutions and *backtracking* whenever it reaches a dead-end.

Think of it like navigating a maze:

You try one path. If you hit a wall, you walk back (backtrack) and try another path.

This is exactly how backtracking works.

---

## Motivation With Example

**Problem:**

Given a binary tree, determine whether there exists a path from the root to a leaf node **without encountering a node with value 0**.

If such a path exists → return `True`

Otherwise → return `False`

### Valid Path Exists

*(visual representation)*

### Valid Path Does Not Exist

*(visual representation)*

### Reasoning

- If the tree is empty → no path exists.
- If the current node is `0` → path is invalid.
- If we reach a leaf node → valid path found.
- Otherwise, the solution must be in either:
    - the **left subtree**, or
    - the **right subtree**

Process:

1. Explore the left subtree.
2. If it returns `True`, return `True`.
3. Otherwise, explore the right subtree.
4. Return `True` if right subtree works; otherwise `False`.

### Code

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def canReachLeaf(root):
    if not root or root.val == 0:
        return False

    if not root.left and not root.right:
        return True

    if canReachLeaf(root.left):
        return True
    if canReachLeaf(root.right):
        return True

    return False

```

### Example Tree:

`[4,0,1,null,7,2,0]`

The valid path follows the right subtree and avoids nodes with value `0`.

---

## Building the Path

Now consider a variation:

Instead of returning only `True` or `False`, **also return the actual path from root to leaf**.

We maintain an array `path` to track nodes along the current DFS path.

### Example Tree:

`[4,0,1,null,7,3,2,null,null,null,0]`

### Process Walkthrough

1. Add `4` to the path.
2. The left subtree is invalid (`0`). Backtrack.
3. Move to the right subtree:
    - Add `1`.
4. Explore left child:
    - Add `3`
    - Both children are `null`, so backtrack (remove `3`).
5. Explore right child:
    - Add `2`
    - This is a leaf node → return `True`.
6. Final valid path:
    
    **`[4, 1, 2]`**
    

### Code

```python
def leafPath(root, path):
    if not root or root.val == 0:
        return False

    path.append(root.val)

    if not root.left and not root.right:
        return True

    if leafPath(root.left, path):
        return True

    if leafPath(root.right, path):
        return True

    path.pop()  # Backtrack when both children fail
    return False

```

---

## Time and Space Complexity

### ⏱ Time Complexity — **O(n)**

We may need to explore every node in the tree in the worst case.

### 🧠 Space Complexity — **O(h)**

Where `h` is the height of the tree.

- Recursion stack depth = height of tree → `O(h)`
- `path` array stores at most `h` values → `O(h)`

Total: **O(h)**