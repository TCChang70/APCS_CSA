import sys
sys.setrecursionlimit(10**6)      # 調高遞迴深度上限

n = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(u, parent):        # 計算以 u 為根的子樹「高度」；parent = u 的上一層節點
    h = 0                  # 目前看到的最大子樹高度
    for v in adj[u]:       # 走過 u 的所有鄰居
        if v != parent:    # 只要 v 不是爸爸，就一定是 u 的「子節點」
            h = max(h, dfs(v, u) + 1)   # 子節點高度 +1，取最大的
    return h               # 回傳這棵子樹的高度

print(dfs(1, 0))           # 以節點 1 為根（0 當虛擬父節點）算整棵樹高度

# 5
# 1 2
# 1 3
# 2 4
# 2 5