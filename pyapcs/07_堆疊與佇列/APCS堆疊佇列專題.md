# APCS 堆疊與佇列（Stack & Queue）專題

## 目錄

1. [堆疊（Stack）](#堆疊stack)
2. [佇列（Queue）](#佇列queue)
3. [雙端佇列（Deque）](#雙端佇列deque)
4. [APCS 常見題型](#apcs-常見題型)
5. [各題型範例與程式](#各題型範例與程式)
6. [效能比較](#效能比較)
7. [實戰建議](#實戰建議)

---

## 堆疊（Stack）

**LIFO（Last In, First Out）** — 後進先出。

Python 中直接用 `list` 實作：
| 操作 | 寫法 | 時間 |
|------|------|------|
| 推入 | `stack.append(x)` | O(1) |
| 彈出 | `stack.pop()` | O(1) |
| 看頂端 | `stack[-1]` | O(1) |
| 是否為空 | `not stack` | O(1) |

**應用場景**：
- 括號匹配
- 函式呼叫追蹤（Call Stack）
- 回溯（Backtracking）
- 運算式求值（中序→後序）
- 單調堆疊（Monotonic Stack）

---

## 佇列（Queue）

**FIFO（First In, First Out）** — 先進先出。

Python 中建議用 `collections.deque`：
| 操作 | 寫法 | 時間 |
|------|------|------|
| 入隊 | `q.append(x)` | O(1) |
| 出隊 | `q.popleft()` | O(1) |
| 看前端 | `q[0]` | O(1) |
| 看末端 | `q[-1]` | O(1) |

> **不要用 `list` 實作佇列**：`pop(0)` 是 O(N)。

**應用場景**：
- BFS（廣度優先搜尋）
- 模擬排隊
- 滑動視窗
- 工作排程

---

## 雙端佇列（Deque）

`collections.deque` 支援兩端皆可 O(1) 新增/移除。

| 操作 | 寫法 |
|------|------|
| 左端加入 | `d.appendleft(x)` |
| 右端加入 | `d.append(x)` |
| 左端彈出 | `d.popleft()` |
| 右端彈出 | `d.pop()` |

---

## APCS 常見題型

| 題型 | 資料結構 | 難度 |
|------|----------|------|
| 括號匹配 | Stack | 初級 |
| 佇列模擬（排隊問題） | Queue / Deque | 初級 |
| 網頁前進/後退 | Stack x2 | 初級 |
| 車站調度問題 | Stack | 中級 |
| BFS 最短路徑 | Queue | 中級 |
| 單調堆疊（找下一個更大元素） | Stack | 中高級 |
| 滑動視窗最大值 | Deque（單調佇列） | 中高級 |

---

## 各題型範例與程式

| 檔案 | 題型 | 難度 |
|------|------|------|
| `ex1_括號匹配.py` | Stack 經典題 | 初級 |
| `ex2_佇列模擬.py` | Queue / Deque 應用 | 初級 |
| `ex3_BFS最短路徑.py` | Queue 圖論 BFS | 中級 |
| `ex4_單調堆疊.py` | 找下一個更大元素 | 中高級 |
| `ex5_單調佇列.py` | 滑動視窗最大值 | 中高級 |

---

## 效能比較

```
N = 100,000

list 當 stack (append/pop):      0.01s ✓
list 當 queue (append/pop(0)):    > 60s ✗ TLE
deque 當 queue (append/popleft): 0.01s ✓

APCS 實戰鐵則：queue 就用 deque，別用 list。
```

---

## 實戰建議

1. **Stack 用 list**：`append()` + `pop()` 即可
2. **Queue 用 `collections.deque`**：`append()` + `popleft()`
3. **BFS 模板**熟記：Queue 存 (位置, 步數) → 四方向擴散
4. **單調堆疊**：遇到「找左/右第一個比當前大/小的元素」時使用
5. **Deque 旋轉**：`d.rotate(k)` 可模擬環狀佇列

---

> 檔案日期：2026-06-20
> 適用範圍：APCS 大學程式設計先修檢測（114 學年度起新制）
