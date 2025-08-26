# Binary Search (Search Range)

## Concept
Imagine you pick a number between 1 and 100 and ask your friend to guess the number you're thinking of. There are three possible outcomes for each guess:
1. The guess is correct.
2. The guess is too small.
3. The guess is too large.

After each guess, you tell your friend if their guess is correct, too small, or too large. Based on your feedback, they adjust their next guess accordingly.

## Implementation
This is a classic binary search problem. As long as there is a way to determine if the guess is too big, too small, or correct, we can adjust the search space accordingly.

In many problems, the comparison is handled by a predefined function or a mathematical equation. In this case, we'll assume we are given the function `isCorrect(n)` that returns:
- `1` if `n` is too big,
- `-1` if `n` is too small,
- `0` if `n` is correct.

### Example: `isCorrect` function
```python
# Return 1 if n is too big, -1 if too small, 0 if correct
def isCorrect(n):
    if n > 10:
        return 1
    elif n < 10:
        return -1
    else:
        return 0
In this example, the correct number is hardcoded as 10.

Now we can use this function to implement binary search. We calculate the middle of the search space and pass it to the isCorrect function as our guess. Depending on the return value, we adjust our search space.