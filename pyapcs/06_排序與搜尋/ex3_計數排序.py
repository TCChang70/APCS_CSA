"""
APCS 排序範例 3：計數排序（初級）

當資料值域很小（如成績 0~100、年齡 0~150）時，
計數排序可以達到 O(N + K)，比比較排序更快。

APCS 應用場景：統計各分數級距人數、字母出現頻率排序。
"""


def counting_sort(arr, max_val):
    freq = [0] * (max_val + 1)
    for v in arr:
        freq[v] += 1
    result = []
    for v in range(max_val + 1):
        result.extend([v] * freq[v])
    return result


def grade_distribution(scores):
    freq = [0] * 101
    for s in scores:
        freq[s] += 1
    print("分數分布：")
    for score in range(101):
        if freq[score] > 0:
            print(f"  {score}分: {freq[score]}人")


if __name__ == '__main__':
    data = [4, 2, 2, 8, 3, 3, 1, 5, 2, 4]
    print(counting_sort(data, max(data)))

    scores = [72, 85, 72, 91, 85, 68, 72, 91, 100, 55]
    grade_distribution(scores)
