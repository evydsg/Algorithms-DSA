# Merge Two Sorted Linked Lists

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from `list1` and `list2`.

---

## ✅ Example 1

**Input:**

```python
list1 = [1,2,4]  
list2 = [1,3,5]
````

**Output:**

```python
[1,1,2,3,4,5]
```

---

## ✅ Example 2

**Input:**

```python
list1 = []  
list2 = [1,2]
```

**Output:**

```python
[1,2]
```

---

## ✅ Example 3

**Input:**

```python
list1 = []  
list2 = []
```

**Output:**

```python
[]
```

---

## 📌 Constraints

* `0 <=` The length of each list `<= 100`
* `-100 <= Node.val <= 100`

---

## 🧩 Plan

1. **Edge Case Check**

   * If both `list1` and `list2` are `None`, return `None`.

2. **Initialize Pointers**

   * Create a dummy node `new_list` with value `0`.
   * Create a `pointer` starting at `new_list`.
   * Set `pointer1 = list1` and `pointer2 = list2`.

3. **Iterate While Both Lists Have Nodes**

   * Compare `pointer1.val` and `pointer2.val`.
   * Link the smaller node to `pointer.next`.
   * Advance the corresponding pointer.
   * Move `pointer` forward.

4. **Attach Remaining Nodes**

   * If `pointer1` still has nodes, link `pointer.next = pointer1`.
   * If `pointer2` still has nodes, link `pointer.next = pointer2`.

5. **Return the Merged List**

   * Return `new_list.next` (skip dummy node).

---

## 💡 Complexity

* **Time Complexity:** `O(n + m)` where `n` and `m` are the lengths of `list1` and `list2`.
* **Space Complexity:** `O(1)` — reuses existing nodes, no extra memory used except the dummy node.


