"""
APCS 排序範例 4：區間合併（中級）

給定多個區間 [start, end]，合併所有重疊的區間。
策略：依 start 排序 → 依序檢查是否能合併。

APCS 應用：會議時間安排、程式執行區段合併、覆蓋範圍計算。
"""


def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [list(intervals[0])]
    for s, e in intervals[1:]:
        if s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    return merged


if __name__ == '__main__':
    tests = [
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
        [[1, 2], [3, 4], [5, 6]],
    ]
    for t in tests:
        print(f"{t} → {merge_intervals(t)}")
