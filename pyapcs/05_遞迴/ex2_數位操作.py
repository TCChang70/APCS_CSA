"""
APCS 遞迴範例 2：數位操作（初級）

常見 APCS 題型：利用整數除法 // 10 與取餘 % 10 收斂。
- 數位和：sum_digits(123) → 1+2+3 = 6
- 數字反轉：reverse_num(123) → 321
- 十進位轉二進位：to_binary(6) → "110"
"""


def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


def reverse_num(n, rev=0):
    if n == 0:
        return rev
    return reverse_num(n // 10, rev * 10 + n % 10)


def to_binary(n):
    if n <= 1:
        return str(n)
    return to_binary(n // 2) + str(n % 2)


if __name__ == '__main__':
    print(sum_digits(12345))
    print(reverse_num(12345))
    print(to_binary(42))
