# Unit 15：Array 演算法：最大值、最小值、總和、搜尋

## 學習目標
- 熟練實作陣列的 4 大基礎演算法
- 理解線性搜尋（Linear Search）
- 掌握 APCS CSA 常考的陣列操作題型

---

## 4 大基礎演算法

```java
int[] arr = {64, 25, 12, 22, 11};
```

### 1. 最大值（Maximum）
```java
int max = arr[0];
for (int i = 1; i < arr.length; i++) {
    if (arr[i] > max) max = arr[i];
}
System.out.println("Max: " + max);  // 64
```

### 2. 最小值（Minimum）
```java
int min = arr[0];
for (int i = 1; i < arr.length; i++) {
    if (arr[i] < min) min = arr[i];
}
System.out.println("Min: " + min);  // 11
```

### 3. 總和與平均（Sum & Average）
```java
int sum = 0;
for (int val : arr) {
    sum += val;
}
double avg = (double) sum / arr.length;
System.out.printf("Sum: %d, Avg: %.2f%n", sum, avg);
```

### 4. 線性搜尋（Linear Search）
```java
int target = 22;
int index = -1;
for (int i = 0; i < arr.length; i++) {
    if (arr[i] == target) {
        index = i;
        break;  // 找到後提早終止
    }
}
if (index != -1) {
    System.out.println(target + " 在索引 " + index);
} else {
    System.out.println(target + " 不存在");
}
```

---

## 演算法選擇指南

| 問題 | 適用演算法 | 初始值 |
|------|-----------|--------|
| 最大值 | Maximum | `arr[0]` |
| 最小值 | Minimum | `arr[0]` |
| 總和/平均 | Sum | `0` |
| 是否存在 | Linear Search | `-1` |

---

## 練習題

### Medium：`indexOfMax(int[] arr)`
回傳最大值索引，相同時取第一個

### Hard：`countAboveAverage(int[] arr)`
統計陣列中高於平均的元素個數

---

## 現在試試看
撰寫方法回傳陣列中第二大的值
