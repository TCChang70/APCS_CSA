"""
【APCS 排序搜尋練習題 3】二分搜尋查詢系統（初級）

問題描述
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
給定一個已排序的整數陣列（由小到大，可能有重複值），
共有 Q 筆查詢，每筆查詢輸入一個目標值 target，
請輸出：

- 第一個 ≥ target 的位置（lower_bound，從 0 開始）
- 第一個 > target 的位置（upper_bound，從 0 開始）
若 target 不存在於陣列中，則 lower_bound = upper_bound
若所有元素都小於 target，則回傳陣列長度

輸入格式
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
第一行：兩個正整數 N 和 Q（1 ≤ N, Q ≤ 10⁵）
第二行：N 個已排序整數
接下來 Q 行：每行一個整數 target

輸出格式
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
對每個查詢輸出一行「lower_bound upper_bound」
以及 target 在陣列中出現的次數（即 upper_bound - lower_bound）

範例輸入
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
8 4
1 2 2 2 3 4 5 5
2
5
6
0

範例輸出
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1 4 3
6 8 2
8 8 0
0 0 0

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
演算法說明
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Python 內建 bisect 模組：
- bisect_left(arr, target) = 第一個 ≥ target 的位置
- bisect_right(arr, target) = 第一個 > target 的位置
對每個查詢 O(log N)，總時間 O((N+Q) log N)
"""

import sys
import bisect
input = sys.stdin.readline


def main():
    N, Q = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(Q):
        target = int(input())
        lb = bisect.bisect_left(arr, target)
        ub = bisect.bisect_right(arr, target)
        print(lb, ub, ub - lb)


if __name__ == '__main__':
    main()
