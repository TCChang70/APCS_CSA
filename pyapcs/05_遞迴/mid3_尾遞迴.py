"""
=============================================================================
【中階遞迴範例 3】尾遞迴（Tail Recursion）
=============================================================================

【教學目標】
理解尾遞迴的概念、與一般遞迴的差別、以及 Python 的限制。

【觀念說明】
尾遞迴定義：遞迴呼叫是函式中**最後一個動作**，且該呼叫的結果
**直接回傳**，不做任何額外運算。

一般遞迴 vs 尾遞迴：

  一般 factorial(5):
    factorial(5) = 5 * factorial(4)
                = 5 * (4 * factorial(3))
                = 5 * (4 * (3 * factorial(2)))
                = 5 * (4 * (3 * (2 * factorial(1))))
                = 5 * (4 * (3 * (2 * 1)))
                = 120
    回傳時需要逐層「回來」做乘法。

  尾遞迴 factorial(5, acc=1):
    tail_factorial(5, 1) = tail_factorial(4, 5)
                         = tail_factorial(3, 20)
                         = tail_factorial(2, 60)
                         = tail_factorial(1, 120)
                         = tail_factorial(0, 120)
                         = 120
    不需要回來做運算，直接到底。

尾遞迴的好處（在支援 TCO 的語言中）：
  - 不需要保留之前的 Stack Frame
  - 空間複雜度 O(1) 而不是 O(N)
  - 不會 Stack Overflow

Python 的**限制**：
  Python 設計者 Guido van Rossum 基於除錯考量，
  決定不實現尾遞迴優化（TCO, Tail Call Optimization）。
  因此在 Python 中，尾遞迴和一般遞迴的記憶體開銷**完全相同**。

=============================================================================
"""

import sys
sys.setrecursionlimit(10000)


def factorial_normal(n):
    """
    一般遞迴實作階乘。

    缺點：回傳時需要 n * factorial_normal(n-1)，
    所以每一層的 Stack Frame 都必須保留到子呼叫返回才能做乘法。

    追蹤 factorial_normal(5)：
      factorial_normal(5) → 5 * factorial_normal(4)
      factorial_normal(4) → 4 * factorial_normal(3)
      ...
      factorial_normal(1) → 1
      然後逐層回溯做乘法：1*2*3*4*5 = 120

    空間：O(N) — 同時有 N 個 Stack Frame
    """
    if n <= 1:               # 基底條件
        return 1
    return n * factorial_normal(n - 1)  # 不是尾遞迴：乘法在遞迴之後


def tail_factorial(n, acc=1):
    """
    尾遞迴實作階乘（使用累積器 acc）。

    acc 參數在每次遞迴時累積計算結果，
    因此回傳時不需要再做任何運算，直接回傳 acc 或遞迴結果。

    追蹤 tail_factorial(5, 1)：
      tail_factorial(5, 1)   → tail_factorial(4, 5)
      tail_factorial(4, 5)   → tail_factorial(3, 20)
      tail_factorial(3, 20)  → tail_factorial(2, 60)
      tail_factorial(2, 60)  → tail_factorial(1, 120)
      tail_factorial(1, 120) → tail_factorial(0, 120)
      tail_factorial(0, 120) → return 120  ← 直接到底

    注意：最後一個動作就是 tail_factorial(...)，
    且回傳值直接是該呼叫的結果。

    然而在 Python 中，這**仍然是 O(N) 空間**，
    因為 Python 不會幫你優化尾遞迴。
    """
    if n == 0:               # 基底條件
        return acc
    return tail_factorial(n - 1, n * acc)  # 尾遞迴：最後一個動作是呼叫自身


def tail_factorial_iter(n):
    """
    尾遞迴本質上等同於迭代（while 迴圈）。
    這是語言優化 TCO 後的結果。

    這段程式展示 tail_factorial 的「迭代等價版」：
    參數 n 和 acc 對應到 while 迴圈的變數。
    """
    acc = 1
    while n > 0:
        acc = n * acc    # 等同 tail_factorial(n-1, n*acc)
        n -= 1
    return acc            # 等同基底條件 return acc


"""
進一步比較：遞迴樹

一般遞迴 factorial(4)：
  factorial(4)
    ├── 4 * factorial(3)
    │     ├── 3 * factorial(2)
    │     │     ├── 2 * factorial(1)
    │     │     │     ├── 1 * factorial(0)
    │     │     │     │     └── return 1
    │     │     │     └── 1 * 1 = 1 ← 回溯
    │     │     └── 2 * 1 = 2 ← 回溯
    │     └── 3 * 2 = 6 ← 回溯
    └── 4 * 6 = 24 ← 回溯

尾遞迴 tail_factorial(4, 1)：
  tail_factorial(4, 1)
    └── tail_factorial(3, 4)
          └── tail_factorial(2, 12)
                └── tail_factorial(1, 24)
                      └── tail_factorial(0, 24)
                            └── return 24  ← 直接回傳，不回溯
"""

def sum_list_tail(lst, acc=0):
    """
    尾遞迴：列表元素求和。

    基底：列表為空 → 回傳 acc（已累積的總和）
    遞迴：sum_list_tail(lst[1:], acc + lst[0])
    最後一個動作就是呼叫自身。
    """
    if not lst:
        return acc
    return sum_list_tail(lst[1:], acc + lst[0])


def reverse_string_tail(s, acc=""):
    """
    尾遞迴：反轉字串。

    基底：原字串為空 → 回傳 acc（已反轉的結果）
    遞迴：每次將第一個字元移到 acc 的前面。
    追蹤 reverse_string_tail("abc", "")：
      → reverse_string_tail("bc", "a")
      → reverse_string_tail("c", "ba")
      → reverse_string_tail("", "cba")
      → return "cba"
    """
    if not s:
        return acc
    return reverse_string_tail(s[1:], s[0] + acc)


if __name__ == '__main__':
    print("一般遞迴 factorial(10):", factorial_normal(10))
    print("尾遞迴 tail_factorial(10):", tail_factorial(10))
    print("迭代版 tail_factorial_iter(10):", tail_factorial_iter(10))

    print("\n尾遞迴列表和:", sum_list_tail([1, 2, 3, 4, 5]))
    print("尾遞迴字串反轉:", reverse_string_tail("APCS"))
