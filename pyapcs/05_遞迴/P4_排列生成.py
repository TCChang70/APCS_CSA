"""
=============================================================================
P4. 排列生成（中級）— 完整程式說明
=============================================================================

【問題回顧】
給定 N 個相異正整數，用 Backtracking 輸出所有排列（字典序）。

【解題思維】
Backtracking 是遞迴窮舉的經典技巧：
  - 每次選擇一個「尚未使用」的數字加入排列
  - 標記該數字為已使用
  - 遞迴到下一層繼續選擇
  - 回來時取消標記（回溯），嘗試其他數字

這形成一棵遞迴樹，葉節點就是一個完整排列。

為了確保字典序，先將輸入數字排序，再依序嘗試。

=============================================================================
程式碼逐段說明
=============================================================================
"""

import sys
input = sys.stdin.readline


def main():
    """
    main() 流程：
    1. 讀取 N 和數字列表
    2. 排序（確保字典序輸出）
    3. 建立 used 標記陣列和 path 暫存路徑
    4. 呼叫 backtrack() 開始遞迴窮舉
    """
    N = int(input())                      # 讀取 N
    nums = list(map(int, input().split())) # 讀取 N 個數字
    nums.sort()                           # 排序：保證字典序輸出

    used = [False] * N                    # used[i] = True 表示第 i 個數字已用
    path = []                             # 暫存當前正在建構的排列


    def backtrack():
        """
        遞迴 Backtracking 生成所有排列。

        每層的任務：
        1. 檢查是否已選滿 N 個（基底條件）
        2. 依序嘗試每個數字：
           a. 若未使用 → 選中它
           b. 標記 used[i] = True，加入 path
           c. 遞迴到下一層
           d. 回溯：取消標記，從 path 移除（恢復原狀）

        範例追蹤（N=3, nums=[1,2,3]）：
          backtrack():
            i=0 → used[0]=T path=[1] → backtrack():
              i=0 skip(used)  i=1 → used[1]=T path=[1,2] → backtrack():
                i=0,1 skip  i=2 → used[2]=T path=[1,2,3] → print → return
                ← used[2]=F path=[1,2]
              ← used[1]=F path=[1]
              i=2 → used[2]=T path=[1,3] → backtrack():
                i=0→used[0]=T path=[1,3,2] → print → return
              ...
        """
        if len(path) == N:                # 基底條件：已選滿 N 個
            print(' '.join(map(str, path))) # 輸出一個完整排列
            return

        for i in range(N):                # 嘗試每個位置
            if not used[i]:               # 若第 i 個數字尚未使用
                used[i] = True            # 選擇它
                path.append(nums[i])      # 加入路徑
                backtrack()               # 遞迴下一層
                path.pop()                # 回溯：移除最後加入的數字
                used[i] = False            # 回溯：取消標記


    backtrack()                           # 從空路徑開始


if __name__ == '__main__':
    main()
"""
=============================================================================
時間複雜度：O(N × N!)
  有 N! 個排列，每個排列需要 O(N) 時間建構和輸出。
  N ≤ 8 時最大 8! = 40320，在合理範圍內。

空間複雜度：O(N)
  used 陣列 O(N) + path 陣列 O(N) + 遞迴深度 O(N)

Backtracking 模板（牢記！）：
  def backtrack():
      if 滿足條件:
          輸出答案
          return
      for 每個選擇:
          if 選擇合法:
              做選擇（標記）
              backtrack()      ← 遞迴
              撤銷選擇（取消標記）

APCS 考點：
  1. Backtracking 標準模板是 APCS 中級必考
  2. used 陣列管理狀態
  3. 先排序確保字典序輸出
  4. path.pop() 和 used[i]=False 的「回溯」是關鍵
=============================================================================
"""
