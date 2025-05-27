# 🧩 LeetCode 707. Design Linked List


---

## 📘 Description

Design your implementation of a linked list.
You can choose to use a **singly** or **doubly** linked list.

* A node in a **singly linked list** should have two attributes:

  * `val`: the value of the current node
  * `next`: a pointer/reference to the next node

* A node in a **doubly linked list** will have one more attribute:

  * `prev`: a pointer/reference to the previous node

**All nodes in the linked list are 0-indexed.**

---

## 🚀 Class: `MyLinkedList`

### 🔧 Methods to Implement:

#### `MyLinkedList()`

* Initializes the `MyLinkedList` object.

#### `int get(int index)`

* Returns the value of the `index`-th node in the linked list.
* If the index is **invalid**, return `-1`.

#### `void addAtHead(int val)`

* Add a node of value `val` **before the first element** of the linked list.
* After insertion, the new node becomes the **first node** of the linked list.

#### `void addAtTail(int val)`

* Append a node of value `val` as the **last element** of the linked list.

#### `void addAtIndex(int index, int val)`

* Add a node of value `val` **before** the `index`-th node in the linked list.
* If `index` equals the **length** of the list, the node is appended at the end.
* If `index` is **greater** than the length, the node will **not** be inserted.

#### `void deleteAtIndex(int index)`

* Delete the `index`-th node in the linked list **if the index is valid**.

---

## 🧪 Example

**Input:**

```python
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
```

**Output:**

```python
[null, null, null, null, 2, null, 3]
```

**Explanation:**

```python
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);         # List: 1
myLinkedList.addAtTail(3);         # List: 1 -> 3
myLinkedList.addAtIndex(1, 2);     # List: 1 -> 2 -> 3
myLinkedList.get(1);               # Returns 2
myLinkedList.deleteAtIndex(1);     # List: 1 -> 3
myLinkedList.get(1);               # Returns 3
```

---

## 📌 Constraints

* `0 <= index, val <= 1000`
* At most `2000` calls will be made to `get`, `addAtHead`, `addAtTail`, `addAtIndex`, and `deleteAtIndex`.
* Do **not** use built-in `LinkedList` libraries.

