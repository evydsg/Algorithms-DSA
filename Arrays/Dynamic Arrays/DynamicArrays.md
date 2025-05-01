
# 📦 Dynamic Arrays

Dynamic arrays are a more flexible alternative to static arrays. They grow automatically as new elements are added, making them especially useful in languages like **Python** and **JavaScript**, where they are the default array structure.

---

## 📌 Key Characteristics

- No need to define size during initialization.
- Automatically resize when full.
- Default initial sizes in some languages:
  - **Java**: `10`
  - **C#**: `4`

---

## ➕ Insertion at the End

```python
# Insert n at the end of the array
def pushback(self, n):
    if self.length == self.capacity:
        self.resize()
    self.arr[self.length] = n
    self.length += 1
```

---

## 🔁 Resize Operation

When the array is full, we create a new array with **double the capacity** and copy all elements over.

```python
def resize(self):
    self.capacity *= 2
    newArr = [0] * self.capacity
    for i in range(self.length):
        newArr[i] = self.arr[i]
    self.arr = newArr
```

- The old array is **deallocated** after copying.
- This operation has a time complexity of **O(n)**.

---

## 🕒 Time Complexity

| Operation           | Big-O Time | Notes                                         |
|--------------------|------------|-----------------------------------------------|
| Access             | O(1)       | Instant lookup using index                    |
| Insertion (end)    | O(1)\*     | Amortized constant time                       |
| Insertion (middle) | O(n)       | Requires shifting elements                    |
| Deletion (end)     | O(1)\*     | Amortized constant time                       |
| Deletion (middle)  | O(n)       | Requires shifting elements                    |

\* **Amortized** over many operations due to periodic resizing.

---

## ⚙️ Why Double the Capacity?

Suppose we start with a size-1 array and keep adding elements:

```
1 → 2 → 4 → 8
```

To reach size 8, the total operations needed:

```
1 + 2 + 4 + 8 = 15
```

This shows the last term (8) is **greater than the sum of previous terms** (1+2+4 = 7), and:

- To grow to size `n`, we do at most **2n operations** → **O(n)**
- So inserting `n` elements is **O(n)** total → **O(1)** amortized per insert

---

## 📚 Summary

- Dynamic arrays **resize automatically** by doubling in size.
- Insertion at the end is **amortized O(1)**.
- Insert/delete in the middle is **O(n)** due to shifting.
- Widely used in high-level languages for their flexibility.
