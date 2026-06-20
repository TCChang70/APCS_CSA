"""
APCS 遞迴範例 1：階乘與費氏數列（初級）

階乘：n! = n × (n-1)!
費氏：F(n) = F(n-1) + F(n-2)

這是最基本的遞迴形式：直接將數學定義轉為程式碼。
"""


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    for i in range(10):
        print(f"factorial({i}) = {factorial(i)}")
    print("---")
    for i in range(10):
        print(f"fibonacci({i}) = {fibonacci(i)}")
