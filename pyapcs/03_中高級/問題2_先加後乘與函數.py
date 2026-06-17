"""
【APCS 中高級】先加後乘與函數
試題來源：程式實作 2023 年 1 月

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
問題描述
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
計算式由非負整數、+、* 與特殊函式 f 組成。

規則：
  1. 「先加後乘」：加法（+）的優先順序高於乘法（*）
     例：1+2*3 = (1+2)*3 = 9
         2+3*1+2+1 = (2+3)*(1+2+1) = 20

  2. f 函式：從一個或多個參數中，取「最大值 − 最小值」
     例：f(5,12,7,4) = 12−4 = 8
         f(6) = 6−6 = 0

  3. f 的參數本身也可以是算式（含巢狀 f）

括號只出現在 f 函式中，不用於改變運算優先順序。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
演算法說明（遞迴下降解析器）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
定義文法（EBNF）：

  expr    ::= term ('*' term)*        ← 乘法是最外層（低優先）
  term    ::= atom ('+' atom)*        ← 加法是內層（高優先）
  atom    ::= NUMBER | 'f' '(' args ')'
  args    ::= expr (',' expr)*

實作使用「位置指標 pos」在字串上移動，依文法規則逐步解析。

運算中間值可能超過 2^31，Python 的大整數自動處理。
"""

import sys
input = sys.stdin.readline


class Parser:
    """
    遞迴下降解析器，解析「先加後乘 + f函式」的算式。
    """

    def __init__(self, s: str):
        self.s = s          # 輸入算式字串
        self.pos = 0        # 目前解析位置（字元索引）

    # ── 頂層：解析「乘法運算式」 ─────────────────────────────
    def parse_expr(self) -> int:
        """
        expr ::= term ('*' term)*
        乘法為最外層（最低優先），先解析各個 term，再依序相乘。
        """
        result = self.parse_term()              # 解析第一個 term
        while self.pos < len(self.s) and self.s[self.pos] == '*':
            self.pos += 1                       # 消耗 '*'
            result *= self.parse_term()         # 繼續解析下一個 term
        return result

    # ── 中層：解析「加法運算式」 ─────────────────────────────
    def parse_term(self) -> int:
        """
        term ::= atom ('+' atom)*
        加法為內層（高優先），先解析各個 atom，再依序相加。
        """
        result = self.parse_atom()              # 解析第一個 atom
        while self.pos < len(self.s) and self.s[self.pos] == '+':
            self.pos += 1                       # 消耗 '+'
            result += self.parse_atom()         # 繼續解析下一個 atom
        return result

    # ── 底層：解析「數字」或「f函式」 ───────────────────────
    def parse_atom(self) -> int:
        """
        atom ::= NUMBER | 'f' '(' args ')'
        """
        if self.s[self.pos] == 'f':
            # ── 解析 f 函式 ───────────────────────────────────
            self.pos += 1           # 消耗 'f'
            self.pos += 1           # 消耗 '('

            args = [self.parse_expr()]   # 解析第一個參數
            while self.s[self.pos] == ',':
                self.pos += 1            # 消耗 ','
                args.append(self.parse_expr())  # 解析後續參數

            self.pos += 1           # 消耗 ')'
            # f 回傳：最大值 − 最小值
            return max(args) - min(args)

        else:
            # ── 解析整數 ──────────────────────────────────────
            start = self.pos
            while self.pos < len(self.s) and self.s[self.pos].isdigit():
                self.pos += 1
            return int(self.s[start:self.pos])


def main():
    # APCS 可能有多筆測試資料，逐行讀取直到 EOF
    import sys
    for line in sys.stdin:
        expr = line.strip()
        if not expr:
            continue
        parser = Parser(expr)
        print(parser.parse_expr())


if __name__ == '__main__':
    main()
