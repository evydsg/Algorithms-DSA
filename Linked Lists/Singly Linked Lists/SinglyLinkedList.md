# 📚 Linked Lists

A **linked list** is a linear data structure where elements (nodes) are linked using pointers. It's similar to an array in storing ordered data, but differs in **memory allocation** and **operations**.

---

### 🔧 Basic Structure

```python
class ListNode:
    def __init__(self, val):
        self.val = val       # Value of the node
        self.next = None     # Reference to the next node
````

* **val**: Can be any data (int, string, etc.)
* **next**: Points to the next `ListNode` in the list (or `None` if it's the last node)

---

### 🔗 Building a Linked List

1. Create nodes:

   ```python
   node1 = ListNode("red")
   node2 = ListNode("blue")
   node3 = ListNode("green")
   ```

2. Link them:

   ```python
   node1.next = node2
   node2.next = node3
   node3.next = None  # Last node
   ```

---

### 🔁 Traversal

To loop through a linked list from start to end:

```python
cur = node1
while cur:
    print(cur.val)
    cur = cur.next
```

* **Time Complexity**: `O(n)`

---

### ♻️ Circular Linked List

If the last node points back to the head:

```python
node3.next = node1
```

* Creates a **circular linked list**
* ⚠️ **Infinite loop** if not handled properly in traversal

---

## 🛠 Operations in a Singly Linked List

### 📌 Head & Tail

* `head`: First node
* `tail`: Last node
* If only 1 node: `head == tail`

---

### ➕ Appending a Node

```python
tail.next = new_node
tail = new_node
```

* **Time Complexity**: `O(1)` — if tail is already known
* If traversal is needed to find the tail: `O(n)`

---

### ❌ Deleting a Node

To delete the second node:

```python
head.next = head.next.next
```

* **Time Complexity**: `O(1)` — if reference to previous node is known
* If traversal is needed: `O(n)`

---

### ⏱ Time Complexity Summary

| Operation | Time Complexity | Note                                         |
| --------- | --------------- | -------------------------------------------- |
| Access    | O(n)            | Need to traverse to reach a node             |
| Search    | O(n)            | Must traverse to find value                  |
| Insertion | O(1)\*          | \*If node reference is known; otherwise O(n) |
| Deletion  | O(1)\*          | \*If node reference is known; otherwise O(n) |
