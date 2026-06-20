"""
APCS 堆疊範例 4：單調堆疊（中高級）

經典題型：Next Greater Element（下一個更大元素）。
給定陣列，對每個元素找右邊第一個比它大的值。

核心：維護一個「遞減」的堆疊，遇到更大的值就 pop 並記錄答案。
時間複雜度 O(N)，暴力法 O(N²)。

APCS 應用：大樓下雨積水、海拔分析、溫度預測。
"""


def next_greater_element(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            ans[idx] = nums[i]
        stack.append(i)
    return ans


def largest_rectangle_area(heights):
    """直方圖中最大的長方形面積（經典單調堆疊題）"""
    stack = []
    max_area = 0
    heights = [0] + heights + [0]
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area


if __name__ == '__main__':
    print(next_greater_element([2, 1, 2, 4, 3]))
    print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))
