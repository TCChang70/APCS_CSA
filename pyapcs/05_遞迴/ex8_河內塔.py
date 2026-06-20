"""
APCS 遞迴範例 8：河內塔（經典遞迴，中級）

經典遞迴問題：將 N 個圓盤從 A 柱移動到 C 柱，B 柱輔助。
規則：
1. 一次只能移動一個圓盤
2. 大的圓盤不能放在小的上面

遞迴策略：
1. 將 N-1 個盤子從 A→B（C 輔助）
2. 將第 N 個盤子從 A→C
3. 將 N-1 個盤子從 B→C（A 輔助）

APCS 常見變化：計算最少移動次數（(2ⁿ - 1)），
或列印特定步驟的移動過程。
"""


def hanoi(n, src, dst, aux):
    """河內塔：將 n 個盤子從 src 移動到 dst，aux 為輔助柱"""
    if n == 0:
        return
    hanoi(n - 1, src, aux, dst)
    print(f"移動盤子 {n}：{src} → {dst}")
    hanoi(n - 1, aux, dst, src)


def hanoi_count(n):
    """河內塔最少步數：2ⁿ - 1"""
    if n == 1:
        return 1
    return 2 * hanoi_count(n - 1) + 1


if __name__ == '__main__':
    print(f"3 層河內塔最少步數：{hanoi_count(3)}")
    print("移動步驟：")
    hanoi(3, 'A', 'C', 'B')
