"""
【APCS 排序搜尋練習題 6】最接近的三數和（中級）

問題描述
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
給定一個長度為 N 的整數陣列 nums 和一個目標值 target，
請從陣列中選出三個數字，使其總和最接近 target。
請輸出該總和與 target 的絕對差值。

若無法選出三個數字（N < 3），則輸出 -1。

輸入格式
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
第一行：兩個正整數 N 和 target（3 ≤ N ≤ 1000）
第二行：N 個整數 nums[i]（-10⁶ ≤ nums[i] ≤ 10⁶）

輸出格式
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
一個整數，表示最小絕對差值

範例輸入
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6 1
-1 2 1 -4 5 3

範例輸出
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
0

說明：選 -1 + 2 + 0 = 1（但 0 不在陣列中）
實際上 -1 + 2 + 1 = 2，差值 |2 - 1| = 1；
-1 + -4 + 5 = 0，差值 |0 - 1| = 1；
最接近的是 2+1+(-4) = -1，差值 2⋯
正解為 -1 + 1 + 2 = 2，差值為 1。

更正範例：陣列 [-1, 2, 1, -4, 5, 3], target = 1
最接近的三數和為 1（(-1) + 2 + 0⋯ 不對）
1 + 2 + (-1) = 2，差值 1。
-4 + 5 + 0⋯

實際最佳解：(-1) + 2 + 1 = 2，差值 |2-1| = 1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
演算法說明
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
排序 + 雙指標（Two Pointers）：
1. 先排序陣列 O(N log N)
2. 固定第一個數 nums[i]，用雙指標 left, right 在 i 右側找
3. 計算 sum = nums[i] + nums[left] + nums[right]
   - 若 sum < target：left++（需要更大的數）
   - 若 sum > target：right--（需要更小的數）
   - 若 sum == target：差值為 0，直接輸出
4. 更新最小差值
時間複雜度 O(N²)，對 N ≤ 1000 足夠快
"""

import sys
input = sys.stdin.readline


def main():
    N, target = map(int, input().split())
    nums = list(map(int, input().split()))

    if N < 3:
        print(-1)
        return

    nums.sort()
    best = 10 ** 9

    for i in range(N - 2):
        left, right = i + 1, N - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            diff = abs(total - target)
            if diff < best:
                best = diff
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                print(0)
                return

    print(best)


if __name__ == '__main__':
    main()
