"""
APCS 排序範例 6：第 K 大元素（中高級）

找出未排序陣列中第 K 大的元素。
不使用完整排序（O(N log N)），而是用 Quick Select（平均 O(N)）。

核心：快速排序的分區（partition）概念 + 只遞迴其中一半。
"""

import random


def find_kth_largest(nums, k):
    def partition(left, right):
        pivot_idx = random.randint(left, right)
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        pivot = nums[right]
        store = left
        for i in range(left, right):
            if nums[i] > pivot:
                nums[store], nums[i] = nums[i], nums[store]
                store += 1
        nums[store], nums[right] = nums[right], nums[store]
        return store

    left, right = 0, len(nums) - 1
    while True:
        pos = partition(left, right)
        if pos == k - 1:
            return nums[pos]
        if pos > k - 1:
            right = pos - 1
        else:
            left = pos + 1


if __name__ == '__main__':
    data = [3, 2, 1, 5, 6, 4]
    print(find_kth_largest(data, 2))
    print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
