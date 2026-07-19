"""
=============================================================================
練習題 2：巢狀 Dict 中查找所有含 "score" 的值（中級）
=============================================================================

給定一個巢狀 Dict（深度 ≤ 10），value 可能是 int、str、list、dict。
請找出所有 key 為 "score" 的 value，回傳為 list。

範例：
  data = {"a": {"score": 90, "b": {"score": 80}}}
  find_scores(data) → [90, 80]

如果 Dict 中有 list，list 內可能也包含 dict，需要繼續查找。

請在上方填入你的程式碼後執行測試。
=============================================================================
"""

# ── 請在這裡撰寫你的程式碼 ──────────────────────────────────
def find_scores(d):
    pass  # TODO


# ── 測試區 ──────────────────────────────────────────────────
if __name__ == '__main__':
    test_cases = [
        ({"score": 100}, [100]),
        ({"a": {"score": 90}, "b": {"score": 80}}, [90, 80]),
        ({"a": [{"score": 70}, {"score": 60}]}, [70, 60]),
        ({"a": 1, "b": "hello", "c": []}, []),
        ({"a": {"b": {"c": {"score": 50}}}}, [50]),
    ]
    for data, expected in test_cases:
        result = find_scores(data)
        status = "✓" if result == expected else "✗"
        print(f"{status} find_scores({data}) = {result} (expected {expected})")
