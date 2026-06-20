"""
APCS 堆疊範例 5：單調佇列（中高級）

經典題型：Sliding Window Maximum。
給定陣列和視窗大小 k，找出每個滑動視窗中的最大值。

核心：用 deque 維護一個「遞減」的佇列，
佇列前端永遠是當前視窗的最大值。
時間複雜度 O(N)，暴力法 O(N·K)。

APCS 應用：即時股價分析、感測器數據流處理。
"""

from collections import deque


def max_sliding_window(nums, k):
    dq = deque()
    result = []
    for i, v in enumerate(nums):
        while dq and nums[dq[-1]] < v:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result


if __name__ == '__main__':
    print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
