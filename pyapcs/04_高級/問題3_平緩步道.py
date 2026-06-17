"""
【APCS 高級】平緩步道
試題來源：程式實作 2022 年 10 月

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
問題描述
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
n×n 的方格地圖，每格有高度值。
入口在左上角 (0,0)，出口在右下角 (n-1,n-1)。

相鄰兩格的「坡度」= 兩格高度差的絕對值。

目標（雙重最優）：
  1. 最小化步道上相鄰格最大坡度（主要目標）
  2. 在最小坡度條件下，最小化步道長度（步數 = 格子數 − 1）

輸出：最小坡度、最短步道長度（步數）。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
演算法說明
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
【步驟一：二分搜尋最小坡度 S】
  對坡度 S 做二分搜尋（範圍 0 ~ max_height = 10^6）：
    - 用 BFS/DFS 檢查是否存在「僅走坡度 ≤ S 的邊」能從入口到出口
    - 找到最小的可行 S

  二分搜尋：O(n² × log(max_height))

【步驟二：BFS 求最短路徑】
  以找到的最小坡度 S，BFS（等距圖）求 (0,0) 到 (n-1,n-1) 的最短步數。
  BFS 只走「坡度 ≤ S」的邊，BFS 的最短路即為最少步數。

  BFS：O(n²)

總時間複雜度：O(n² × log(max_height))，n ≤ 300，max_height ≤ 10^6
  → 300² × 20 ≈ 1.8 × 10^6 → 在時間限制內 ✓
"""

import sys
from collections import deque
input = sys.stdin.readline

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 上、下、左、右


def main():
    n = int(input())

    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))

    # ── 步驟一：二分搜尋最小坡度 ────────────────────────────
    def can_reach(S):
        """
        BFS：判斷在坡度上限 S 下，能否從 (0,0) 到 (n-1,n-1)。
        只走「相鄰格高度差 ≤ S」的邊。
        """
        if n == 1:
            return True   # 起點 = 終點
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        q = deque([(0, 0)])
        while q:
            r, c = q.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if (0 <= nr < n and 0 <= nc < n
                        and not visited[nr][nc]
                        and abs(grid[nr][nc] - grid[r][c]) <= S):
                    if nr == n - 1 and nc == n - 1:
                        return True   # 提早終止
                    visited[nr][nc] = True
                    q.append((nr, nc))
        return visited[n - 1][n - 1]

    lo, hi = 0, 10 ** 6
    while lo < hi:
        mid = (lo + hi) // 2
        if can_reach(mid):
            hi = mid        # mid 可行，嘗試更小的坡度
        else:
            lo = mid + 1    # mid 不可行，需要更大的坡度

    min_slope = lo   # 最小坡度

    # ── 步驟二：BFS 求最短路徑長度 ──────────────────────────
    def shortest_path(S):
        """
        BFS：在坡度上限 S 下，求 (0,0) 到 (n-1,n-1) 的最短步數。
        因為每步距離均為 1，BFS 保證找到最短路。
        回傳：步數（= 經過的邊數 = 經過格子數 − 1）
        """
        dist = [[-1] * n for _ in range(n)]
        dist[0][0] = 0
        q = deque([(0, 0)])
        while q:
            r, c = q.popleft()
            if r == n - 1 and c == n - 1:
                return dist[r][c]
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if (0 <= nr < n and 0 <= nc < n
                        and dist[nr][nc] == -1
                        and abs(grid[nr][nc] - grid[r][c]) <= S):
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
        return dist[n - 1][n - 1]   # 必然可達（已驗證）

    min_length = shortest_path(min_slope)

    # ── 輸出 ─────────────────────────────────────────────────
    print(min_slope)    # 第一行：最小坡度
    print(min_length)   # 第二行：在最小坡度下的最短步道長度（步數）


if __name__ == '__main__':
    main()
