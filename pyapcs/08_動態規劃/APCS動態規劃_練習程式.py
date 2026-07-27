"""
APCS 動態規劃練習程式（Dynamic Programming Practice）

使用方式：
1. 先閱讀同資料夾的 APCS動態規劃_練習說明.md
2. 執行本檔案觀察範例輸出
3. 嘗試改寫每題函式（例如自己先註解掉答案重寫）

題目難度標示：
  ★      初級（APCS 40 分題可見）
  ★★     中級（APCS 40~50 分題常見）
  ★★★   中高級（APCS 55~70 分挑戰）
"""

from bisect import bisect_left


# ============================================================
#  ★ 初級 1D DP
# ============================================================

def p1_climb_stairs(n: int) -> int:
    """題 1：爬樓梯（Climbing Stairs）★
    一次可走 1 或 2 階，求到第 n 階的方法數。

    狀態：dp[i] = 到第 i 階的方法數
    轉移：dp[i] = dp[i-1] + dp[i-2]
    初始：dp[1]=1, dp[2]=2
    複雜度：時間 O(N)，空間 O(1)（僅保留前兩項）
    """
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def p1b_climb_stairs_k(n: int, k: int) -> int:
    """題 1b：爬樓梯進階（一次走 1~k 階）★
    轉移：dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-k]

    時間 O(N*K)，空間 O(K)（用環形陣列）
    """
    if n == 0:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i] += dp[i - j]
    return dp[n]


def p2_coin_change_min(coins: list[int], amount: int) -> int:
    """題 2：最少硬幣數（Coin Change, Min Coins）★
    回傳湊出 amount 的最少硬幣數，無法湊出回傳 -1。

    狀態：dp[x] = 湊出金額 x 所需的最少硬幣數
    轉移：dp[x] = min(dp[x - c] + 1) for c in coins
    初始：dp[0]=0，其餘 INF
    複雜度：時間 O(amount * len(coins))，空間 O(amount)
    """
    inf = 10**9
    dp = [inf] * (amount + 1)
    dp[0] = 0

    for cur in range(1, amount + 1):
        for c in coins:
            if cur >= c:
                dp[cur] = min(dp[cur], dp[cur - c] + 1)

    return -1 if dp[amount] == inf else dp[amount]


def p2b_coin_change_ways(coins: list[int], amount: int) -> int:
    """題 2b：零錢組合數（Coin Change II）★
    求湊出 amount 的組合數（順序不同算同一種）。

    狀態：dp[x] = 湊出 x 的方法數
    轉移：dp[x] += dp[x - c]
    注意：迴圈順序必須是「先物品、後金額」，才不會重複計入排列
    """
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for x in range(c, amount + 1):
            dp[x] += dp[x - c]
    return dp[amount]


# ============================================================
#  ★★ 中級 DP
# ============================================================

def p3_kadane(nums: list[int]) -> int:
    """題 3：最大連續子陣列和（Maximum Subarray, Kadane）★★
    找連續子陣列的最大總和。

    狀態：dp[i] = 以 i 結尾的最大和
    轉移：dp[i] = max(nums[i], dp[i-1] + nums[i])
    時間 O(N)，空間 O(1)
    """
    best_end_here = nums[0]
    best_overall = nums[0]

    for x in nums[1:]:
        best_end_here = max(x, best_end_here + x)
        best_overall = max(best_overall, best_end_here)

    return best_overall


def p3b_kadane_with_indices(nums: list[int]) -> tuple[int, int, int]:
    """題 3b：Kadane 同時回傳起訖索引 ★★
    回傳 (最大和, 起始索引, 結束索引)
    """
    best_end_here = nums[0]
    best_overall = nums[0]
    start = temp_start = 0
    end = 0

    for i in range(1, len(nums)):
        if nums[i] > best_end_here + nums[i]:
            best_end_here = nums[i]
            temp_start = i
        else:
            best_end_here += nums[i]

        if best_end_here > best_overall:
            best_overall = best_end_here
            start = temp_start
            end = i

    return best_overall, start, end


def p4_knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    """題 4：0/1 背包（0/1 Knapsack）★★
    每個物品最多只能選一次。

    狀態：dp[w] = 容量 w 時的最大價值
    轉移：dp[w] = max(dp[w], dp[w-weights[i]] + values[i])
    關鍵：必須從大到小更新 w，避免同一物品被重複選取
    時間 O(N*W)，空間 O(W)
    """
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]


def p4b_knapsack_unbounded(weights: list[int], values: list[int],
                            capacity: int) -> int:
    """題 4b：無限背包（Unbounded Knapsack）★★
    每個物品可選無限次。差別：正序更新 w。

    時間 O(N*W)，空間 O(W)
    """
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        for w in range(weights[i], capacity + 1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]


def p5_lis_nlogn(nums: list[int]) -> int:
    """題 5：最長遞增子序列長度（LIS）★★
    O(N log N) 作法：tails + binary search。

    tails[k] = 長度 k+1 的遞增子序列中，最小結尾值
    時間 O(N log N)，空間 O(N)
    """
    tails: list[int] = []

    for x in nums:
        pos = bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x

    return len(tails)


def p5_lis_dp(nums: list[int]) -> int:
    """題 5b：LIS 的 O(N^2) DP 寫法（供比較）"""
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def p6_lcs_length(a: str, b: str) -> int:
    """題 6：最長共同子序列長度（LCS Length）★★
    空間壓縮到 O(min(N, M))。

    狀態：dp[j] = 目前列中 A[:i] 與 B[:j] 的 LCS 長度
    轉移：
      若 A[i-1]==B[j-1]：dp[j] = prev_diag + 1
      否則：dp[j] = max(dp[j], dp[j-1])
    關鍵：用 prev_diag 保存左上角舊值
    """
    if len(a) < len(b):
        short_s, long_s = a, b
    else:
        short_s, long_s = b, a

    dp = [0] * (len(short_s) + 1)

    for ch in long_s:
        prev_diag = 0
        for j in range(1, len(short_s) + 1):
            old = dp[j]
            if ch == short_s[j - 1]:
                dp[j] = prev_diag + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            prev_diag = old

    return dp[-1]


def p6b_lcs_string(a: str, b: str) -> str:
    """題 6b：回傳 LCS 字串本身（需 2D 表追溯路徑）"""
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = n, m
    result = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            result.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(result))


# ============================================================
#  ★★★ 中高級 DP
# ============================================================

def p7_edit_distance(word1: str, word2: str) -> int:
    """題 7：編輯距離（Edit Distance）★★★
    將 word1 轉換成 word2 的最少操作數（插入/刪除/替換）。

    狀態：dp[i][j] = word1[:i] 轉為 word2[:j] 的最少步數
    轉移：
      若 word1[i-1] == word2[j-1]：dp[i][j] = dp[i-1][j-1]（無需操作）
      否則：dp[i][j] = 1 + min(
          dp[i-1][j],      # 刪除 word1[i-1]
          dp[i][j-1],      # 插入 word2[j-1]
          dp[i-1][j-1]     # 替換 word1[i-1] 為 word2[j-1]
      )
    初始化：dp[i][0] = i, dp[0][j] = j

    時間 O(N*M)，空間壓縮至 O(min(N,M))
    """
    n, m = len(word1), len(word2)

    if n < m:
        word1, word2 = word2, word1
        n, m = m, n

    dp = list(range(m + 1))

    for i in range(1, n + 1):
        prev_diag = dp[0]
        dp[0] = i
        for j in range(1, m + 1):
            temp = dp[j]
            if word1[i - 1] == word2[j - 1]:
                dp[j] = prev_diag
            else:
                dp[j] = 1 + min(dp[j], dp[j - 1], prev_diag)
            prev_diag = temp

    return dp[m]


def p8_partition_equal_subset(nums: list[int]) -> bool:
    """題 8a：分割等和子集（Partition Equal Subset Sum）★★★
    判斷能否將 nums 分成兩個總和相等的子集。

    本質：子集和問題（subset sum）
    狀態：dp[s] = 能否湊出總和 s
    轉移：dp[s] = dp[s] or dp[s - num]
    初始：dp[0] = True

    時間 O(N * sum/2)，空間 O(sum/2)
    """
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]

    return dp[target]


def p8b_partition_diff_min(nums: list[int]) -> int:
    """題 8b：分割兩子集最小差 ★★★
    將 nums 分成兩組，使兩組和的差最小，回傳最小差。

    只需判斷哪些元素放入第一組（總和接近 total/2）
    """
    total = sum(nums)
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]

    for s in range(target, -1, -1):
        if dp[s]:
            return total - 2 * s
    return total


# ============================================================
#  Demo 主程式
# ============================================================

def _demo() -> None:
    print("=" * 55)
    print("  APCS 動態規劃練習程式 Demo")
    print("=" * 55)

    print("\n--- ★ 初級 1D DP ---")

    print("\n[題 1] 爬樓梯")
    print(f"  n=10  -> {p1_climb_stairs(10)}")          # 89

    print("\n[題 1b] 爬樓梯（1~k 階）")
    print(f"  n=5, k=3 -> {p1b_climb_stairs_k(5, 3)}")  # 13

    print("\n[題 2] 最少硬幣數")
    print(f"  coins=[1,2,5], amount=11 -> {p2_coin_change_min([1, 2, 5], 11)}")  # 3

    print("\n[題 2b] 零錢組合數")
    print(f"  coins=[1,2,5], amount=5  -> {p2b_coin_change_ways([1, 2, 5], 5)}")  # 4

    print("\n--- ★★ 中級 DP ---")

    print("\n[題 3] Kadane 最大子陣列和")
    arr3 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"  {arr3}")
    print(f"  最大和 -> {p3_kadane(arr3)}")  # 6
    val, s, e = p3b_kadane_with_indices(arr3)
    print(f"  帶索引 -> 和={val}, 子陣列={arr3[s:e+1]}")

    print("\n[題 4] 0/1 背包")
    w = [2, 3, 4, 5]
    v = [3, 4, 5, 6]
    print(f"  weights={w}, values={v}, capacity=5")
    print(f"  0/1 背包     -> {p4_knapsack_01(w, v, 5)}")           # 7
    print(f"  無限背包     -> {p4b_knapsack_unbounded(w, v, 5)}")    # 7

    print("\n[題 5] 最長遞增子序列 LIS")
    arr5 = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"  {arr5}")
    print(f"  O(N^2) DP -> {p5_lis_dp(arr5)}")      # 4
    print(f"  O(NlogN)  -> {p5_lis_nlogn(arr5)}")   # 4

    print("\n[題 6] 最長共同子序列 LCS")
    a, b = "ABCBDAB", "BDCAB"
    print(f"  A='{a}', B='{b}'")
    print(f"  LCS 長度  -> {p6_lcs_length(a, b)}")  # 4
    print(f"  LCS 字串  -> {p6b_lcs_string(a, b)}")  # BCAB

    print("\n--- ★★★ 中高級 DP ---")

    print("\n[題 7] 編輯距離")
    w1, w2 = "horse", "ros"
    print(f"  '{w1}' -> '{w2}' : {p7_edit_distance(w1, w2)} 步")  # 3
    w1, w2 = "intention", "execution"
    print(f"  '{w1}' -> '{w2}' : {p7_edit_distance(w1, w2)} 步")  # 5

    print("\n[題 8a] 分割等和子集")
    print(f"  [1,5,11,5] -> {p8_partition_equal_subset([1, 5, 11, 5])}")  # True
    print(f"  [1,2,3,5]  -> {p8_partition_equal_subset([1, 2, 3, 5])}")   # False

    print("\n[題 8b] 分割兩子集最小差")
    print(f"  [1,6,11,5] -> {p8b_partition_diff_min([1, 6, 11, 5])}")  # 1

    print("\n" + "=" * 55)


if __name__ == "__main__":
    _demo()
