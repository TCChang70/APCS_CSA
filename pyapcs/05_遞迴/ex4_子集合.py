"""
APCS 遞迴範例 4：子集合（Backtracking，中級）

給定一組不重複數字，回傳所有可能的子集合（幂集）。
遞迴策略：對每個元素選擇「取」或「不取」，形成二元樹。

APCS 常考變化：
- 子集合總和是否等於目標值
- 子集合元素數量限制
"""


def subsets(nums):
    ans = []

    def backtrack(start, path):
        ans.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return ans


def subset_sum(nums, target):
    """是否存在子集合總和等於 target"""
    def dfs(i, cur):
        if cur == target:
            return True
        if i == len(nums) or cur > target:
            return False
        return dfs(i + 1, cur + nums[i]) or dfs(i + 1, cur)

    return dfs(0, 0)


if __name__ == '__main__':
    print(subsets([1, 2, 3]))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
