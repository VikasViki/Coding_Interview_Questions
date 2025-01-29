# Minimum Friendship Score in a Graph (Trio Cycle)

## Problem Statement

You are given an **undirected graph** with nodes labeled from **1 to total_friends**. The graph is defined by an **edges list**, where each edge represents a **friendship** between two nodes.  

A **trio cycle** is a set of exactly **three nodes (u, v, w)** such that:  
- There exists an edge between **(u, v)**  
- There exists an edge between **(v, w)**  
- There exists an edge between **(w, u)**  
- This forms a **closed cycle of three nodes**.  

The **friendship score** of a trio cycle is defined as the total number of edges that connect any of the three nodes **to nodes outside the trio**.  

Your task is to **find the minimum friendship score** among all trio cycles in the graph. If there are no trio cycles, return `-1`.  

---

## Input Format

- An integer **total_friends**: the number of nodes in the graph.  
- An integer **m**: the number of edges.  
- A list **edges** of size **m × 2**, where each entry `[u, v]` represents an **undirected edge** between node `u` and node `v`.  

---

## Output Format

- Return a single integer representing the **minimum friendship score** among all trio cycles in the graph.  
- If no trio cycle exists, return `-1`.  

---

## Constraints

- \( 1 \leq total\_friends \leq 400 \)  
- \( 1 \leq m \leq 10^4 \)  
- \( 1 \leq u, v \leq total\_friends \)  
- There are no self-loops or duplicate edges.  

---

## Example

### **Input**
```plaintext
total_friends = 6
edges = [[1, 2], [2, 3], [3, 1], [3, 4], [4, 5], [5, 6], [6, 4], [2, 4]]
```

  1 --- 2
   \   /
    3
    |
    4 --- 5
    |     |
    6 ----


### **Output**
```plaintext
1
```

### Explanation

- The **trio cycle (1, 2, 3)** forms a **closed cycle**, and its **friendship score** is **1**, because:  
  - **Node 1** has **no external edges**.  
  - **Node 2** has **no external edges**.  
  - **Node 3** has **one external edge to 4**.  
  - **Total external edges = 1**.  

- The **trio cycle (3, 4, 6)** does **not exist** because **(3, 6) is not connected**.  

- The **minimum friendship score** among all **trio cycles** is **1**.  




