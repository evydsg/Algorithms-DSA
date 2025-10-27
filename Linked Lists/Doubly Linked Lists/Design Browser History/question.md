# 🧭 1472. Design Browser History
**Leetcode Link:** [Leetcode 1472](https://leetcode.com/problems/design-browser-history/)

---

## 📝 Problem Description

You have a browser with one tab where you start on the homepage. You can:

* Visit another URL.
* Go back in the history a number of steps.
* Move forward in the history a number of steps.

---

## 📘 Implement the `BrowserHistory` class:

```python
class BrowserHistory:
    def __init__(self, homepage: str):
        pass

    def visit(self, url: str) -> None:
        pass

    def back(self, steps: int) -> str:
        pass

    def forward(self, steps: int) -> str:
        pass
```

---

### 🧱 API Methods

| Method                            | Description                                                                                                            |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `BrowserHistory(string homepage)` | Initializes the object with the homepage of the browser.                                                               |
| `void visit(string url)`          | Visits `url` from the current page. Clears all forward history.                                                        |
| `string back(int steps)`          | Move `steps` back in history. If `steps > history length`, return the earliest page. Returns the current URL.          |
| `string forward(int steps)`       | Move `steps` forward in history. If `steps > forward history`, go as far forward as possible. Returns the current URL. |

---

## 📌 Example

```python
Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]
```

### 🧭 Step-by-step Walkthrough:

```python
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       # leetcode.com -> google.com
browserHistory.visit("facebook.com");     # google.com -> facebook.com
browserHistory.visit("youtube.com");      # facebook.com -> youtube.com
browserHistory.back(1);                   # youtube.com -> facebook.com => return "facebook.com"
browserHistory.back(1);                   # facebook.com -> google.com => return "google.com"
browserHistory.forward(1);                # google.com -> facebook.com => return "facebook.com"
browserHistory.visit("linkedin.com");     # facebook.com -> linkedin.com (clears forward history)
browserHistory.forward(2);                # No forward => return "linkedin.com"
browserHistory.back(2);                   # linkedin.com -> facebook.com -> google.com => return "google.com"
browserHistory.back(7);                   # google.com -> leetcode.com => return "leetcode.com"
```

---

## 🔒 Constraints

* `1 <= homepage.length <= 20`
* `1 <= url.length <= 20`
* `1 <= steps <= 100`
* `homepage` and `url` consist of only **lowercase English letters** or **'.'**
* At most **5000 calls** will be made to `visit`, `back`, and `forward`.