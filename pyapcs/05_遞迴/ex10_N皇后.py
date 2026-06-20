"""
APCS 遞迴範例 10：N 皇后（Backtracking，中高級）

在 N×N 棋盤上放置 N 個皇后，使彼此不互相攻擊。
皇后可以攻擊同一行、同一列、同一對角線上的棋子。

遞迴策略：
逐列放置皇后，對每列嘗試所有可能的行位置，
若與已放置的皇后不衝突則繼續下一列。

APCS 高級題偶爾出現，也常見於：
- 數獨求解
- 著色問題
- 排列類的窮舉
"""


def solve_n_queens(n):
    ans = []
    cols = [0] * n

    def is_valid(row, col):
        for r in range(row):
            if (cols[r] == col or
                abs(cols[r] - col) == abs(r - row)):
                return False
        return True

    def backtrack(row):
        if row == n:
            ans.append([''.join('Q' if c == col else '.'
                                for col in range(n))
                         for c in cols])
            return
        for col in range(n):
            if is_valid(row, col):
                cols[row] = col
                backtrack(row + 1)

    backtrack(0)
    return ans


def total_n_queens(n):
    """只計算解法數量，不列印（APCS 節省時間的技巧）"""
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)

    def backtrack(row):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            d1 = row + col
            d2 = row - col + n - 1
            if not cols[col] and not diag1[d1] and not diag2[d2]:
                cols[col] = diag1[d1] = diag2[d2] = True
                count += backtrack(row + 1)
                cols[col] = diag1[d1] = diag2[d2] = False
        return count

    return backtrack(0)


if __name__ == '__main__':
    solutions = solve_n_queens(4)
    for sol in solutions:
        for row in sol:
            print(row)
        print()

    print(f"8 皇后共有 {total_n_queens(8)} 種解法")
