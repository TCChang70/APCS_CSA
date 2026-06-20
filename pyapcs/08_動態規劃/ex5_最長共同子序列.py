"""
APCS DP 範例 5：最長共同子序列（中級）

LCS（Longest Common Subsequence）：
給定兩個字串 A 和 B，找出最長的共同子序列（不要求連續）。

狀態：dp[i][j] = A[:i] 與 B[:j] 的 LCS 長度
轉移：
  若 A[i-1] == B[j-1]：dp[i][j] = dp[i-1][j-1] + 1
  否則：dp[i][j] = max(dp[i-1][j], dp[i][j-1])

時間 O(N·M)，空間可壓縮至 O(min(N, M))。
"""


def lcs_length(A, B):
    n, m = len(A), len(B)
    dp = [0] * (m + 1)
    for i in range(1, n + 1):
        prev = 0
        for j in range(1, m + 1):
            temp = dp[j]
            if A[i - 1] == B[j - 1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            prev = temp
    return dp[m]


def lcs_string(A, B):
    """回傳 LCS 字串本身（完整 2D 表）"""
    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = n, m
    result = []
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            result.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(result))


if __name__ == '__main__':
    A, B = "ABCBDAB", "BDCAB"
    print(f"LCS 長度: {lcs_length(A, B)}")
    print(f"LCS 字串: {lcs_string(A, B)}")
