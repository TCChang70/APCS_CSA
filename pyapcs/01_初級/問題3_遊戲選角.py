"""
【APCS 初級】遊戲選角
試題來源：程式實作 2024 年 10 月（推測）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
問題描述
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
共 n 名角色，每名角色有「攻擊力 atk」與「防禦力 def」。
綜合能力 = atk² + def²
找出「綜合能力第二高」的角色，輸出其攻擊力與防禦力。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
演算法說明
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. 讀入所有角色，計算各自的綜合能力分數。
2. 以綜合能力「降序」排序。
3. 取排序後第二個角色（索引 1）的攻防數值輸出。

題目保證所有角色的綜合能力皆相異，故不需處理平手情況。
時間複雜度：O(n log n)
"""

import sys
input = sys.stdin.readline


def main():
    n = int(input())   # 角色總數 (3 ≤ n ≤ 20)

    characters = []
    for _ in range(n):
        atk, defense = map(int, input().split())
        # 計算綜合能力（攻擊力平方 + 防禦力平方）
        score = atk ** 2 + defense ** 2
        # 將 (分數, 攻擊力, 防禦力) 存入列表
        characters.append((score, atk, defense))

    # 依綜合能力「從大到小」排序
    # sorted() 預設升序，reverse=True 改為降序
    characters.sort(key=lambda x: x[0], reverse=True)

    # 取第二高（索引 1）
    _, atk2, def2 = characters[1]
    print(atk2, def2)


if __name__ == '__main__':
    main()
