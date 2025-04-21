- Python executes $10^7$ operations per second 
- If $f_1(n)$ is $O(g_1(n))$ and $f_2(n)$ is $O(g_2(n))$, then $f_1(n) + f_2(n)$ is $O(max(g_1(n), g_2(n)))$
- Suppose Algorithm has two phases
   1.  Phase A takes time $O(g_A(n))$
   2.  Phase B takes time $O(g_B (n))$
   - Algorithm as a whole takes time $max(O(g_A(n), g_B (n)))$
- $f(n)$ is $O(g(n))$ means $g(n)$ is an upper bound for $f(n)$
    - Useful to describe asymptotic worst case running time
- $f(n)$ is $Ω(g(n))$ means $g(n)$ is a lower bound for $f (n)$
    - Typically used for a problem as a whole, rather than an individual algorihm
- $f (n)$ is $Θ(g(n))$: matching upper and lower bounds
    - We have found an optimal algorithm for a problem
---
Here's a clean table summarizing **searching** and **sorting algorithms**, including:

- **Time complexities** (Best, Average, Worst)
- **Naive complexities**
- **Main logic**
- **Bottlenecks**

---

### 🔍 **Searching Algorithms**

| Algorithm     | Best     | Average   | Worst     | Naive Complexity | Logic (Short)                                  | Bottleneck                          |
|---------------|----------|-----------|-----------|------------------|------------------------------------------------|-------------------------------------|
| **Linear Search** | $ O(1) $   |  $O(n)$   | $ O(n)$   | $ O(n)$            | Scan every element until match found           | Checking every element              |
| **Binary Search** | $O(1)$   |  $O(\log n)$ | $O(\log n)$ | $O(n)$           | Repeatedly divide sorted array                 | Needs sorted array; comparisons     |

---

### 🔃 **Sorting Algorithms**

| Algorithm       | Best       | Average     | Worst       | Naive Complexity | Logic (Short)                                      | Bottleneck                          |
|------------------|------------|-------------|-------------|------------------|---------------------------------------------------|-------------------------------------|
| **Bubble Sort**   |$O(n)$     | $O(n^2)$     |  $O(n^2)$      | $ O(n^2)$         | Repeatedly swap adjacent elements if out of order | Too many comparisons/swaps          |
| **Selection Sort**| $O(n^2)$   | $ O(n^2)$     | $ O(n^2)$      | $ O(n^2)$         | Select min element and place at correct position  | Finding min every time              |
| **Insertion Sort**|  $O(n)$     | $O(n^2)$      | $O(n^2)$     | $ O(n^2)$         | Insert each element into sorted subarray          | Shifting elements                   |
| **Merge Sort**    |  $O(n \log n)$ | $ O(n \log n)$  |  $O(n \log n)$ |  $O(n \log n)$     | Divide array and the way you devide also matters a lot, sort halves, and merge              | Merge step                          |
| **Quick Sort**    | $ O(n \log n)$ | $O(n \log n)$  | $ O(n^2)$     |$ O(n^2)$         | Partition using pivot, sort subarrays recursively | Bad pivot choice in worst case     |
| **Heap Sort**     |  $O(n \log n)$ | $O(n \log n)$ |$ O(n \log n)$ | $ O(n \log n)$     | Build heap, extract max repeatedly                | Heapify and reheapify               |
| **Radix Sort**    |  $O(nk)$      |  $O(nk)$      | $O(nk)$      |  $O(nk)$            | Sort digits place-by-place using counting sort    | Only works with integers; digit size |
| **Counting Sort** | $O(n + k)$   | $ O(n + k)$   | $ O(n + k)$   |  $O(n^2)$         | Count frequencies, rebuild sorted array           | Large range of values               |

---
- Stability of sorting is crucial in many applications, Sorting on column B should not disturb sorting on column A
    - The quicksort implementation we described is not stable
    - Merge sort is stable if we merge carefully
       -  Do not allow elements from the right to overtake elements on the left
       -  While merging, prefer the left list while breaking ties
    - Quicksort is often the algorithm of choice, despite $O(n^2)$ worst case
---
- Graph: G = (V, E)
    - V is a set of vertices or nodes
    - E is a set of edges
    - $E ⊆ V × V$ — binary relation
- Directed graph
    - $(v, v_0) ∈ E \nRightarrow (v_0, v) ∈ E$
    - The teacher-course graph is directed
- Undirected graph
    - $(v, v_0) \in E \Leftrightarrow (v_0, v) \in E$
    - Effectively $(v, v_0), (v_0, v)$ are the same edge
    - Friendship graph is undirected
- A path is a sequence of vertices $v_1, v_2, . . . , v_k$ connected by edges, a path does not visit a vertex twice.
- Vertex $v$ is reachable from vertex $u$ if there is a path from $u$ to $v$
- A sequence that re-visits a vertex is usually called a walk 
- Typical questions
    1. Is v reachable from u?
    1. What is the shortest path from u to v?
    1. What are the vertices reachable from u?
    1. Is the graph connected? Are all vertices
    1. reachable from each other?

- Colouring is a function   $c : V \rightarrow C \text{ such that } (u, v) \in E \Rightarrow c(u) \ne c(v)$
    - Abstraction: if we distort the graph, problem is unchanged
    - For planar graphs derived from geographical maps, 4 colours suffice
- Vertex cover - Marking v covers all edges from v
- Independent set - Subset of vertices such that no two are connected by an edge
- Matching
    - $G = (V, E)$, an undirected graph
    - A matching is a subset $M ⊆ E$ of mutually disjoint edge
    - Is there a perfect matching, covering all vertices
- A cycle is a path (technically, a walk) that starts and ends at the same vertex.
    - Cycle should not repeat edges: $i-j-i$ i.e 4-2-4
    - Edges explored by BFS form a tree, one tree per component
    - Detect cycles by searching for non-tree edges
- for scheduling we do topological sorting a DAG.
    - Enumerate $V = {0, 1, . . . , n − 1}$ such that for any $(i, j) ∈ E$, $i$ appears before $j$
    - A graph with directed cycles cannot be sorted topologically, but Every DAG can be topologically sorted
- we compute longest path after topological sorting, and would it be unique, do we need uniqness? 
- BFS computes shortest path, in terms of number of edges, to every reachable vertex
    - Each new shortest path we discover extends an earlier one
- A tree on $n$ vertices has exactly $n − 1$ edges
- Adding an edge to a tree must create a cycle.
- In a tree, every pair of vertices is connected by a unique path.
- Any two of the following facts about a graph $G$ implies the third
    1. $G$ is connected
    1. $G$ is acyclic
    1. $G$ has $ n − 1$ edges
- **Minimum seprator lemma**
    - Let $V$ be partitioned into two non-empty sets $U$ and $W = V \setminus U$
    - Let $e = (u,w)$ be the minimum cost edge with $u ∈ U, w ∈ W$
    - Every MCST must include $e$
- If edge weights repeat, MCST is not unique
---
Here's a detailed comparison table listing the **time complexities** of various graph algorithms — **Dijkstra's**, **Floyd-Warshall**, **Bellman-Ford**, **Prim's**, **Kruskal's**, **BFS**, and **DFS** — with respect to:
- **Naive implementation**
- **Adjacency List**
- **Adjacency Matrix**
- **Main bottlenecks**

| Algorithm         | Best            | Average         | Worst            | Naive Complexity   | Logic (Short)                                            | Bottleneck                             |
|------------------|------------------|------------------|------------------|---------------------|----------------------------------------------------------|----------------------------------------|
| **Topological Sort** | $O(V + E)$    | $O(V + E)$       | $O(V + E)$        | $O(V^2)$             | Visit nodes in order of dependencies                     | Cycle check, full graph traversal      |
| **Longest Path (DAG)** | $O(V + E)$         | $O(V + E)$         | $O(V + E)$         | $O(V^2)$         | Topo sort + relax edges in order                     | Only for DAGs; depends on topo sort     |
| **Dijkstra**        | $O((V + E)\log V)$ | $O((V + E)\log V)$ | $O(V^2)$        | $O(V^2)$             | Relax shortest distances using greedy choice             | No heap = slow min-distance selection  |
| **Floyd-Warshall**  | $O(V^3)$       | $O(V^3)$         | $O(V^3)$          | $O(V^3)$             | All-pairs shortest path via dynamic programming          | Triple nested loop                     |
| **Bellman-Ford**    | $O(VE)$        | $O(VE)$          | $O(VE)$           | $O(VE)$              | Relax all edges V−1 times                                | Many edge relaxations                  |
| **Prim’s MST**      | $O((V + E)\log V)$ | $O((V + E)\log V)$ | $O(V^2)$       | $O(V^2)$             | Grow MST from source by choosing min edge                | Finding min edge without heap          |
| **Kruskal’s MST**   | $O(E \log E)$  | $O(E \log E)$    | $O(E \log E)$     | $O(E^2)$             | Sort edges, add if no cycle using union-find             | Sorting + union-find operations        |
| **BFS**             | $O(V + E)$     | $O(V + E)$       | $O(V + E)$        | $O(V^2)$             | Visit nodes level by level                               | Matrix = slow neighbor checks          |
| **DFS**             | $O(V + E)$     | $O(V + E)$       | $O(V + E)$        | $O(V^2)$             | Recursively explore as far as possible                   | Matrix = slow neighbor checks          |

### Notes:
- $V$  = Number of vertices, $E$ = Number of edges.
- **Adjacency List** is space-efficient and faster for sparse graphs.
- **Adjacency Matrix** is simple but inefficient for dense graphs.
- **Naive** versions usually skip data structures like heaps or union-find, making them slower.
- Algorithms like Dijkstra’s and Prim’s benefit greatly from **heaps** for performance.
- Kruskal’s bottleneck is **sorting the edges** and managing **union-find** efficiently.
- BFS/DFS are linear in list form but become  $O(V^2)$  with matrix due to scanning all possible edges.
- If Bellman-Ford algorithm does not converge after $n − 1$ iterations, there is a negative cycle
---

<!-- Let me know if you want a printable/markdown version of this. -->
- BSTs:
    1. All values in the left subtree are $ < v$ i.e Minimum is left most node in the tree
    1. All values in the right subtree are $> v$ i.e Maximum is right most node in the tree
    1. Each node has a value and pointers to its children
- General strategy to build a small balanced tree of height h:
    - Smallest balanced tree of height $h − 1$ as left subtree
    - Smallest balanced tree of height $h − 2$ as right subtree
    - Slope of a node : self.left.height() - self.right.height(), Balanced tree — slope is ${−1, 0, 1}$, if the tree is not balanced perform rotations.
- DP and Greedy algos
- Regular expressions:
    1. To match the start of the string, write $ˆp$
    2. To match the end of the string, write $p$ $
    3. ˆbana$ does not match banana, but $ˆba(na)^+$ does, this means that the string in between must only contain more $(na)$ and nothing else. To modify it we can write $ˆba(na)^+.*na$ then we can have any string that would match the pattern bananananan123na or anything else.
- Linear programming :
    - Feasible region is convex
---
# Abstraction of the course (i.e solving a problem at hand).

| Paradigm            | Algorithms                              | Optimal Data Structures         | Notes                                                       |
|---------------------|------------------------------------------|----------------------------------|--------------------------------------------------------------|
| **Divide & Conquer**| Merge Sort                               | Arrays                           | Divides array, recursively sorts and merges                  |
|                     | Quick Sort                               | Arrays                           | Partitions using pivot, sorts subarrays                      |
|                     | Heap Sort                                | Binary Heap (Array-based)        | Uses max heap to sort                                        |
|                     | Binary Search                            | Sorted Arrays                    | Divides array to search efficiently                          |
|                     | Ternary Search                           | Sorted Arrays                    | Like binary, but splits into 3 parts                         |
| **Greedy**          | Selection Sort                           | Arrays                           | Repeatedly selects min element                               |
|                     | Insertion Sort                           | Arrays                           | Builds sorted array one element at a time                   |
|                     | Counting Sort                            | Arrays + Count Array             | Assumes known range of keys                                 |
|                     | Radix Sort                               | Arrays + Buckets (queues)        | Sorts digits by place (uses counting sort inside)           |
|                     | Bucket Sort                              | Arrays + Linked Lists/Buckets    | Divides elements into buckets, sorts individually           |
| **Dynamic Programming** | Longest Increasing Subsequence (LIS) | Arrays + DP table or Binary Search | DP: $O(n²)$, Optimized: $O(n \log n)$                        |
|                     | Optimal Binary Search Tree               | 2D DP Table                      | Computes min-cost BST from frequencies                      |
| **Naive / Brute Force** | Bubble Sort                          | Arrays                           | Swaps adjacent if out of order                              |
|                     | Linear Search                            | Arrays/Lists                     | Checks each element one by one                              |
|                     | Exponential Search                       | Sorted Arrays                    | Combines binary search + exponential step                   |
