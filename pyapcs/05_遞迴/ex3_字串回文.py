"""
APCS 遞迴範例 3：字串回文判斷（初級）

回文：正著讀與反著讀都一樣的字串，如 "racecar"。
遞迴策略：每次檢查頭尾字元是否相同，然後縮減字串範圍。
基底條件：字串長度 ≤ 1 → 是回文。
"""


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


if __name__ == '__main__':
    tests = ["racecar", "hello", "level", "python"]
    for t in tests:
        print(f"is_palindrome({t!r}) = {is_palindrome(t)}")
    print(reverse_string("APCS"))
