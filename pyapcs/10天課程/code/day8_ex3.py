n = int(input())                          # 節點數量（編號 1~n）
adj = [[] for _ in range(n + 1)]          # 長度 n+1：adj[u] 放「所有跟 u 相鄰的節點」
                                          # 多開一格是為了讓 adj[1] 對應到編號 1 的節點
for _ in range(n - 1):                    # 樹的定義：n 個點、恰好 n-1 條邊
    u, v = map(int, input().split())      # 讀一條邊：u 和 v 相鄰
    adj[u].append(v)                      # u 的鄰居清單加入 v
    adj[v].append(u)                      # 無向圖：v 的鄰居清單也要加入 u（兩邊都記）

for i in range(1, n + 1):                 # 依序印出每個節點的鄰居，檢查讀入結果
    print(i, adj[i])

print(adj)

# 5
# 1 2
# 1 3
# 2 4
# 2 5