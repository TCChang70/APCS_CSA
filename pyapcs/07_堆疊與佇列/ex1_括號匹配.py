"""
APCS 堆疊範例 1：括號匹配（初級）

經典 Stack 應用：檢查字串中的括號是否合法配對。
支援 ()、{}、[] 三種括號。

規則：
1. 左括號必須有對應的右括號
2. 括號必須正確嵌套，不能交叉
"""


def is_valid_parentheses(s):
    pair = {')': '(', '}': '{', ']': '['}
    stack = []
    for ch in s:
        if ch in '({[':
            stack.append(ch)
        elif ch in ')}]':
            if not stack or stack[-1] != pair[ch]:
                return False
            stack.pop()
    return not stack


if __name__ == '__main__':
    tests = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}",
    ]
    for t in tests:
        print(f"{t:10s} → {is_valid_parentheses(t)}")
