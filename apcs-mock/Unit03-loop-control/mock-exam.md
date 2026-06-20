# Unit 03：迴圈控制變數與條件設計 — APCS 模擬練習

> **題型：** 選擇題 (MCQ) + 程式實作 (FRQ) | **總分：** 20 分 | **時間：** 25 分鐘

---

## 選擇題（每題 3 分，共 15 分）

### 1. 執行次數計算
```java
for (int i = 3; i <= 8; i++) {
    System.out.println(i);
}

此迴圈執行幾次？
(A) 5  (B) 6  (C) 8  (D) 11
```
### 2. Off-by-one
```
下列哪個 for 迴圈會輸出 1 到 100（含）的所有整數？
(A) for (int i = 1; i < 100; i++)
(B) for (int i = 1; i <= 100; i++)
(C) for (int i = 0; i < 100; i++)
(D) for (int i = 0; i <= 100; i++)
```

### 3. 複合條件
```java
for (int i = 1; i <= 50; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
        System.out.print(i + " ");
    }
}

輸出為何？
(A) 3 6 9 12 15 ... (所有 3 的倍數)
(B) 5 10 15 20 ... (所有 5 的倍數)
(C) 15 30 45  
(D) 15 30 45 60
```
### 4. 浮點數陷阱
```java
double x = 0.0;
int count = 0;
while (x != 1.0) {
    x += 0.1;
    count++;
}

對此程式碼的敘述，何者正確？
(A) 執行 10 次後正常結束
(B) 因浮點數精度問題可能造成無限迴圈
(C) 編譯錯誤
(D) 執行 9 次後結束
```
### 5. 控制變數修改
```java
int sum = 0;
for (int i = 1; i <= 10; i++) {
    sum += i;
    if (sum > 20) {
        i += 5;
    }
}
System.out.println(sum);

輸出為何？
(A) 55  (B) 28  (C) 36  (D) 30
```
---

## 程式實作（5 分）

### FRQ：範圍內的奇數和
撰寫方法計算從 `start` 到 `end`（含）之間所有奇數的總和。

```java
public static int sumOddInRange(int start, int end)
```

**注意：** 需確保你的條件設計不會產生 Off-by-one 錯誤。

**範例：**
- `sumOddInRange(1, 10)` → 1+3+5+7+9 = **25**
- `sumOddInRange(4, 8)` → 5+7 = **12**
- `sumOddInRange(2, 2)` → **0**（無奇數）

> 解答請見：`answer-key.md`
