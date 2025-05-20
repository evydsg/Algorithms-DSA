# 📘 Doubly Linked Lists (DLL)

A **Doubly Linked List** is a linear data structure where each node has **two pointers**:
- `next` → points to the next node
- `prev` → points to the previous node

This allows **bidirectional traversal**, unlike singly linked lists.

---

## 🧩 Node Structure (Python)

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
````

---

## 🔁 Common Operations

### 🔹 Insertion at the End

**Time Complexity**: O(1)

```python
def insert_end(self, value):
    newNode = ListNode(value)
    if not self.head:
        self.head = self.tail = newNode
    else:
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
```

**🌀 Animation**: [Visualgo – DLL Insert End](https://visualgo.net/en/list?slide=7)

---

### 🔹 Insertion at the Front

**Time Complexity**: O(1)

```python
def insert_front(self, value):
    newNode = ListNode(value)
    if not self.head:
        self.head = self.tail = newNode
    else:
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
```

**🌀 Animation**: [Visualgo – DLL Insert Front](https://visualgo.net/en/list?slide=8)

---

### 🔹 Deletion at the End

**Time Complexity**: O(1)

```python
def delete_end(self):
    if not self.tail:
        return
    if self.head == self.tail:
        self.head = self.tail = None
    else:
        self.tail = self.tail.prev
        self.tail.next = None
```

**🌀 Animation**: [Visualgo – DLL Remove End](https://visualgo.net/en/list?slide=9)

---

### 🔹 Deletion at the Front

**Time Complexity**: O(1)

```python
def delete_front(self):
    if not self.head:
        return
    if self.head == self.tail:
        self.head = self.tail = None
    else:
        self.head = self.head.next
        self.head.prev = None
```

**🌀 Animation**: [Visualgo – DLL Remove Front](https://visualgo.net/en/list?slide=10)

---

## 🔍 Access & Search

* DLLs do **not support random access**
* Must **traverse** from the head or tail to reach a node
* Time Complexity: **O(n)**

✅ **Advantage**: Can **traverse forward and backward**

---

## 🧠 Use Case Notes

Doubly linked lists are great for:

* Undo/Redo functionality
* Browser history
* LRU (Least Recently Used) Cache
* Deques (Double-ended queues)

---

## 📊 Time Complexity Summary

| Operation | Time Complexity | Notes                                |
| --------- | --------------- | ------------------------------------ |
| Access    | O(n)            | Must traverse list                   |
| Search    | O(n)            | Linear search                        |
| Insertion | O(1)            | Efficient if node reference is known |
| Deletion  | O(1)            | Efficient if node reference is known |

