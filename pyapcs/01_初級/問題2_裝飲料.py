"""
【APCS 初級】裝飲料
試題來源：程式實作 2024 年 10 月

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
問題描述
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
造型杯由「下方長方體」＋「上方長方體」組成：
  下方：底面 w1×w1 cm²，高 h1 cm
  上方：底面 w2×w2 cm²，高 h2 cm（w1 < w2）

依序倒入 N 杯冰水，計算每次水位上升的高度，輸出最大值。
杯子裝滿後高度不再上升（上升值為 0）。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
演算法說明
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. 計算下方容量 = w1² × h1，上方容量 = w2² × h2，總容量 = 兩者之和。
2. 用輔助函式 volume_to_height(vol) 將體積轉換為水位高度：
     - 若 vol ≤ 下方容量：高度 = vol ÷ (w1²)
     - 否則：高度 = h1 + (vol − 下方容量) ÷ (w2²)
3. 逐杯加水，追蹤累積體積（不超過總容量）；
   計算每次 新高度 − 舊高度 = 本次上升量，取最大值。

時間複雜度：O(N)
"""

import sys
input = sys.stdin.readline


def solve():
    # 讀取此測試資料
    N = int(input())                          # 購買冰水杯數
    w1, w2, h1, h2 = map(int, input().split())  # 杯子規格
    volumes = list(map(int, input().split()))   # N 杯冰水體積

    # ── 計算杯子各區容量 ────────────────────────────────────
    lower_cap = w1 * w1 * h1   # 下方長方體最大容積 (cm³ = ml)
    upper_cap = w2 * w2 * h2   # 上方長方體最大容積
    total_cap = lower_cap + upper_cap  # 總容量

    def volume_to_height(vol):
        """
        將杯中累積體積 vol 轉換成水位高度。

        下方區填滿前：高度 = vol / (w1²)
        下方區填滿後：高度 = h1 + (超出量) / (w2²)
        題目保證每次高度均為整數，故用整數除法。
        """
        if vol <= lower_cap:
            return vol // (w1 * w1)          # 水仍在下方區
        else:
            extra = vol - lower_cap          # 超出下方區的體積
            return h1 + extra // (w2 * w2)  # 下方滿高 + 上方高度

    # ── 逐杯倒水，記錄最大上升量 ────────────────────────────
    current_vol = 0   # 目前杯中水的總體積（從 0 開始）
    max_rise = 0      # 答案：最大水位上升高度

    for v in volumes:
        old_height = volume_to_height(current_vol)
        # 加水後體積不可超過總容量（杯滿則截斷）
        current_vol = min(current_vol + v, total_cap)
        new_height = volume_to_height(current_vol)
        rise = new_height - old_height       # 本次上升量
        max_rise = max(max_rise, rise)

    print(max_rise)


# ── 主程式：APCS 題目可能包含多筆測試資料 ───────────────────
import sys
data = sys.stdin.read().split()
ptr = 0

while ptr < len(data):
    N = int(data[ptr]); ptr += 1
    w1, w2, h1, h2 = int(data[ptr]), int(data[ptr+1]), int(data[ptr+2]), int(data[ptr+3])
    ptr += 4
    volumes = [int(data[ptr + i]) for i in range(N)]
    ptr += N

    # ── 計算杯子各區容量 ────────────────────────────────────
    lower_cap = w1 * w1 * h1
    upper_cap = w2 * w2 * h2
    total_cap = lower_cap + upper_cap

    def volume_to_height(vol, lower_cap=lower_cap, upper_cap=upper_cap,
                         w1=w1, w2=w2, h1=h1):
        if vol <= lower_cap:
            return vol // (w1 * w1)
        else:
            extra = vol - lower_cap
            return h1 + extra // (w2 * w2)

    current_vol = 0
    max_rise = 0

    for v in volumes:
        old_h = volume_to_height(current_vol)
        current_vol = min(current_vol + v, total_cap)
        new_h = volume_to_height(current_vol)
        rise = new_h - old_h
        if rise > max_rise:
            max_rise = rise

    print(max_rise)
