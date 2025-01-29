
# DSA Interview Question: Max Substring as a Subsequence

## Problem:

### Max Substring as a Subsequence

Given two strings `s` and `t`, your task is to find the longest substring of `t` that is also a subsequence of `s`.

- A **substring** of a string is a contiguous sequence of characters within that string.
- A **subsequence** of a string is a sequence derived from the string by deleting some or no characters without changing the order of the remaining characters.

### Function Signature:

```python
def max_substring(s: str, t: str) -> str:
    pass
```

### Input:

- A string `s` (1 ≤ len(s) ≤ 1000)
- A string `t` (1 ≤ len(t) ≤ 1000)

Both `s` and `t` consist of lowercase English letters.

### Output:

- Return the longest substring of `t` that is also a subsequence of `s`.
- If there are multiple such substrings with the same length, return any of them.

### Constraints:

- The length of `s` and `t` can each go up to 1000, so your solution should ideally have a time complexity better than O(n^3).

---

## Example 1:

### Input:

```python
s = "abcacb"
t = "ab"
```

### Output:

```python
"ab"
```

### Explanation:

The longest substring of `t` that is also a subsequence of `s` is `"ab"`.

---

## Example 2:

### Input:

```python
s = "abcdef"
t = "ace"
```

### Output:

```python
"ace"
```

### Explanation:

The longest substring of `t` that is a subsequence of `s` is `"ace"`. It is also a subsequence of `s` and matches the entire string.

---

## Example 3:

### Input:

```python
s = "abcde"
t = "fghij"
```

### Output:

```python
""
```

### Explanation:

There is no substring of `t` that can be a subsequence of `s` because the characters of `t` do not appear in `s`.

---

## Example 4:

### Input:

```python
s = "abcdefg"
t = "bcdf"
```

### Output:

```python
"bcd"
```

### Explanation:

The longest substring of `t` that is also a subsequence of `s` is `"bcd"`.

---

## Hints for the Interview:

- Consider the efficient way to check if a substring of `t` is a subsequence of `s`.
- You could optimize this by using dynamic programming or a two-pointer technique for matching subsequences.
- Pay attention to the constraints of the problem—solving it with brute force may not be efficient enough for large inputs.

---

## Edge Cases:

- When `t` is empty, the result should be an empty string.
- When `s` and `t` have no common subsequences, return an empty string.
- Handle both strings being long but containing overlapping subsequences.

---
