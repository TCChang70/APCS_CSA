"""
APCS 遞迴範例 5：迷宮 DFS（中級）

給定 n×m 地圖，0 可通行、1 障礙物。
計算從起點 (sr, sc) 到終點 (er, ec) 是否有路徑。
使用遞迴 DFS 四方向探索。

APCS 常見變化：
- 連通區塊數量（島嶼數量）
- 最短路徑長度（BFS 更適合）
- 特定形狀的區域計算
"""


def has_path(grid, sr, sc, er, ec):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if grid[r][c] == 1 or visited[r][c]:
            return False
        if r == er and c == ec:
            return True
        visited[r][c] = True
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if dfs(r + dr, c + dc):
                return True
        return False

    return dfs(sr, sc)


def count_islands(grid):
    """計算地圖中有多少個獨立的島嶼（連通 1 的區域）"""
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] == 0 or visited[r][c]:
            return
        visited[r][c] = True
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dfs(r + dr, c + dc)

    ans = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                ans += 1
                dfs(i, j)
    return ans


if __name__ == '__main__':
    maze = [
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0],
    ]
    print(has_path(maze, 0, 0, 3, 3))

    grid = [
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 1],
    ]
    print(count_islands(grid))
