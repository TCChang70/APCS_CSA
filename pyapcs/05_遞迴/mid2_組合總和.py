"""
=============================================================================
【中階遞迴範例 2】組合總和（Backtracking 剪枝）
=============================================================================

【教學目標】
理解 Backtracking 剪枝策略，避免無效搜尋。

【觀念說明】
剪枝（Pruning）：在遞迴窮舉時，
若當前路徑**不可能**導向合法解，就直接放棄該分支。

常見剪枝策略：
1. 超過目標值 → 停止往後加（所有數字為正數）
2. 總和已等於目標 → 記錄答案，不再繼續
3. 跳過重複數字 → 避免產生相同組合
4. 預先排序 → 超過目標時可提前 break

=====================================================================
題目：組合總和
給定一群正整數 candidates（可能有重複）和目標值 target，
找出所有總和等於 target 的組合。
每個數字只能用一次，組合不能重複。

例如：candidates=[10,1,2,7,6,1,5], target=8
答案：[[1,1,6], [1,2,5], [1,7], [2,6]]

剪枝策略：
  先排序 [1,1,2,5,6,7,10]
  - 總和一旦 > 8，後面更大的數字不用再試（因為已排序）
  - 同一層跳過重複數字（避免 [1,2,5] 出現兩次）
=====================================================================
"""

import sys
input = sys.stdin.readline


def combination_sum(candidates, target):
    """
    找出 candidates 中所有總和等於 target 的組合（不重複，每個數用一次）。

    參數：
      candidates: list[int]，正整數列表
      target: int，目標總和

    回傳：
      list[list[int]]，所有符合條件的組合

    Backtracking 流程（以 candidates=[1,2,3], target=4 為例）：
      sort: [1,2,3]
      backtrack(start=0, path=[], cur=0):
        i=0 → path=[1], cur=1 → backtrack(1, [1], 1):
          i=1 → path=[1,2], cur=3 → backtrack(2, [1,2], 3):
            i=2 → path=[1,2,3], cur=6>4 → 剪枝 return
          i=2 → path=[1,3], cur=4==target → 記錄 [1,3], return
        i=1 → path=[2], cur=2 → backtrack(2, [2], 2):
          i=2 → path=[2,3], cur=5>4 → 剪枝 return
        i=2 → path=[3], cur=3 → backtrack(3, [3], 3):
          無後續元素 → return
      最終答案：[[1,3]]
    """
    candidates.sort()                     # 排序：確保剪枝正確
    ans = []

    def backtrack(start, path, cur_sum):
        """
        start: 從哪個索引開始選（避免回頭 → 避免重複排列）
        path:   當前已選的數字列表
        cur_sum: 當前總和
        """
        if cur_sum == target:             # 基底條件 1：找到一組解
            ans.append(path[:])           #   path[:] 複製一份，避免後續修改影響
            return
        if cur_sum > target:              # 剪枝 1：超過目標，不再繼續
            return
        for i in range(start, len(candidates)):
            # ── 剪枝 2：跳過同一層的重複數字 ──────────────────
            # 若 candidates[i] == candidates[i-1] 且 i > start，
            # 代表在同一層已經處理過相同的值，跳過避免重複組合
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            # ── 剪枝 3：最小的數字都已太大，後面更大更不用試 ──
            if cur_sum + candidates[i] > target:
                break

            path.append(candidates[i])    # 選擇當前數字
            backtrack(i + 1, path, cur_sum + candidates[i])  # 遞迴（i+1 不重複選）
            path.pop()                    # 回溯：取消選擇

    backtrack(0, [], 0)
    return ans


def main():
    """讀取輸入並輸出結果"""
    target = int(input())                  # 目標總和
    candidates = list(map(int, input().split()))  # 可選數字列表
    result = combination_sum(candidates, target)
    for combo in result:
        print(' '.join(map(str, combo)))


if __name__ == '__main__':
    main()
