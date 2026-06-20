# Unit 06：迴圈與數學計算

## 學習目標
- 使用迴圈計算累加、累乘、平均
- 理解 Running Total / Running Product 模式
- 能結合數學演算法

---

## 概念說明

三大模式：累加（Running Total）、累乘（Running Product）、平均

| 模式 | 初始值 | 核心操作 |
|------|--------|---------|
| 累加 | `sum = 0` | `sum += value` |
| 累乘 | `product = 1` | `product *= value` |
| 平均 | `sum = 0` | `(double) sum / count` |

---

## 程式碼範例

### 範例 1：計算 1-100 總和（累加）
```java
int sum = 0;
for (int i = 1; i <= 100; i++) {
    sum += i;
}
System.out.println("Sum = " + sum);  // 5050
```

### 範例 2：階乘計算（累乘）
```java
int n = 10;
long factorial = 1;
for (int i = 1; i <= n; i++) {
    factorial *= i;
}
System.out.println(n + "! = " + factorial);  // 3628800
```

### 範例 3：陣列平均值（注意 int/double 轉型）
```java
int[] data = {85, 90, 78, 92, 88};
double total = 0;
for (int i = 0; i < data.length; i++) {
    total += data[i];
}
double avg = total / data.length;
System.out.printf("平均：%.2f%n", avg);
```

### 範例 4：GCD（輾轉相除法）
```java
int a = 48, b = 18;
while (b != 0) {
    int temp = b;
    b = a % b;
    a = temp;
}
System.out.println("GCD = " + a);  // 6
```

### 範例 5：Fibonacci 數列（追蹤前兩值）
```java
int a = 1, b = 1;
System.out.print(a + " " + b + " ");
for (int i = 3; i <= 15; i++) {
    int c = a + b;
    System.out.print(c + " ");
    a = b;
    b = c;
}
```

---

## 練習題

### Easy：計算 `base^exp`（不使用 `Math.pow()`）
base=3, exp=5 → 243

### Medium：印出 Fibonacci 前 15 項

---

## 現在試試看
計算 1² + 2² + ... + 20² 的總和
