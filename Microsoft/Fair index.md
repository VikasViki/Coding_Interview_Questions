
# Fair Index Problem

## Problem Statement

You are given two integer arrays, **A** and **B**, of the same length **N**. A "fair index" is defined as an index **K** (where **1 \leq K < N**) that satisfies the following conditions:

1. The sum of the first **K** elements of **A** is equal to the sum of the remaining elements of **A**.  
2. The sum of the first **K** elements of **B** is equal to the sum of the remaining elements of **B**.  
3. The sum of the first **K** elements of **A** is equal to the sum of the first **K** elements of **B**.  
4. The sum of the remaining elements of **A** is equal to the sum of the remaining elements of **B**.

Your task is to determine the number of fair indices in the given arrays **A** and **B**.

## Implementation Details
- The function **solution(A, B)** is implemented to find the fair indices using prefix and suffix sum arrays.
- The helper functions **get_prefix_sum_array()** and **get_suffix_sum_array()** compute cumulative sums from the start and end, respectively.
- The main function iterates over all possible **K** values and checks whether the four conditions for a fair index are met.

## Example 1
### **Input:**
```python
A = [4, -1, 0, 3]
B = [-2, 5, 0, 3]
```

### **Step-by-step Breakdown:**
1. Compute prefix and suffix sum arrays:
   - `A_prefix = [4, 3, 3, 6]`
   - `B_prefix = [-2, 3, 3, 6]`
   - `A_suffix = [6, 2, 3, 3]`
   - `B_suffix = [6, 3, 3, 3]`
   
2. Identify valid **K** values (1 \leq K < N):
   - For **K = 2**:
     - `A_prefix[1] = 3`, `A_suffix[2] = 3`
     - `B_prefix[1] = 3`, `B_suffix[2] = 3`
     - All conditions are satisfied → **Fair index found**

### **Output:**
```python
1
```

## Example 2
### **Input:**
```python
A = [2, 3, 1, 4]
B = [2, 3, 1, 4]
```

### **Output:**
```python
0  # No fair index satisfies the conditions
```

## Constraints
- **1 \leq N \leq 100,000**  
- **-10^9 \leq A[i], B[i] \leq 10^9**  

## Discussion
- The algorithm currently runs in **O(N)** time due to the prefix and suffix sum calculations.
- Space complexity is **O(N)** due to the additional arrays used for storing prefix and suffix sums.
- Can this approach be optimized further to reduce space complexity?


## Python Solution
```python
import copy

def get_prefix_sum_array(arr, arr_len):
    arr = copy.deepcopy(arr)
    for index in range(1, arr_len):
        arr[index] += arr[index-1]
    return arr

def get_suffix_sum_array(arr, arr_len):
    arr = copy.deepcopy(arr)
    for index in range(arr_len-2, -1, -1):
        arr[index] += arr[index+1]
    return arr

def solution(A, B):
    # Implement your solution here
    arr_len = len(A)

    A_prefix = get_prefix_sum_array(A, arr_len)
    B_prefix = get_prefix_sum_array(B, arr_len)

    A_suffix = get_suffix_sum_array(A, arr_len)
    B_suffix = get_suffix_sum_array(B, arr_len)

    fair_indexex_count = 0
    for K in range(1, arr_len):
        if (A_prefix[K-1] == A_suffix[K] == B_prefix[K-1] == B_suffix[K]):
            fair_indexex_count += 1
    
    return fair_indexex_count
```
