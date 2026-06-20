"""
APCS 排序範例 1：三大基本排序實作（初級）

氣泡排序、選擇排序、插入排序的 Python 實作。
核心目的：理解排序演算法的工作原理，而非在實戰中使用。
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == '__main__':
    test = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(test.copy()))
    print(selection_sort(test.copy()))
    print(insertion_sort(test.copy()))
