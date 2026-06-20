"""
APCS DP 範例 1：爬樓梯與零錢問題（初級～中級）

爬樓梯：一次爬 1 階或 2 階，到第 n 階有幾種方法？
  dp[i] = dp[i-1] + dp[i-2]

零錢問題（Coin Change）：給定硬幣面額，湊出目標金額的最少硬幣數。
  dp[amt] = min(dp[amt - coin] + 1 for coin in coins)

兩者都是最基礎的 1D DP，狀態定義和轉移非常直覺。
"""


def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def coin_change(coins, amount):
    INF = 10 ** 9
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i >= c:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return dp[amount] if dp[amount] != INF else -1


if __name__ == '__main__':
    print(f"爬 10 階樓梯: {climb_stairs(10)} 種方法")
    print(f"湊 11 元（硬幣 1,2,5）: {coin_change([1, 2, 5], 11)} 個硬幣")
