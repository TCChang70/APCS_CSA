"""
APCS DP 範例 4：最長遞增子序列（中級）

LIS（Longest Increasing Subsequence）：
給定整數陣列，找最長的嚴格遞增子序列（不要求連續）。

DP 解 O(N²)：
  dp[i] = 以 nums[i] 結尾的 LIS 長度
  dp[i] = max(dp[j] + 1) for j < i and nums[j] < nums[i]

貪婪 + 二分搜尋 O(N log N)：
  維護 tails 陣列，tails[l] = 長度 l+1 的 LIS 中結尾的最小值
"""


def lis_dp(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def lis_bs(nums):
    tails = []
    for v in nums:
        lo, hi = 0, len(tails)
        while lo < hi:
            mid = (lo + hi) // 2
            if tails[mid] < v:
                lo = mid + 1
            else:
                hi = mid
        if lo == len(tails):
            tails.append(v)
        else:
            tails[lo] = v
    return len(tails)


if __name__ == '__main__':
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"LIS (DP): {lis_dp(arr)}")
    print(f"LIS (BS): {lis_bs(arr)}")
