# Patterns

The 15 patterns are grouped by the data structure they usually work on. Work through them in order; later groups reuse ideas from earlier ones (BFS reuses the queue from level-order traversal, DP is backtracking plus memo).

```mermaid
graph TD
    subgraph AS["Arrays and Strings"]
        P1["1 Prefix Sum"] --> P2["2 Two Pointers"] --> P3["3 Sliding Window"]
    end
    subgraph LL["Linked Lists"]
        P4["4 Fast and Slow"] --> P5["5 In-place Reversal"]
    end
    subgraph SH["Stacks and Heaps"]
        P6["6 Monotonic Stack"] --> P7["7 Top-K"]
    end
    subgraph IS["Intervals and Search"]
        P8["8 Intervals"] --> P9["9 Binary Search"]
    end
    subgraph TG["Trees and Graphs"]
        P10["10 Tree Traversal"] --> P11["11 DFS"] --> P12["12 BFS"] --> P13["13 Matrix"]
    end
    subgraph SS["Search Spaces"]
        P14["14 Backtracking"] --> P15["15 DP"]
    end
    P2 -.->|"pointers on nodes"| P4
    P3 -.->|"window max uses a deque"| P6
    P10 -.->|"generalise to graphs"| P11
    P11 -.->|"add memo"| P15
```

| Group | Patterns | Shared idea |
|---|---|---|
| Arrays & Strings | [Prefix Sum](prefix-sum.md) · [Two Pointers](two-pointers.md) · [Sliding Window](sliding-window.md) | replace the O(n²) pair scan with one O(n) pass |
| Linked Lists | [Fast & Slow](fast-slow-pointers.md) · [In-place Reversal](linked-list-reversal.md) | O(1) extra space by rewiring / racing pointers |
| Stacks & Heaps | [Monotonic Stack](monotonic-stack.md) · [Top-K](top-k-elements.md) | the right container keeps only what still matters |
| Intervals & Search | [Overlapping Intervals](overlapping-intervals.md) · [Binary Search](modified-binary-search.md) | sorted order unlocks the answer |
| Trees & Graphs | [Tree Traversal](binary-tree-traversal.md) · [DFS](depth-first-search.md) · [BFS](breadth-first-search.md) · [Matrix](matrix-traversal.md) | visit each node once → O(V + E) |
| Search Spaces | [Backtracking](backtracking.md) · [DP](dynamic-programming.md) | enumerate choices; cache repeated sub-answers |
