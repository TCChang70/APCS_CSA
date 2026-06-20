"""
APCS DP 範例 2：Kadane 演算法（中級）

最大連續子陣列和（Maximum Subarray）：
給定整數陣列，找一個連續子陣列使其總和最大。

核心：dp[i] = 以 i 結尾的最大子陣列和
  dp[i] = max(nums[i], dp[i-1] + nums[i])
  
時間 O(N)，空間 O(1)。Kadane 是 APCS 中級最常考的 DP 之一。
"""


def max_subarray(nums):
    cur = best = nums[0]
    for v in nums[1:]:
        cur = max(v, cur + v)
        best = max(best, cur)
    return best


def max_subarray_with_indices(nums):
    cur = best = nums[0]
    start = end = 0
    temp_start = 0
    for i, v in enumerate(nums[1:], 1):
        if v > cur + v:
            cur = v
            temp_start = i
        else:
            cur = cur + v
        if cur > best:
            best = cur
            start = temp_start
            end = i
    return best, start, end


if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"最大子陣列和: {max_subarray(arr)}")

    best, s, e = max_subarray_with_indices(arr)
    print(f"最大子陣列: {arr[s:e+1]}, 和 = {best}")
