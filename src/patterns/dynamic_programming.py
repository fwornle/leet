"""Pattern 15 · Dynamic Programming.

Sections between `--8<-- [start:x]` / `[end:x]` markers are embedded
into docs/patterns/dynamic-programming.md, so every snippet shown there is tested.
"""

from functools import cache


# --8<-- [start:template_top_down]
def fib_memo(n: int) -> int:
    @cache                          # memo: each state computed exactly once
    def f(i: int) -> int:
        if i < 2:                   # base case
            return i
        return f(i - 1) + f(i - 2)  # recurrence
    return f(n)
# --8<-- [end:template_top_down]


# --8<-- [start:template_bottom_up]
def fib_table(n: int) -> int:
    if n < 2:
        return n
    dp = [0] * (n + 1)              # state: dp[i] = fib(i)
    dp[1] = 1                       # base cases
    for i in range(2, n + 1):       # order: smaller i first
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
# --8<-- [end:template_bottom_up]


# --8<-- [start:climbing_stairs]
def climb_stairs(n: int) -> int:  # LeetCode 70
    one_back, two_back = 1, 1       # ways(i-1), ways(i-2): only 2 states needed
    for _ in range(n - 1):
        one_back, two_back = one_back + two_back, one_back
    return one_back
# --8<-- [end:climbing_stairs]


# --8<-- [start:house_robber]
def rob(nums: list[int]) -> int:  # LeetCode 198
    skip, take = 0, 0               # best so far without / with robbing previous house
    for money in nums:
        skip, take = max(skip, take), skip + money
    return max(skip, take)
# --8<-- [end:house_robber]


# --8<-- [start:coin_change]
def coin_change(coins: list[int], amount: int) -> int:  # LeetCode 322
    INF = amount + 1
    dp = [0] + [INF] * amount       # dp[a] = fewest coins to make amount a
    for a in range(1, amount + 1):
        for coin in coins:          # try every coin as the LAST coin
            if coin <= a:
                dp[a] = min(dp[a], dp[a - coin] + 1)
    return dp[amount] if dp[amount] != INF else -1
# --8<-- [end:coin_change]


# --8<-- [start:lcs]
def longest_common_subsequence(text1: str, text2: str) -> int:  # LeetCode 1143
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]   # dp[i][j] = LCS of text1[:i], text2[:j]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1          # match: extend diagonal
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # drop one char
    return dp[m][n]
# --8<-- [end:lcs]
