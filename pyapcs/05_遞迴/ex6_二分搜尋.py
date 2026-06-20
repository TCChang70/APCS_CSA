"""
APCS 遞迴範例 6：二分搜尋（分治法，中級）

在已排序的陣列中尋找目標值。
遞迴策略：每次將搜尋範圍縮小一半。

時間複雜度：O(log N)
空間複雜度：O(log N)（遞迴深度）
"""


def binary_search(arr, target):
    def helper(left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            return helper(left, mid - 1)
        return helper(mid + 1, right)

    return helper(0, len(arr) - 1)


def find_max(arr):
    """分治法找最大值"""
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2
    left_max = find_max(arr[:mid])
    right_max = find_max(arr[mid:])
    return left_max if left_max > right_max else right_max


if __name__ == '__main__':
    nums = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(nums, 7))
    print(binary_search(nums, 4))
    print(find_max([3, 7, 2, 9, 5, 1, 8]))
