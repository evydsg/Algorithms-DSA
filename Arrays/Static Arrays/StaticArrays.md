# 📚 Static Arrays

## 📌 What is a Static Array?
> - In **statically typed languages** (Java, C++, C#), arrays have a **fixed size and type** at initialization.
> - Once declared, the **size cannot change**.
> - **Dynamically typed languages** (like Python, JavaScript) don't have static arrays — they use dynamic structures.

---

## ⚙️ Key Operations on Arrays

### 🔹 Reading from an Array

```python
myArray = [1, 3, 5]
value = myArray[i]
```

- **Access is O(1)** — Direct mapping between index and RAM.
- ✅ Fast regardless of array size.

> ℹ️ **Note:** O(1) means "constant time," not necessarily "fast" if individual operations are expensive.

<details>
<summary>Expand: Reading Example</summary>

You can access any element instantly by index without traversing the array.
</details>

---

### 🔹 Traversing an Array

```python
for i in range(len(myArray)):
    print(myArray[i])
```
or
```python
i = 0
while i < len(myArray):
    print(myArray[i])
    i += 1
```

- **Traversal is O(n)** — You visit every element once.

> 📈 The number of operations grows linearly with the size of the array.

---

### 🔹 Deleting from an Array

<details>
<summary>Delete from the End</summary>

```python
def removeEnd(arr, length):
    if length > 0:
        arr[length - 1] = 0
```

- **O(1)** — Overwrite last element.
- Soft delete by replacing with `0`, `-1`, or `null`.

</details>

<details>
<summary>Delete at a Specific Index</summary>

```python
def removeMiddle(arr, i, length):
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
```

- **O(n)** — Need to shift all elements to maintain contiguous memory.
- Worst case: deleting the first element.

</details>

---

### 🔹 Inserting into an Array

<details>
<summary>Insert at the End</summary>

```python
def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n
```

- **O(1)** — Insert at the next available position.

</details>

<details>
<summary>Insert at a Specific Index</summary>

```python
def insertMiddle(arr, i, n, length):
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]
    arr[i] = n
```

- **O(n)** — Shift elements to the right before inserting.

</details>

---

## 📊 Quick Summary: Time Complexity

| Operation  | Time Complexity | Notes |
|------------|------------------|-------|
| Reading    | **O(1)**          | Direct access |
| Insertion  | **O(1)** (end) / **O(n)** (middle) | Shifting if middle |
| Deletion   | **O(1)** (end) / **O(n)** (middle) | Shifting if middle |
| Traversing | **O(n)**          | Linear |

---

# ✅ Key Takeaways
- Accessing an element = **O(1)** (instant).
- Traversing = **O(n)** (visit all elements).
- Insert/Delete at end = **O(1)**.
- Insert/Delete at middle = **O(n)** (shift required).
