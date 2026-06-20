"""
APCS 遞迴範例 9：記憶化費氏數列（DP + 記憶化，中級）

樸素費氏遞迴的缺點：重複計算 → 指數爆炸 O(2ⁿ)
解決方案：用 memo 記住算過的結果，將 O(2ⁿ) 降為 O(N)

這也是動態規劃（Dynamic Programming）的 top-down 形式。
APCS 高級題常需要將遞迴 + 記憶化做為優化手段。
"""

from functools import lru_cache


def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


@lru_cache(maxsize=None)
def fibonacci_lru(n):
    """使用 Python 內建的 lru_cache 裝飾器"""
    if n <= 1:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


def fibonacci_iter(n):
    """迭代版（面試常問的非遞迴實作）"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    import time

    for fn in [fibonacci_memo, fibonacci_lru, fibonacci_iter]:
        start = time.time()
        result = fn(100)
        elapsed = time.time() - start
        print(f"{fn.__name__}(100) = {result} ({elapsed:.4f}s)")
