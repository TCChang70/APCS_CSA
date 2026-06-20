"""
【APCS 遞迴練習題 4】排列生成（中級）

問題描述
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
給定 N 個相異的正整數，請使用遞迴 Backtracking 輸出所有可能的排列。

排列數 = N!，N ≤ 8 以確保輸出在合理範圍內。

輸入格式
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
第一行：一個正整數 N（1 ≤ N ≤ 8）
第二行：N 個相異的正整數

輸出格式
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
輸出所有排列，每行一個排列，數字以空白間隔。
輸出順序請依照字典序（lexicographical order）。

範例輸入
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3
1 2 3

範例輸出
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
演算法說明
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Backtracking 排列模板：
1. 對每個位置嘗試所有尚未使用的數字
2. 選擇一個數字 → 標記已用 → 遞迴下一層 → 取消標記
3. 為確保字典序，先將數字排序再進行遞迴
時間複雜度 O(N!)
"""

import sys
input = sys.stdin.readline


def main():
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    used = [False] * N
    path = []

    def backtrack():
        if len(path) == N:
            print(' '.join(map(str, path)))
            return
        for i in range(N):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False

    backtrack()


if __name__ == '__main__':
    main()
