"""
=============================================================================
範例 2：巢狀 Dict 遞迴操作（中級）
=============================================================================

【教學目標】
- 學會走訪巢狀 Dict
- 學會在巢狀 Dict 中搜尋與修改
- 理解 Dict + List 混合的遞迴處理

【應用場景】
APCS 中常見巢狀 Dict 的題型：
1. JSON 設定檔解析
2. 樹狀分類結構（類別、標籤）
3. 組織架構查詢
4. 檔案系統路徑查詢
=============================================================================
"""


# ─────────────────────────────────────────────────────────────
# 1. 巢狀 Dict 深度走訪
# ─────────────────────────────────────────────────────────────
def print_all_pairs(d, prefix=""):
    """
    走訪巢狀 Dict，輸出所有 key-value 對。
    value 如果是 Dict，遞迴進入並在 key 前加上父層路徑。
    value 如果是 List，對每個元素遞迴處理（若元素是 Dict）。

    範例走訪：
      {"a": 1, "b": {"c": 2, "d": [3, {"e": 4}]}}
      輸出：
        a = 1
        b.c = 2
        b.d[0] = 3
        b.d[1].e = 4
    """
    for key, val in d.items():
        current_key = f"{prefix}.{key}" if prefix else key
        if isinstance(val, dict):
            print_all_pairs(val, current_key)   # 遞迴子 Dict
        elif isinstance(val, list):
            for idx, item in enumerate(val):
                list_key = f"{current_key}[{idx}]"
                if isinstance(item, dict):
                    print_all_pairs(item, list_key)  # List 中的 Dict
                else:
                    print(f"{list_key} = {item}")
        else:
            print(f"{current_key} = {val}")


# ─────────────────────────────────────────────────────────────
# 2. 查找巢狀 Dict 中特定 Key 的所有值
# ─────────────────────────────────────────────────────────────
def find_all_values(d, target_key):
    """
    搜尋巢狀 Dict 中所有 key 等於 target_key 的值。
    不論位在哪一層，只要 key 符合就收集。

    例如 data = {"x": 1, "y": {"x": 2, "z": {"x": 3}}}
    find_all_values(data, "x") → [1, 2, 3]

    注意：在同層可能有多個相同 key（但 Python dict key 唯一，
    所以主要會在不同層找到相同 key 名）。
    """
    results = []
    for key, val in d.items():
        if key == target_key:
            results.append(val)
        if isinstance(val, dict):
            results.extend(find_all_values(val, target_key))
        elif isinstance(val, list):
            for item in val:
                if isinstance(item, dict):
                    results.extend(find_all_values(item, target_key))
    return results


# ─────────────────────────────────────────────────────────────
# 3. 巢狀 Dict 深層修改
# ─────────────────────────────────────────────────────────────
def set_deep_value(d, keys_list, new_val):
    """
    根據 keys_list 路徑設定巢狀 Dict 的值。
    例如 keys_list = ["a", "b", "c"] 代表 d["a"]["b"]["c"] = new_val。

    這個函式示範如何在遞迴過程中「修改」原本的結構。
    注意：dict 是可變物件，修改會直接影響原資料。

    基底條件：keys_list 只剩一個 key → 直接設定值
    遞迴條件：keys_list 還有兩個以上 key → 取得子 dict 繼續遞迴
    """
    if len(keys_list) == 1:
        d[keys_list[0]] = new_val
        return
    first, rest = keys_list[0], keys_list[1:]
    if first in d and isinstance(d[first], dict):
        set_deep_value(d[first], rest, new_val)


# ─────────────────────────────────────────────────────────────
# 4. 取得巢狀 Dict 中指定路徑的值（安全版）
# ─────────────────────────────────────────────────────────────
def get_deep_value(d, keys_list, default=None):
    """
    根據 keys_list 路徑安全取值，若路徑不存在回傳 default。
    不拋出 KeyError 或 TypeError。

    範例：
      get_deep_value({"a": {"b": 1}}, ["a", "b"]) → 1
      get_deep_value({"a": {"b": 1}}, ["a", "x"]) → None
      get_deep_value({"a": 1}, ["a", "b"]) → None
    """
    if not keys_list:
        return default
    if not isinstance(d, dict):
        return default
    key = keys_list[0]
    if key not in d:
        return default
    if len(keys_list) == 1:
        return d[key]
    return get_deep_value(d[key], keys_list[1:], default)


# ─────────────────────────────────────────────────────────────
# 5. 巢狀 Dict 扁平化（將巢狀結構變成一層 key.path）
# ─────────────────────────────────────────────────────────────
def flatten_dict(d, parent_key=""):
    """
    將巢狀 Dict 扁平化為一層 Dict，key 用 "." 連接路徑。

    範例：
      flatten_dict({"a": 1, "b": {"c": 2, "d": 3}})
      → {"a": 1, "b.c": 2, "b.d": 3}

    注意：如果 value 也是 dict，繼續遞迴；否則直接填入。
    這裡的 List 不會進一步展開。
    """
    items = {}
    for key, val in d.items():
        new_key = f"{parent_key}.{key}" if parent_key else key
        if isinstance(val, dict):
            items.update(flatten_dict(val, new_key))
        else:
            items[new_key] = val
    return items


# ─────────────────────────────────────────────────────────────
# 6. 計算巢狀 Dict 的最大深度
# ─────────────────────────────────────────────────────────────
def dict_depth(d):
    """
    計算巢狀 Dict 的最大深度。
    定義：空 dict 深度為 1，{"a": 1} 深度為 1，
          {"a": {"b": 1}} 深度為 2。

    遞迴公式：
      depth = 1 + max(每個 value 的 depth)
      對非 dict 的 value 而言 depth = 0
    """
    if not isinstance(d, dict):
        return 0
    if not d:
        return 1
    return 1 + max(dict_depth(val) for val in d.values())


# ─────────────────────────────────────────────────────────────
# 主程式測試
# ─────────────────────────────────────────────────────────────
if __name__ == '__main__':
    data = {
        "name": "root",
        "level": 1,
        "child": {
            "name": "level1",
            "tags": ["python", "recursion"],
            "child": {
                "name": "level2",
                "value": 42
            }
        }
    }

    print("1. 巢狀 Dict 深度走訪：")
    print_all_pairs(data)

    print(f"\n2. 查找所有 'name' key 的值：{find_all_values(data, 'name')}")
    print(f"3. Dict 深度：{dict_depth(data)}")
    print(f"4. 扁平化 Dict：{flatten_dict(data)}")

    print("\n5. 安全取值測試：")
    print(f"   data.child.child.name = {get_deep_value(data, ['child', 'child', 'name'])}")
    print(f"   data.child.x = {get_deep_value(data, ['child', 'x'], 'NOT_FOUND')}")

    print("\n6. 深層修改測試：")
    set_deep_value(data, ["child", "child", "value"], 99)
    print(f"   修改後 data.child.child.value = {data['child']['child']['value']}")
