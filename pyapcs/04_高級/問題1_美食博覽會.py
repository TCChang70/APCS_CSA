"""
【APCS 高級】美食博覽會
試題來源：程式實作 2021 年 9 月

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
問題描述
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
共 n 個攤位，第 i 個提供美食品項 food[i]。
共 k 位試吃員，每人從某個攤位出發，依編號遞增逐一造訪，
若下一攤的美食是已吃過的品項則停止並離場。

目標：k 位試吃員造訪的攤位聯集（不重複計算）最多有幾個？

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
演算法說明
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
【預計算 reach[i]】（滑動視窗，O(n)）
  reach[i] = 從位置 i 出發，不重複美食的最遠結束位置（exclusive）。
  使用雙指標維護一個「無重複元素的視窗」[left, right)。

【DP 求最大聯集覆蓋】（O(n × k)）
  dp[j][i] = 使用 j 位試吃員，且第一位從索引 ≥ i 出發，
             最多能覆蓋的攤位數。

  轉移：dp[j][i] = max(
          dp[j][i+1],                    ← 跳過位置 i 不出發
          (reach[i] - i) + dp[j-1][reach[i]]  ← 從 i 出發，下一位從 reach[i] 開始
        )

  為節省空間，用兩個一維陣列滾動更新。

  答案：dp[k][0]

  觀察：相鄰出發位置的選擇不需重疊，因為重疊只會浪費覆蓋範圍。

時間複雜度：O(n) + O(n × k) = O(n × k) ≤ O(5 × 10^6) ✓
"""

import sys
from collections import defaultdict
input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    foods = list(map(int, input().split()))   # foods[i] = 攤位 i 的美食品項

    # ── 步驟一：預計算 reach[i]（滑動視窗） ───────────────────
    # reach[i] = 從位置 i 出發時，視窗最右端（exclusive），即可訪問 [i, reach[i])
    reach = [0] * (n + 1)   # reach[n] = n（哨兵）
    freq = defaultdict(int) # 目前視窗中各美食的出現次數
    right = 0               # 視窗右端（尚未加入）

    for left in range(n):
        # 若 left 向右移動，先從視窗中移除 foods[left - 1]（若 left > 0）
        if left > 0:
            freq[foods[left - 1]] -= 1
            if freq[foods[left - 1]] == 0:
                del freq[foods[left - 1]]

        # 向右擴展視窗，直到遇到重複或超出範圍
        while right < n and foods[right] not in freq:
            freq[foods[right]] += 1
            right += 1

        reach[left] = right   # [left, right) 是以 left 為起點的最大無重複視窗

    # ── 步驟二：DP 求最大覆蓋（滾動一維陣列） ─────────────────
    # prev_dp[i] = 使用 j-1 位試吃員從索引 ≥ i 出發的最大覆蓋
    # curr_dp[i] = 使用 j 位試吃員從索引 ≥ i 出發的最大覆蓋
    #
    # 從右往左計算（因為 dp[j][i] 依賴 dp[j][i+1] 和 dp[j-1][reach[i]]）

    # 初始化：0 位試吃員，覆蓋 = 0
    prev_dp = [0] * (n + 1)

    for _ in range(k):
        curr_dp = [0] * (n + 1)
        # 從右往左填表（curr_dp[n] = 0 已設定）
        for i in range(n - 1, -1, -1):
            # 選項 1：不從位置 i 出發，等候下一個位置
            skip = curr_dp[i + 1]
            # 選項 2：從位置 i 出發，取得 [i, reach[i]) 的攤位，
            #         剩餘試吃員從 reach[i] 開始
            take = (reach[i] - i) + prev_dp[reach[i]]
            curr_dp[i] = max(skip, take)
        prev_dp = curr_dp

    print(prev_dp[0])


if __name__ == '__main__':
    main()
