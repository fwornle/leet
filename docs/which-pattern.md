# Which Pattern? (Decision Tree)

Read the problem and ask these questions **in order**. The first diagram tells you which branch to follow, and the branch diagram names the pattern.

## Step 1 · What is the input, and what is asked?

```mermaid
graph TD
    Q["Read the problem"] --> I1{"All combinations,<br/>permutations, subsets?"}
    I1 -->|yes| BT["14 Backtracking"]
    I1 -->|no| I2{"Optimal value:<br/>min / max / count ways,<br/>choices overlap?"}
    I2 -->|yes| DPN["15 Dynamic Programming"]
    I2 -->|no| I3{"Input type?"}
    I3 -->|"array / string"| ARR["→ Step 2a"]
    I3 -->|"linked list"| LL["→ Step 2b"]
    I3 -->|"tree / graph / grid"| TG["→ Step 2c"]
```

## Step 2a · Array or string

```mermaid
graph LR
    A{"Array / string"} -->|"many range-sum queries,<br/>or subarray sum = k"| P1["1 Prefix Sum"]
    A -->|"contiguous subarray / substring<br/>longest, shortest, at most k"| P3["3 Sliding Window"]
    A -->|"sorted, find a pair / triplet,<br/>or palindrome / in-place"| P2["2 Two Pointers"]
    A -->|"next greater / smaller element"| P6["6 Monotonic Stack"]
    A -->|"k largest / smallest / most frequent"| P7["7 Top-K Heap"]
    A -->|"intervals, meetings, ranges"| P8["8 Overlapping Intervals"]
    A -->|"sorted or monotonic, O(log n),<br/>min max / max min"| P9["9 Modified Binary Search"]
```

## Step 2b · Linked list

```mermaid
graph TD
    L{"Linked list"} -->|"cycle, middle,<br/>k-th from end"| P4["4 Fast and Slow Pointers"]
    L -->|"reverse, reorder,<br/>swap in groups"| P5["5 In-place Reversal"]
```

## Step 2c · Tree, graph or grid

```mermaid
graph LR
    T{"Tree / graph / grid"} -->|"binary tree: visit order,<br/>depth, BST property"| P10["10 Binary Tree Traversal"]
    T -->|"shortest path, fewest steps,<br/>level by level"| P12["12 BFS"]
    T -->|"connected components, cycles,<br/>all paths, topological order"| P11["11 DFS"]
    T -->|"2-D grid of cells"| P13["13 Matrix Traversal"]
    P13 -.->|"shortest steps"| P12
    P13 -.->|"islands / flood fill"| P11
```

## Keyword lookup

| If the problem says… | Think | Complexity to aim for |
|---|---|---|
| "range sum", "sum of subarray equals k" | Prefix Sum | O(n) |
| "sorted array", "pair that sums to", "palindrome", "in-place" | Two Pointers | O(n) |
| "longest / shortest substring", "subarray of size k", "at most k distinct" | Sliding Window | O(n) |
| "cycle", "middle of list", "duplicate number in 1..n" | Fast & Slow | O(n), O(1) space |
| "reverse", "reorder list", "k-group" | In-place Reversal | O(n), O(1) space |
| "next greater", "warmer day", "histogram", "span" | Monotonic Stack | O(n) |
| "k-th largest", "top k", "k closest", "most frequent" | Top-K Heap | O(n log k) |
| "merge intervals", "meeting rooms", "overlap" | Intervals | O(n log n) |
| "sorted / rotated", "minimum speed / capacity such that…" | Binary Search | O(log n) or O(n log M) |
| "inorder", "level order", "depth", "BST" | Tree Traversal | O(n) |
| "connected", "provinces", "course schedule", "clone graph" | DFS | O(V + E) |
| "minimum steps", "shortest path" (unweighted), "spread" | BFS | O(V + E) |
| "grid", "islands", "flood fill", "spiral" | Matrix | O(R·C) |
| "all combinations", "generate", "n-queens" | Backtracking | O(2ⁿ) / O(n!) |
| "number of ways", "minimum cost", "longest increasing" | DP | O(states × work) |

!!! warning "Common confusions"
    - **Sliding window vs prefix sum:** a window needs **non-negative** numbers (or a monotone condition). With negatives, use prefix sum + hash map.
    - **BFS vs DFS:** both are O(V + E). Use **BFS when the answer is a distance**, DFS when you need to explore or check connectivity.
    - **Backtracking vs DP:** if the same sub-call `f(i, state)` repeats, add memoisation, which turns the backtracking solution into DP. If the task is to *list* every solution, it stays backtracking.
    - **Heap vs sort:** sorting costs O(n log n). A size-k heap costs O(n log k), which wins when k ≪ n.
