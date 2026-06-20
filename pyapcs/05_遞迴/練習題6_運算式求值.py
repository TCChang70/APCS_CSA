"""
【APCS 遞迴練習題 6】簡易運算式求值（中級）

問題描述
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
給定一個僅包含數字 0~9、加號 +、減號 -、乘號 * 的合法運算式
（不含括號、不含空格），數字皆為個位數，請使用遞迴下降解析
（Recursive Descent）計算其結果。

運算子優先順序：* 高於 + 和 -（先乘除後加減）。
所有運算皆為整數運算。

輸入格式
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
第一行：一個正整數 N，表示有 N 個運算式
接下來 N 行：每行一個字串 s，長度不超過 100

輸出格式
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
對每個運算式輸出一行整數結果

範例輸入
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3
1+2*3
2*3+4*5
5-3*2+8/4

範例輸出
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7
26
7

說明：
1+2*3 = 1+6 = 7
2*3+4*5 = 6+20 = 26

注意：本題除法為整數除法（無條件捨去），但題目範例 8/4=2，
若有除號請比照乘法優先順序。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
演算法說明
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
遞迴下降解析（Recursive Descent Parsing）：
運算式語法（BNF）：
  expr   → term { ('+'|'-') term }
  term   → factor { ('*'|'/') factor }
  factor → 數字

- expr() 解析加減法，內部呼叫 term() 取得左右運算元
- term() 解析乘除法，內部呼叫 factor() 取得左右運算元
- factor() 解析數字
時間複雜度 O(len(s))
"""

import sys
input = sys.stdin.readline


class Parser:
    def __init__(self, s):
        self.s = s
        self.pos = 0

    def peek(self):
        return self.s[self.pos] if self.pos < len(self.s) else ''

    def consume(self):
        ch = self.s[self.pos]
        self.pos += 1
        return ch

    def parse_expr(self):
        result = self.parse_term()
        while self.peek() in '+-':
            op = self.consume()
            right = self.parse_term()
            if op == '+':
                result += right
            else:
                result -= right
        return result

    def parse_term(self):
        result = self.parse_factor()
        while self.peek() in '*/':
            op = self.consume()
            right = self.parse_factor()
            if op == '*':
                result *= right
            else:
                result //= right
        return result

    def parse_factor(self):
        return int(self.consume())


def main():
    N = int(input())
    for _ in range(N):
        s = input().strip()
        parser = Parser(s)
        print(parser.parse_expr())


if __name__ == '__main__':
    main()
