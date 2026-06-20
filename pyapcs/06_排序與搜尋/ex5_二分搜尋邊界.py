"""
APCS 排序範例 5：二分搜尋邊界（中級）

進階二分搜尋：在已排序陣列中找特定值的邊界。
- 第一個 >= target 的位置（lower_bound）
- 第一個 > target 的位置（upper_bound）

Python 內建 bisect 模組可直接使用，但理解原理對解變形題很重要。
APCS 應用：尋找插入位置、計算某數值區間內的元素數量。
"""

import bisect


def lower_bound(arr, target):
    """第一個 >= target 的索引"""
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(arr, target):
    """第一個 > target 的索引"""
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == '__main__':
    arr = [1, 2, 2, 2, 3, 4, 5]

    print(f"lower_bound(arr, 2) = {lower_bound(arr, 2)}")
    print(f"upper_bound(arr, 2) = {upper_bound(arr, 2)}")
    print(f"bisect_left(arr, 2) = {bisect.bisect_left(arr, 2)}")
    print(f"bisect_right(arr, 2) = {bisect.bisect_right(arr, 2)}")

    target = 2
    lb = bisect.bisect_left(arr, target)
    ub = bisect.bisect_right(arr, target)
    print(f"值 {target} 出現 {ub - lb} 次")
