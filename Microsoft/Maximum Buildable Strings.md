# Maximum Buildable Strings Problem

## Problem Statement

You are given a list of strings **S** and an integer **K**. Your goal is to determine the maximum number of strings from **S** that can be formed using at most **K** unique characters. 

### **Constraints:**
- Each string in **S** consists of lowercase English letters.
- **K** represents the maximum number of unique characters that can be selected.
- A string is considered "buildable" if all of its characters are within the selected **K** unique characters.

### **Your Task:**
Write a function `solution(S, K)` that returns the maximum number of strings that can be built using at most **K** unique characters.

## Example 1
### **Input:**
```python
S = ["abc", "bca", "da", "adb"]
K = 2
```

### **Step-by-step Breakdown:**
1. The unique characters across all strings: `{'a', 'b', 'c', 'd'}`
2. Possible selections of **K = 2** unique characters: `{'a', 'b'}`, `{'a', 'c'}`, `{'a', 'd'}`, `{'b', 'c'}`, etc.
3. Checking each selection:
   - `{a, b}` → Can build `adb` and `da`
   - `{b, c}` → Can build `bca`
   - `{a, d}` → Can build `da` and `adb`
   - Maximum buildable count = **2**

### **Output:**
```python
2
```

## Example 2
### **Input:**
```python
S = ["xyz", "xy", "z", "yz"]
K = 1
```

### **Output:**
```python
1  # The best we can do is pick 'z' and build "z"
```

## Discussion
- The algorithm runs in **O(2^N)** time complexity in the worst case due to checking all subsets of **K** unique characters.
- Space complexity is **O(N)** due to storing unique characters and combinations.
- Can this approach be optimized further for larger values of **N**?

## Python Solution
```python
from itertools import combinations

def get_curr_buildable_strings_count(S, selected_chars):
    count = 0
    for string in S:
        set_string = set(string)
        if set_string.issubset(selected_chars):
            count += 1
    return count

def solution(S, K):
    # Implement your solution here
    
    unique_chars = set()
    for string in S:
        for char in string:
            unique_chars.add(char)
    
    max_buildable_strings = 0
    for char_subset in combinations(unique_chars, K):
        selected_chars = set(char_subset)
        curr_buildable_strings = get_curr_buildable_strings_count(S, selected_chars)
        max_buildable_strings = max(max_buildable_strings, curr_buildable_strings)
    
    return max_buildable_strings
```

