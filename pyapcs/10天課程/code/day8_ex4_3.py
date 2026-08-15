from collections import deque

n, m = map(int, input().split())          # 迷宮大小（列、行）
grid = [list(input().strip()) for _ in range(n)]  # 逐列讀入：'.' 可走、'#' 是牆
dist = [[-1] * m for _ in range(n)]       # dist[i][j] = 起點到 (i,j) 的最短步數
q = deque()
dist[0][0] = 0                            # 起點 (0,0) 距離 0
q.append((0, 0))                          # 起點座標放入佇列
dirs = [(-1,0),(1,0),(0,-1),(0,1)]        # 上、下、左、右

while q:
    i, j = q.popleft()                    # 取出「最早進佇列」的格子（FIFO）
    if (i, j) == (n - 1, m - 1):          # 到達終點 (n-1, m-1)
        print(dist[i][j])                 # 第一次到就是最短步數 → 印出並結束
        break
    for di, dj in dirs:                   # 往 4 個方向擴散
        ni, nj = i + di, j + dj           # 鄰居座標
        # 四個條件都成立才能走：在矩陣內 且 沒走過 且 不是牆壁 '#'
        if 0 <= ni < n and 0 <= nj < m and dist[ni][nj] == -1 and grid[ni][nj] != '#':
            dist[ni][nj] = dist[i][j] + 1 # 步數 +1
            print(f"dist[{ni}][{nj}] = {dist[ni][nj]}")  # 印出每個格子最短步數
            q.append((ni, nj))            # 放入佇列，等下一輪擴散

# 5 5
# .....
# ##.##
# .#...
# .###.
# .....