"""
APCS 堆疊範例 3：BFS 最短路徑（中級）

使用 Queue 實作廣度優先搜尋，在無權重地圖中 
找從起點到終點的最短路徑長度（每一步花費 1）。

APCS 應用：迷宮最短路徑、病毒感染擴散、城市間最少轉乘。
"""

from collections import deque


def bfs_shortest_path(grid, sr, sc, er, ec):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    q = deque()
    q.append((sr, sc, 0))
    visited[sr][sc] = True

    while q:
        r, c, dist = q.popleft()
        if r == er and c == ec:
            return dist
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if not visited[nr][nc] and grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    q.append((nr, nc, dist + 1))
    return -1


if __name__ == '__main__':
    maze = [
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0],
    ]
    steps = bfs_shortest_path(maze, 0, 0, 3, 3)
    print(f"最短路徑長度: {steps}")
