import sys

n = int(input())                  # 節點數
adj = [[] for _ in range(n + 1)]  # 鄰接表
for _ in range(n - 1):            # 樹的 n-1 條邊
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

print("adj =", adj)
visited = [False] * (n + 1)       # visited[u] = 節點 u 有沒有走訪過（先全部設 False）
order = []                        # 記錄走訪順序

def dfs(u):                       # 從節點 u 出發的深度優先搜尋
    visited[u] = True             # 1. 進入就先「標記來過」（不標記會無限迴圈）
    order.append(u)               #    記下走訪順序
    for v in adj[u]:              # 2. 依序看 u 的所有鄰居
        if not visited[v]:        # 3. 只有「沒去過」的鄰居才走
            dfs(v)                # 4. 遞迴深入那一層，一路走到底再回頭

dfs(1)                            # 從節點 1 出發
print(order)                      # 印出 DFS 走訪順序

# 7
# 1 2
# 1 3
# 2 4
# 2 5
# 3 6
# 3 7