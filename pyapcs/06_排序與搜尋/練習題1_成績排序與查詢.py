"""
【APCS 排序搜尋練習題 1】成績排序與排名查詢（初級）

問題描述
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
期中考結束，老師想將學生的成績從高到低排序，並提供排名查詢功能。

給定 N 個學生的學號和成績（N ≤ 1000），
先輸出依成績從高到低排序的結果（同分者學號較小在前），
再接受 Q 個查詢（Q ≤ 1000），每個查詢輸入一個學號，
輸出該學生的排名（1-based）和成績。

輸入格式
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
第一行：正整數 N
接下來 N 行：每行一個整數學號 id 和一個整數成績 score（0 ≤ score ≤ 100）
下一行：正整數 Q
接下來 Q 行：每行一個整數 id 表示查詢學號

輸出格式
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
先輸出 N 行排序結果，每行為「學號 成績」
再輸出 Q 行查詢結果，每行為「學號 排名 成績」
若查詢的學號不存在，輸出「學號 not found」

範例輸入
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5
101 88
102 92
103 88
104 75
105 92
3
102
103
999

範例輸出
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
102 92
105 92
101 88
103 88
104 75
102 1 92
103 3 88
999 not found

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
演算法說明
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. 讀入學生資料，依 (成績 DESC, 學號 ASC) 排序
2. 計算排名：同分者並列排名，佔用相同名次
3. 將結果存入 dict 方便查詢（學號 → (排名, 成績)）
4. 對每個查詢直接從 dict 取值，不存在則輸出 not found
時間複雜度 O(N log N + Q)
"""

import sys
input = sys.stdin.readline


def main():
    N = int(input())
    students = []
    for _ in range(N):
        sid, score = map(int, input().split())
        students.append((sid, score))

    students.sort(key=lambda x: (-x[1], x[0]))

    rank_info = {}
    rank = 1
    i = 0
    while i < N:
        j = i
        while j < N and students[j][1] == students[i][1]:
            j += 1
        same = j - i
        for k in range(i, j):
            sid, score = students[k]
            rank_info[sid] = (rank, score)
        rank += same
        i = j

    for sid, score in students:
        print(sid, score)

    Q = int(input())
    for _ in range(Q):
        qid = int(input())
        if qid in rank_info:
            r, s = rank_info[qid]
            print(qid, r, s)
        else:
            print(qid, "not found")


if __name__ == '__main__':
    main()
