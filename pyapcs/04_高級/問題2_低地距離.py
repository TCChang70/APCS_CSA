"""
【APCS 高級】低地距離
試題來源：程式實作 2020 年 10 月

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
問題描述
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
共 2n 座碉堡，每種高度 k（1 ≤ k ≤ n）恰好出現兩次。

對每種高度 k，設兩座碉堡位置為 p < q：
  低地距離 d(k) = 在 (p, q) 之間且高度 < k 的碉堡數量

計算 Σ d(k)（k 從 1 到 n 的總和）。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
演算法說明（Binary Indexed Tree / Fenwick Tree，O(n log n)）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
觀察：
  d(k) = (在位置 q 之前，高度 < k 的碉堡數)
       − (在位置 p 之前，高度 < k 的碉堡數)
  因為 h[p] = k，h[p] 本身不小於 k，故等式成立。

演算法：
  從左到右掃描，維護一個「樹狀陣列（BIT）」，索引為高度值。
  - 遇到高度 v 的第一次出現：記錄 first_count[v] = BIT.query(v-1)
                             （目前已有多少高度 < v 的碉堡）
  - 遇到高度 v 的第二次出現：d(v) = BIT.query(v-1) − first_count[v]
                             total += d(v)
  - 每次將當前高度 v 插入 BIT（update(v, +1)）

BIT（樹狀陣列）支援：
  - update(i, delta)：O(log n)  在索引 i 加上 delta
  - query(i)        ：O(log n)  查詢前綴和 [1..i]

注意：答案可能超過 2^31，Python 的大整數自動處理。
"""

import sys
input = sys.stdin.readline


class BIT:
    """
    樹狀陣列（Binary Indexed Tree / Fenwick Tree）。
    支援單點更新與前綴求和，時間複雜度均為 O(log n)。
    索引從 1 開始。
    """

    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)   # 內部陣列（1-indexed）

    def update(self, i: int, delta: int = 1):
        """在位置 i 加上 delta（向高位進位更新）"""
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)    # 低位 1 進位：i += i & (-i)

    def query(self, i: int) -> int:
        """查詢前綴和 [1..i]（向低位退位求和）"""
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)    # 低位 1 退位：i -= i & (-i)
        return s


def main():
    n = int(input())              # 共 2n 座碉堡
    heights = list(map(int, input().split()))   # 2n 個高度值

    bit = BIT(n)                  # BIT 索引範圍：高度 1 ~ n
    first_count = {}              # first_count[v] = 遇到 v 第一次時，BIT.query(v-1) 的值
    total = 0                     # 低地距離總和

    for v in heights:
        if v not in first_count:
            # 第一次遇到高度 v
            # 記錄此時「高度 < v 的碉堡數量」
            first_count[v] = bit.query(v - 1)
            bit.update(v)         # 將 v 插入 BIT
        else:
            # 第二次遇到高度 v（位置 q）
            # d(v) = 現在高度 < v 的總數 − 第一次出現前的高度 < v 的總數
            #       = 兩個位置之間，高度 < v 的碉堡數
            d = bit.query(v - 1) - first_count[v]
            total += d
            bit.update(v)         # 將 v 插入 BIT

    print(total)


if __name__ == '__main__':
    main()
