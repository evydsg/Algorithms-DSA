# 🧠 What Dynamic Programming REALLY is

Dynamic Programming (DP) is **not a new algorithm**.

It is simply:

> **Avoiding repeated work.**
> 

That’s it.

A more formal definition:

> DP solves a big problem by breaking it into smaller problems **and remembering the answers** so we never recompute them again.
> 

So DP =

**Recursion + Memory**

(That memory is called a *cache* or *memo*.)

---

# Why Recursion Becomes Slow (Fibonacci Example)

We start with Fibonacci:

[

F(n) = F(n-1) + F(n-2)

]

Brute force:

```python
def bruteForce(n):
    if n <= 1:
        return n
    return bruteForce(n - 1) + bruteForce(n - 2)
```

Looks innocent.

But here is the problem:

When you calculate `fib(5)`…

You calculate:

```
fib(5)
 ├─ fib(4)
 │   ├─ fib(3)
 │   │   ├─ fib(2)
 │   │   └─ fib(1)
 │   └─ fib(2)
 └─ fib(3)
     ├─ fib(2)
     └─ fib(1)
```

Do you see it?

👉 **fib(2) is calculated 3 times**

👉 **fib(3) is calculated 2 times**

Your computer keeps forgetting.

This is why time complexity becomes:

[

O(2^n)

]

Exponential = 💀 death in interviews.

---

# The Big Idea of DP

Instead of recomputing…

We **store the answer** the first time.

So next time:

> “Oh, I already solved this. I’ll just reuse it.”
> 

This is called:

## 🔹 Memoization (Top-Down DP)

We keep a dictionary (cache).

```python
def memoization(n, cache):
    if n <= 1:
        return n

    if n in cache:
        return cache[n]

    cache[n] = memoization(n-1, cache) + memoization(n-2, cache)
    return cache[n]
```

What changed?

We added:

```python
if n in cache:
    return cache[n]
```

Now:

Each Fibonacci number is calculated **only once**.

Time complexity:

[

O(n)

]

You just turned an exponential algorithm into a linear one.

That’s why interviewers LOVE DP.

---

# Two Types of Dynamic Programming

There are only **2 DP styles**.

This is extremely important.

---

## 1️⃣ Top-Down (Memoization)

You start with the big problem and go downward using recursion.

Think:

> “I want fib(100), let me recursively break it.”
> 

Uses:

- recursion
- hashmap (cache)

---

## 2️⃣ Bottom-Up (Tabulation)

Opposite mindset.

You don’t ask:

> What is fib(100)?
> 

You say:

> I already know fib(0) and fib(1).
> 
> 
> Let me build up to 100.
> 

We fill answers step-by-step.

```
index: 0 1 2 3 4 5
value: 0 1 1 2 3 5
```

Code:

```python
def dp(n):
    if n < 2:
        return n

    dp = [0, 1]

    i = 2
    while i <= n:
        tmp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = tmp
        i += 1

    return dp[1]
```

---

# The Most Important Interview Insight ⭐

We don’t actually need an array.

Why?

Because Fibonacci only needs the **last 2 values**.

We only care about:

```
previous
current
```

So we compress memory → O(1) space.

This is the *real DP thinking* interviewers test.

---

## Cleanest Version (Best One)

```python
def fib(n):
    if n <= 1:
        return n

    prev = 0
    curr = 1

    for _ in range(2, n+1):
        prev, curr = curr, prev + curr

    return curr
```

Time: **O(n)**

Space: **O(1)** ← interview gold

---

# When Do You Know a Problem is DP?

This is the secret interview trick:

A problem is DP if it has **BOTH**:

### 1) Overlapping Subproblems

You solve the same smaller problem multiple times.

(Fibonacci, climbing stairs, coin change)

### 2) Optimal Substructure

The big answer depends on smaller optimal answers.

Example:

```
best way to reach step 10
depends on
best way to reach step 9 and step 8
```

---

# What “1-Dimensional DP” Means

It just means:

> We only need ONE variable indexed by position.
> 

Examples:

- Fibonacci
- Climbing Stairs
- House Robber
- Maximum Subarray
- Coin Change

(You will 100% get one of these in interviews.)

---

# The Mental Model You Should Use

When you see a problem, ask:

1. Can I define a state?
    
    → “What does dp[i] represent?”
    
2. How do I transition?
    
    → “How do I get dp[i] from smaller answers?”
    
3. Base cases?
    
    → smallest solvable problems
    

That’s literally DP.