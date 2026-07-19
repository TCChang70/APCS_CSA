"""
=============================================================================
範例 1：巢狀 List 遞迴走訪（初級～中級）
=============================================================================

【教學目標】
- 理解巢狀 List 的遞迴結構
- 學會四種巢狀 List 基本操作：求和、找最大、扁平化、計算深度
- 比較遞迴與迭代的差異

【觀念】
巢狀 List 中的每個元素不是「數字」就是「另一個巢狀 List」。
這恰好對應遞迴的兩種路徑：基底（數字）和遞迴（子 List）。
=============================================================================
"""


# ─────────────────────────────────────────────────────────────
# 1. 巢狀 List 求和
# ─────────────────────────────────────────────────────────────
def nested_sum(nested):
    """
    巢狀 List 中所有數字的總和。

    範例追蹤 nested_sum([1, [2, 3], [[4, 5], 6]])：
      [1, [2, 3], [[4, 5], 6]]
      ├── 1 → +1
      ├── [2, 3] → 遞迴呼叫：
      │     ├── 2 → +2
      │     └── 3 → +3  → 回傳 5
      └── [[4, 5], 6] → 遞迴呼叫：
            ├── [4, 5] → 遞迴呼叫：
            │     ├── 4 → +4
            │     └── 5 → +5  → 回傳 9
            └── 6 → +6  → 回傳 15
      總和 = 1 + 5 + 15 = 21
    """
    total = 0
    for elem in nested:
        if isinstance(elem, list):   # 如果是子 List → 遞迴
            total += nested_sum(elem)
        else:                        # 如果是數字 → 直接加
            total += elem
    return total


# ─────────────────────────────────────────────────────────────
# 2. 巢狀 List 找最大值
# ─────────────────────────────────────────────────────────────
def nested_max(nested):
    """
    巢狀 List 中的最大值。
    基底條件：如果巢狀是空 List，回傳 0（假設都是正數）。
    若可能有負數，用 float('-inf') 做初始值。
    """
    best = 0
    for elem in nested:
        if isinstance(elem, list):
            best = max(best, nested_max(elem))
        else:
            best = max(best, elem)
    return best


# ─────────────────────────────────────────────────────────────
# 3. 巢狀 List 扁平化
# ─────────────────────────────────────────────────────────────
def flatten(nested):
    """
    將巢狀 List 展開成一維 List。

    範例：flatten([1, [2, [3, 4]], 5]) → [1, 2, 3, 4, 5]

    注意：用 result.extend(...) 而不是 result.append(...)，
    因為 flatten() 回傳的是 list，需要用 extend 合併。
    """
    result = []
    for elem in nested:
        if isinstance(elem, list):
            result.extend(flatten(elem))  # 遞迴展開後合併
        else:
            result.append(elem)           # 直接加入數字
    return result


# ─────────────────────────────────────────────────────────────
# 4. 計算巢狀 List 的最大深度
# ─────────────────────────────────────────────────────────────
def nested_depth(nested):
    """
    計算巢狀 List 的最大深度。
    定義：最內層元素的巢狀層數。
    空 List 深度為 1，[1, 2] 深度為 1，[1, [2]] 深度為 2。

    遞迴公式：
      depth = 1 + max(每個子元素的 depth)
      對數字而言 depth = 0
    """
    if not isinstance(nested, list):
        return 0                     # 數字不是巢狀結構
    if not nested:
        return 1                     # 空 List 深度為 1
    return 1 + max(nested_depth(elem) for elem in nested)


# ─────────────────────────────────────────────────────────────
# 5. 深度優先走訪（含路徑資訊）
# ─────────────────────────────────────────────────────────────
def dfs_nested(nested, path=""):
    """
    深度優先走訪巢狀 List，輸出每個元素的位置和值。

    範例輸出（部分）：
      dfs_nested([1, [2, 3]])
      → "arr[0] = 1"
      → "arr[1][0] = 2"
      → "arr[1][1] = 3"
    """
    for idx, elem in enumerate(nested):
        current_path = f"{path}[{idx}]"
        if isinstance(elem, list):
            dfs_nested(elem, current_path)  # 遞迴進入子 List
        else:
            print(f"{current_path} = {elem}")


# ─────────────────────────────────────────────────────────────
# 6. 巢狀 List 迭代版（Stack 模擬遞迴）
# ─────────────────────────────────────────────────────────────
def nested_sum_iterative(nested):
    """
    用 Stack 模擬遞迴實現巢狀 List 求和。
    當巢狀深度過大時（>1000），Python 遞迴會失敗，
    但此迭代版不會有 Stack Overflow 問題。

    注意：這裡的 Stack 是我們自己管理的 list，
    跟 Python 的 Call Stack 不同。
    """
    total = 0
    stack = [nested]                 # 把整個 List 推入 Stack
    while stack:
        node = stack.pop()           # 取出一個節點
        for elem in node:
            if isinstance(elem, list):
                stack.append(elem)   # 子 List 推入 Stack
            else:
                total += elem        # 數字直接加
    return total


# ─────────────────────────────────────────────────────────────
# 主程式測試
# ─────────────────────────────────────────────────────────────
if __name__ == '__main__':
    data = [1, [2, 3], [[4, 5], 6], [7, [8, [9, 10]]]]

    print("巢狀 List:", data)
    print(f"1. 總和 = {nested_sum(data)}")
    print(f"   (迭代版) = {nested_sum_iterative(data)}")
    print(f"2. 最大值 = {nested_max(data)}")
    print(f"3. 扁平化 = {flatten(data)}")
    print(f"4. 最大深度 = {nested_depth(data)}")
    print("5. DFS 走訪：")
    dfs_nested(data, "data")
