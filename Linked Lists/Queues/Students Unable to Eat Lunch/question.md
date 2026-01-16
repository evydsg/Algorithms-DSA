# 🥪 1700. Number of Students Unable to Eat Lunch
**Link**: [Leetcode Problem #1700](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch)
## 🧠 Problem Summary

In a school cafeteria:

* Sandwiches are stacked (top = index 0).
* Students are queued (front = index 0).
* Each sandwich is either:

  * `0` → Circular sandwich
  * `1` → Square sandwich
* Each student has a preference: `0` or `1`.

---

## 🕹️ Rules:

1. At each step:

   * If the **front student** wants the **top sandwich**, they take it and **both leave**.
   * Else, the student **moves to the end** of the queue.

2. This process continues until:

   * **No students want the top sandwich**, i.e., full rotation with no match.

---

## 🔁 Simulation

### ✅ If student matches sandwich:

* `students.pop(0)`
* `sandwiches.pop(0)`
* reset unsuccessful attempts counter

### ❌ If no match:

* `students.append(students.pop(0))`
* increment the counter
* if counter == len(students): break

---

## 🧪 Example 1

**Input**:

```python
students = [1,1,0,0]
sandwiches = [0,1,0,1]
```

**Process**:

```
[1,1,0,0] | [0,1,0,1] → no match → rotate
[1,0,0,1] | [0,1,0,1] → no match → rotate
[0,0,1,1] | [0,1,0,1] → match → pop both
[0,1,1]   | [1,0,1]   → no match → rotate
[1,1,0]   | [1,0,1]   → match → pop both
[1,0]     | [0,1]     → no match → rotate
[0,1]     | [0,1]     → match → pop both
[1]       | [1]       → match → pop both
[]        | []        → done
```

**Output**:

```python
0  # All students got their preferred sandwich
```

---

## 🧪 Example 2

**Input**:

```python
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
```

**Process**:

```
[1,1,1,0,0,1] | [1,...] → match
[1,1,0,0,1]   | [0,...] → no match → rotate x3
[0,0,1,1,1]   | [0,...] → match
[0,1,1,1]     | [0,...] → match
[1,1,1]       | [0,...] → no match → rotate x3
[1,1,1]       | [0,...] → no one wants 0 → stop
```

**Output**:

```python
3  # Three students couldn’t eat
```

---

## ✅ Constraints

* `1 <= students.length == sandwiches.length <= 100`
* `students[i]` and `sandwiches[i]` ∈ {0, 1}
