# One-Page Cheatsheet

Use this page for self-quizzing: cover the right side, read a pattern name, and recall its signal, skeleton and complexity.

| # | Pattern | Signal | Skeleton | Time | Space |
|---|---|---|---|---|---|
| 1 | Prefix Sum | range sums, sum = k | `P[i+1]=P[i]+x` · `sum(i..j)=P[j+1]-P[i]` · `cnt+=seen[run-k]` | O(n) + O(1)/q | O(n) |
| 2 | Two Pointers | sorted pair, palindrome | `l,r=0,n-1` · `while l<r:` move the side that helps | O(n) | O(1) |
| 3 | Sliding Window | longest/shortest contiguous | `for r: add(r)` · `while bad: remove(l); l+=1` · update best | O(n) | O(k) |
| 4 | Fast & Slow | cycle, middle | `slow=slow.next; fast=fast.next.next` · meet → cycle | O(n) | O(1) |
| 5 | List Reversal | reverse / reorder | `nxt=cur.next; cur.next=prev; prev=cur; cur=nxt` | O(n) | O(1) |
| 6 | Monotonic Stack | next greater/smaller | `while st and a[st[-1]]<x: ans[st.pop()]=i` · `st.append(i)` | O(n) | O(n) |
| 7 | Top-K | k largest / frequent | `heappush(h,x)` · `if len(h)>k: heappop(h)` | O(n log k) | O(k) |
| 8 | Intervals | merge / overlap | `sort by start` · `if s<=out[-1][1]: extend else append` | O(n log n) | O(n) |
| 9 | Binary Search | sorted, min-max, O(log n) | `while lo<hi: mid; if ok(mid): hi=mid else lo=mid+1` | O(log n) | O(1) |
| 10 | Tree Traversal | pre/in/post/level | `dfs(n.left); visit(n); dfs(n.right)` / queue per level | O(n) | O(h) |
| 11 | DFS | components, cycles, paths | `visited.add(u); for v in g[u]: if v not in visited: dfs(v)` | O(V+E) | O(V) |
| 12 | BFS | fewest steps | `q=deque([s]); while q: for _ in range(len(q)): …` | O(V+E) | O(V) |
| 13 | Matrix | grid, islands | `for dr,dc in DIRS: if in bounds and not seen: …` | O(R·C) | O(R·C) |
| 14 | Backtracking | all combos / perms | `path.append(c); bt(); path.pop()` | O(2ⁿ)/O(n!) | O(n) |
| 15 | DP | count ways / min cost | `dp[i] = best(dp[i-1], dp[i-2] + …)` · `@cache` | O(states·work) | O(states) |

## The complexity reasons in one breath

!!! success "Say it like this"
    *"Each element is touched a constant number of times, so O(n). Halving gives O(log n). Sorting sets an O(n log n) floor. A heap of size k gives O(n log k). Visiting every node and edge once is O(V + E). A recursion tree costs branches to the power of depth, and memoising it costs states times work per state."*

## Python idioms worth knowing by heart

```python
from collections import defaultdict, Counter, deque
from functools import cache
import heapq, bisect

seen = defaultdict(int)            # counts without KeyError
freq = Counter(nums)               # freq.most_common(k)
q = deque([start]); q.popleft()    # O(1) queue
heapq.heappush(h, (-x, i))         # max-heap via negation
i = bisect.bisect_left(arr, x)     # first index with arr[i] >= x
DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

@cache
def dp(i): ...                     # memoised top-down DP
```
