"""
【APCS 初級】七言對聯
試題來源：程式實作 2021 年 9 月

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
問題描述
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
每首七言對聯有兩句，每句7個字，每字為 0(平聲) 或 1(仄聲)。
檢查三條平仄規則：

  A. 二四不同二六同：
       每句第2字與第4字平仄必須「不同」；
       每句第2字與第6字平仄必須「相同」。
       （索引從0開始：位置 1、3、5）

  B. 仄起平收：
       第一句第7字（索引6）必須是仄聲 1；
       第二句第7字（索引6）必須是平聲 0。

  C. 同聯相對：
       第一句的第2、4、6字，分別與第二句的第2、4、6字平仄相反。

輸出違反的規則字母（依 A→B→C 順序），若全部符合則輸出 None。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
演算法說明
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
直接根據規則逐條判斷，時間複雜度 O(n)。
"""

import sys
input = sys.stdin.readline


def check_couplet(line1, line2):
    """
    檢查一首七言對聯是否符合三條平仄規則。

    參數:
        line1 (list[int]): 第一句的7個平仄值 (0=平, 1=仄)
        line2 (list[int]): 第二句的7個平仄值

    回傳:
        str: 違反的規則字母組合，例如 "AC"；全符合則回傳 "None"
    """
    violations = []

    # ── 規則 A：二四不同二六同 ──────────────────────────────
    # 對「每一句」分別檢查（任一句違反即算 A 規則不符）
    # 索引：第2字=1, 第4字=3, 第6字=5（題目是從1開始計數）
    rule_a = False
    for line in [line1, line2]:
        if line[1] == line[3]:   # 第2與第4字應「不同」，若相同則違反
            rule_a = True
        if line[1] != line[5]:   # 第2與第6字應「相同」，若不同則違反
            rule_a = True
    if rule_a:
        violations.append('A')

    # ── 規則 B：仄起平收 ────────────────────────────────────
    # 第一句末字(索引6)須為仄(1)，第二句末字須為平(0)
    rule_b = False
    if line1[6] != 1:   # 第一句末字應為仄聲
        rule_b = True
    if line2[6] != 0:   # 第二句末字應為平聲
        rule_b = True
    if rule_b:
        violations.append('B')

    # ── 規則 C：同聯相對 ────────────────────────────────────
    # 兩句的第2、4、6字（索引1,3,5）平仄應各自相反（即 XOR = 1）
    rule_c = False
    for idx in [1, 3, 5]:
        if line1[idx] == line2[idx]:   # 相同代表沒有相反，違反規則 C
            rule_c = True
    if rule_c:
        violations.append('C')

    return ''.join(violations) if violations else 'None'


def main():
    n = int(input())         # 共 n 首七言對聯
    for _ in range(n):
        # 每次讀取兩句，各為7個整數（0或1）
        line1 = list(map(int, input().split()))
        line2 = list(map(int, input().split()))
        print(check_couplet(line1, line2))


if __name__ == '__main__':
    main()
