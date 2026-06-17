"""
【APCS 中高級】連鎖反應
試題來源：程式實作 2024 年 10 月

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
問題描述
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
M×N 的場地，格子值：
  -2 = 寶藏位置（起始陷阱）
  -1 = 石頭（訊號無法穿越）
  非負整數 = 陷阱的影響半徑（0 代表不觸發其他陷阱）

觸發規則：
  一個影響半徑為 x 的陷阱被觸發後，以 BFS（避開石頭與界外）
  距離 ≤ x 的所有陷阱也被觸發（可能造成連鎖反應）。

求寶藏位置「最小初始半徑 R」，使得至少 Q 個陷阱被觸發。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
演算法說明
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. 二分搜尋 R（範圍 0 ~ M+N，因為 M+N 是最大 BFS 距離）。
2. 對每個候選 R，模擬連鎖反應：
     a. BFS 從寶藏出發，找出距離 ≤ R 的所有格子，觸發陷阱。
     b. 每個新觸發的陷阱若半徑 > 0，加入待處理佇列。
     c. 反覆從佇列取出陷阱，BFS 觸發其半徑內的更多陷阱。
     d. 回傳觸發陷阱總數。
3. 找到最小 R 使觸發數 ≥ Q。

BFS 避開石頭，實際影響範圍受石頭阻擋（非單純曼哈頓距離）。
時間複雜度：O(log(M+N) × K × r_max²)，K ≤ 1500，r_max ≤ 30
"""

import sys
from collections import deque
input = sys.stdin.readline


def main():
    M, N, Q = map(int, input().split())

    grid = []
    treasure_r, treasure_c = 0, 0
    for i in range(M):
        row = list(map(int, input().split()))
        grid.append(row)
        for j in range(N):
            if row[j] == -2:
                treasure_r, treasure_c = i, j  # 記錄寶藏位置

    def simulate(R):
        """
        模擬以初始半徑 R 觸發寶藏陷阱後的連鎖反應。

        回傳：觸發的陷阱總數。
        """
        # triggered[i][j] = True 表示 (i,j) 的陷阱已被觸發
        triggered = [[False] * N for _ in range(M)]
        triggered[treasure_r][treasure_c] = True
        count = 1

        # 待處理佇列：(起點行, 起點列, 影響半徑)
        to_process = deque()
        to_process.append((treasure_r, treasure_c, R))

        while to_process:
            sr, sc, radius = to_process.popleft()

            # ── BFS：從 (sr, sc) 出發，找距離 ≤ radius 的所有可達格子 ──
            # 使用 deque + 距離追蹤（BFS 層次 = 步數距離）
            bfs_visited = set()
            bfs_visited.add((sr, sc))
            bfs_q = deque()
            bfs_q.append((sr, sc, 0))   # (行, 列, 已走步數)

            while bfs_q:
                r, c, d = bfs_q.popleft()

                # 若當前步數已達半徑上限，不再繼續向外擴展
                if d >= radius:
                    continue

                # 向四個方向擴展
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r + dr, c + dc
                    # 邊界檢查、石頭排除、已訪問排除
                    if (0 <= nr < M and 0 <= nc < N
                            and (nr, nc) not in bfs_visited
                            and grid[nr][nc] != -1):
                        bfs_visited.add((nr, nc))
                        # 若此格陷阱尚未觸發，觸發它
                        if not triggered[nr][nc]:
                            triggered[nr][nc] = True
                            count += 1
                            val = grid[nr][nc]
                            # 若影響半徑 > 0，加入連鎖反應佇列
                            if val > 0:
                                to_process.append((nr, nc, val))
                        bfs_q.append((nr, nc, d + 1))

        return count

    # ── 二分搜尋最小初始半徑 R ──────────────────────────────
    # 觸發數是 R 的單調遞增函數
    lo, hi = 0, M + N   # R 最大不超過整個場地的對角距離
    while lo < hi:
        mid = (lo + hi) // 2
        if simulate(mid) >= Q:
            hi = mid        # mid 可行，嘗試更小
        else:
            lo = mid + 1    # mid 不夠，需要更大

    print(lo)


if __name__ == '__main__':
    main()
