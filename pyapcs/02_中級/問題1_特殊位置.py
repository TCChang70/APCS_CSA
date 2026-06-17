"""
【APCS 中級】特殊位置
試題來源：程式實作 2023 年 6 月

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
問題描述
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
給定一個 n×m 的正整數陣列 A（元素值為 1~9）。

兩元素 A[i][j] 與 A[s][t] 的距離 = |i-s| + |j-t|（曼哈頓距離）。

判斷「特殊位置」：對於 A[i][j] = x，
  若「與其距離 ≤ x 的所有元素總和（含自身）mod 10」= x mod 10，
  則 (i, j) 為特殊位置。

輸出特殊位置總數 k，再依照「列小→行小」輸出每個特殊位置。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
演算法說明
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
暴力枚舉：對每個位置 (i,j)，枚舉所有距離 ≤ x 的格子並求和。
  曼哈頓距離 ≤ x 的格子範圍：
    行(row) 差 <= x，列(col) 差 <= x - |row_diff|
  合法範圍限縮：0 ≤ s < n, 0 ≤ t < m

元素值最大為 9，n, m ≤ 50 → 最多掃描直徑為 9 的菱形 ≈ 181 個格子。
總時間複雜度：O(n × m × x_max²) = O(50 × 50 × 81) ≈ 202,500 → 非常快。
"""

import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())   # n 列 m 行

    # 讀入整個二維陣列
    A = []
    for _ in range(n):
        row = list(map(int, input().split()))
        A.append(row)

    special = []   # 儲存所有特殊位置

    for i in range(n):
        for j in range(m):
            x = A[i][j]   # 目標元素值

            # ── 計算距離 ≤ x 的元素總和 ──────────────────────
            total = 0
            # 行差 dr 從 -x 到 x
            for dr in range(-x, x + 1):
                s = i + dr             # 目標行（row）
                if s < 0 or s >= n:    # 超出陣列範圍，跳過
                    continue
                # 在行差為 dr 的情況下，剩餘可用的列差為 x - |dr|
                max_dc = x - abs(dr)
                for dc in range(-max_dc, max_dc + 1):
                    t = j + dc         # 目標列（col）
                    if t < 0 or t >= m:
                        continue
                    total += A[s][t]   # 累加元素值

            # ── 判斷是否為特殊位置 ────────────────────────────
            # 總和 mod 10 是否與 x mod 10 相同
            # 因為 x 為 1~9（皆 < 10），x mod 10 = x
            if total % 10 == x % 10:
                special.append((i, j))

    # ── 輸出 ─────────────────────────────────────────────────
    print(len(special))           # 特殊位置總數
    for (r, c) in special:
        print(r, c)               # 依列小→行小順序輸出（已是自然順序）


if __name__ == '__main__':
    main()
