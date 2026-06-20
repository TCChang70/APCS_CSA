"""
APCS DP 範例 3：0/1 背包問題（中級）

給定 N 個物品，每個物品有重量 w[i] 和價值 v[i]。
背包容量 W，每個物品最多選一次，求最大總價值。

狀態：dp[i][w] = 前 i 個物品中選出總重 ≤ w 的最大價值
轉移：dp[i][w] = max(dp[i-1][w], dp[i-1][w-w[i]] + v[i])

空間壓縮：用一維陣列從後往前更新。
"""


def knapsack(weights, values, W):
    N = len(weights)
    dp = [0] * (W + 1)
    for i in range(N):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[W]


def knapsack_unbounded(weights, values, W):
    """無限背包（每種物品可取無限次）"""
    dp = [0] * (W + 1)
    for w in range(1, W + 1):
        for i in range(len(weights)):
            if w >= weights[i]:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[W]


if __name__ == '__main__':
    w = [2, 3, 4, 5]
    v = [3, 4, 5, 6]
    print(f"0/1 背包容量 5: {knapsack(w, v, 5)}")
    print(f"無限背包容量 5: {knapsack_unbounded(w, v, 5)}")
