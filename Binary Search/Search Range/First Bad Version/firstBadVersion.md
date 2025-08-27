# 278. First Bad Version

## 📘 Problem Statement

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check.

Since each version is developed based on the previous version, all versions after a bad version are also bad.

Given n versions [1, 2, ..., n], you need to find the first bad version, which causes all the following ones to be bad.

You are provided an API:

isBadVersion(version: int) -> bool

Returns True if the version is bad.

Returns False if the version is good.

You should minimize the number of calls to this API.

### 🔹 Example 1

Input:

n = 5, bad = 4


Process:

isBadVersion(3) -> False
isBadVersion(5) -> True
isBadVersion(4) -> True


Output:

4

### 🔹 Example 2

Input:

n = 1, bad = 1


Output:

1