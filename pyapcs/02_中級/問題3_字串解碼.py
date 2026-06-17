"""
【APCS 中級】字串解碼
試題來源：程式實作 2022 年 6 月

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
問題描述
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
編碼函式 t = f(s, e)（s 為大寫英文字串，e 為 0/1 字串，長度均為 n）：

  步驟一：若 e 中 1 的個數為奇數，將 s 的前半段與後半段交換。
          （若 n 為奇數，正中間字元不動）

  步驟二：從 i=0 到 n-1，依 e[i] 決定 t[i]：
          e[i]=0 → 取出 s 目前第一個字元給 t[i]，並刪除 s 的第一個字元
          e[i]=1 → 取出 s 目前最後一個字元給 t[i]，並刪除 s 的最後一個字元

原始字串 s0 經 m 次編碼（使用編碼表 e0, e1, ..., e_{m-1}）得到最終字串 sm。

給定 sm 與編碼表，求原始字串 s0（解碼）。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
演算法說明（解碼 = 反向還原每一步）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
編碼過程：s0 → s1 → s2 → ... → sm
解碼過程：sm → s_{m-1} → ... → s0（反向使用編碼表）

對每一步「反向解碼」，即給定 t（已知）與 e，還原 s：

  反向步驟二：
    t[i] 是從 s 的前端（e[i]=0）或後端（e[i]=1）取出的。
    從 i = n-1 倒推到 i = 0，將 t[i] 放回 s 對應位置：
      e[i]=0 → t[i] 放回 deque 的左端（前端）
      e[i]=1 → t[i] 放回 deque 的右端（後端）
    還原後得到「步驟一之後的 s」。

  反向步驟一：
    步驟一是「若奇數個 1 則交換前後半段」，該操作自反（做兩次 = 還原），
    因此再做一次相同操作即可還原。

時間複雜度：O(m × n)
"""

import sys
from collections import deque
input = sys.stdin.readline


def decode_once(t_str, e_str):
    """
    給定編碼後的字串 t_str 與 0/1 鍵 e_str，還原出編碼前的字串 s。

    參數:
        t_str (str): 編碼後的字串（結果）
        e_str (str): 0/1 編碼鍵

    回傳:
        str: 編碼前的原始字串 s
    """
    n = len(e_str)
    t = list(t_str)   # 轉成列表方便索引

    # ── 反向步驟二：從 t 還原出「步驟一後的 s」 ──────────────
    # 正向編碼：e[i]=0 從 s 取 front；e[i]=1 從 s 取 back → 組成 t
    # 反向：從 i = n-1 到 0，將 t[i] 放回 deque 的對應端
    s_deque = deque()
    for i in range(n - 1, -1, -1):
        if e_str[i] == '0':
            s_deque.appendleft(t[i])   # 原本從 front 取出 → 放回 front
        else:
            s_deque.append(t[i])        # 原本從 back 取出 → 放回 back

    # s_deque 現在是步驟一之後、步驟二之前的 s
    s_list = list(s_deque)

    # ── 反向步驟一：若奇數個 1 則再次交換前後半段（自反操作）─
    ones_count = e_str.count('1')
    if ones_count % 2 == 1:
        # 交換前半段與後半段（中間字元若奇數長度則不動）
        half = n // 2
        # 前半段索引：[0, half)，後半段索引：[n-half, n)
        # 範例：n=5 → 前半[0,2), 中間[2], 後半[3,5)
        s_list = s_list[n - half:] + s_list[half: n - half] + s_list[:half]

    return ''.join(s_list)


def main():
    m, n = map(int, input().split())   # m 個 0/1 鍵，每個長度 n

    # 讀取 m 個 0/1 字串（編碼表 e0, e1, ..., e_{m-1}）
    keys = []
    for _ in range(m):
        keys.append(input().strip())

    # 讀取編碼後的訊息（最終字串 sm）
    encoded = input().strip()

    # ── 解碼：從 sm 倒推到 s0 ────────────────────────────────
    # 對編碼表「反向」逐步解碼
    # 編碼：s0 --e0--> s1 --e1--> s2 ... --e_{m-1}--> sm
    # 解碼：sm --e_{m-1} 反向--> s_{m-1} ... --e0 反向--> s0
    current = encoded
    for i in range(m - 1, -1, -1):    # 從最後一步倒推
        current = decode_once(current, keys[i])

    print(current)


if __name__ == '__main__':
    main()
