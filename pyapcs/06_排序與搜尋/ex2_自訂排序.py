"""
APCS 排序範例 2：自訂排序規則（初級）

APCS 常見題型：不單純照數字大小排序，而是依特定規則。
使用 sorted() 的 key 參數搭配 lambda 或自訂函式。

常見規則：
1. 字串長度排序
2. 多欄位排序（先成績降冪、再年齡升冪）
3. 特殊規則（如偶數在前、奇數在後）
"""


students = [
    ("Alice", 85, 17),
    ("Bob", 92, 16),
    ("Charlie", 85, 18),
    ("David", 92, 15),
]

by_score_desc_age_asc = sorted(
    students,
    key=lambda s: (-s[1], s[2])
)

print("成績高→低，同分者年齡小→大：")
for name, score, age in by_score_desc_age_asc:
    print(f"  {name}: {score}分, {age}歲")


words = ["apple", "hi", "banana", "cat", "elephant"]
by_len = sorted(words, key=len)
print(f"依長度排序: {by_len}")


nums = [1, 2, 3, 4, 5, 6, 7, 8]
even_first = sorted(nums, key=lambda x: (x % 2, x))
print(f"偶數在前: {even_first}")
