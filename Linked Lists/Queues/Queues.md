# 🔄 Queues

A **Queue** is another data structure that overlaps with arrays and stacks. However, it follows a **FIFO** approach — *First In, First Out*.

## 📌 Real-World Analogy

A good example of a queue is a **line at the bank**:
- The first person added to the line is the **first person to be served**.

---

## 🧱 Implementation and Operations

The simplest way to implement a queue is with a **linked list**.

You can also use a **dynamic array**, but to maintain efficient time complexity, you would need to use a **circular array** and additional operations.

### ✅ Enqueue (Add to end)

The `enqueue` operation inserts an element at the **end** of the queue.  
With a singly linked list, this runs in **O(1)** time.

```python
def enqueue(self, val):
    newNode = ListNode(val)

    # Queue is non-empty
    if self.right:
        self.right.next = newNode
        self.right = self.right.next
    # Queue is empty
    else:
        self.left = self.right = newNode
