"""
APCS 遞迴範例 7：合併排序（分治法，中級）

經典的分治排序演算法：
1. 分割：將陣列分成兩半
2. 遞迴：分別對兩半排序
3. 合併：將兩個已排序的子陣列合併

時間複雜度：O(N log N)
空間複雜度：O(N)
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == '__main__':
    data = [38, 27, 43, 3, 9, 82, 10]
    print(merge_sort(data))
