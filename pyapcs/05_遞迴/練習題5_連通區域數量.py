"""
【APCS 遞迴練習題 5】連通區域數量（中級）

問題描述
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
給定一個 n × m 的二維地圖，地圖由 0 和 1 組成。
1 代表陸地，0 代表水域。陸地之間若上下左右相鄰則視為同一塊
連通區域（島嶼）。請計算地圖中有多少塊島嶼。

請使用遞迴 DFS 實作。

輸入格式
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
第一行：兩個正整數 n 和 m（1 ≤ n, m ≤ 100）
接下來 n 行：每行 m 個整數（0 或 1）

輸出格式
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
一個整數，表示島嶼數量

範例輸入
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5 5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
0 0 0 1 1

範例輸出
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
演算法說明
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DFS Flood Fill：
1. 遍歷每個格子，遇到未訪問的陸地 (1) 時：
   - 島嶼數量 +1
   - 從該格開始遞迴 DFS 四方向，標記所有相鄰陸地為已訪問
2. 遞迴 DFS：若超出邊界或是水域或已訪問則返回，
   否則標記已訪問並往四個方向繼續遞迴
時間複雜度 O(n × m)
"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    def dfs(r, c):
        if r < 0 or r >= n or c < 0 or c >= m:
            return
        if grid[r][c] == 0 or visited[r][c]:
            return
        visited[r][c] = True
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    islands = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                islands += 1
                dfs(i, j)

    print(islands)


if __name__ == '__main__':
    main()
