"""
=============================================================================
範例 3：JSON 結構遞迴操作（中級～中高級）
=============================================================================

【教學目標】
- 學會處理 List + Dict 混合的巢狀結構
- 實作組織樹的深度遍歷
- 學會複製/轉換巢狀結構

【應用場景】
- JSON API 回應解析
- 檔案目錄樹走訪
- 選單/分類結構處理
- 資料轉換（例如樹狀資料轉為表格）

=============================================================================
"""

# ─────────────────────────────────────────────────────────────
# 範例資料：組織樹
# ─────────────────────────────────────────────────────────────
org_tree = {
    "name": "總公司",
    "employees": 120,
    "departments": [
        {
            "name": "研發部",
            "budget": 500,
            "teams": [
                {"name": "前端組", "members": 8, "lead": "Alice"},
                {"name": "後端組", "members": 12, "lead": "Bob"},
                {"name": "AI組", "members": 5, "lead": "Charlie"}
            ]
        },
        {
            "name": "行銷部",
            "budget": 300,
            "teams": [
                {"name": "廣告組", "members": 6, "lead": "Diana"},
                {"name": "公關組", "members": 4, "lead": "Eve"}
            ]
        },
        {
            "name": "財務部",
            "budget": 200,
            "teams": [
                {"name": "會計組", "members": 7, "lead": "Frank"}
            ]
        }
    ]
}


# ─────────────────────────────────────────────────────────────
# 1. 計算組織總人數（遞迴累加）
# ─────────────────────────────────────────────────────────────
def count_total_employees(node):
    """
    遞迴計算組織總人數。
    每個節點可能有 employees 或 members 欄位，
    以及 departments 或 teams 子節點列表。
    """
    total = 0
    if "employees" in node:
        total += node["employees"]
    if "departments" in node:
        for dept in node["departments"]:
            total += count_total_employees(dept)
    if "teams" in node:
        for team in node["teams"]:
            if "members" in team:
                total += team["members"]
    return total


# ─────────────────────────────────────────────────────────────
# 2. 列出所有團隊負責人（走訪所有 leaf 節點）
# ─────────────────────────────────────────────────────────────
def list_all_leads(node, results=None):
    """
    收集所有團隊的 lead 名稱。
    node 可能是公司、部門或團隊。
    """
    if results is None:
        results = []
    if "lead" in node:
        results.append((node["name"], node["lead"]))
    if "departments" in node:
        for dept in node["departments"]:
            list_all_leads(dept, results)
    if "teams" in node:
        for team in node["teams"]:
            list_all_leads(team, results)
    return results


# ─────────────────────────────────────────────────────────────
# 3. 依條件篩選節點（預算 > 250 的部門）
# ─────────────────────────────────────────────────────────────
def find_high_budget_depts(node, threshold=250):
    """
    遞迴找所有 budget > threshold 的部門。
    回傳部門名稱列表。
    """
    results = []
    if "budget" in node and node["budget"] > threshold:
        results.append(node["name"])
    if "departments" in node:
        for dept in node["departments"]:
            results.extend(find_high_budget_depts(dept, threshold))
    return results


# ─────────────────────────────────────────────────────────────
# 4. 建立縮排的組織圖（深度優先輸出）
# ─────────────────────────────────────────────────────────────
def print_org_chart(node, depth=0, prefix=""):
    """
    以樹狀縮排輸出組織架構。
    depth 控制縮排層數。

    輸出範例：
    ─ 總公司 (120人)
      ├─ 研發部 (預算:500)
      │  ├─ 前端組 (8人, 負責人:Alice)
      │  ├─ 後端組 (12人, 負責人:Bob)
      │  └─ AI組 (5人, 負責人:Charlie)
      ├─ 行銷部 (預算:300)
      │  ├─ 廣告組 (6人, 負責人:Diana)
      │  └─ 公關組 (4人, 負責人:Eve)
      └─ 財務部 (預算:200)
         └─ 會計組 (7人, 負責人:Frank)
    """
    indent = "  " * depth
    branch = prefix + ("├─ " if depth > 0 else "")

    if "employees" in node:
        print(f"{indent}{branch}{node['name']} ({node.get('employees', 0)}人)")
    elif "budget" in node:
        print(f"{indent}{branch}{node['name']} (預算:{node.get('budget', 0)})")
    elif "members" in node:
        print(f"{indent}{branch}{node['name']} ({node['members']}人, 負責人:{node.get('lead', 'N/A')})")

    if "departments" in node:
        for i, dept in enumerate(node["departments"]):
            is_last = (i == len(node["departments"]) - 1)
            next_prefix = "└─ " if is_last else "├─ "
            print_org_chart(dept, depth + 1, next_prefix)
    if "teams" in node:
        for i, team in enumerate(node["teams"]):
            is_last = (i == len(node["teams"]) - 1)
            next_prefix = "└─ " if is_last else "├─ "
            print_org_chart(team, depth + 1, next_prefix)


# ─────────────────────────────────────────────────────────────
# 5. 深層複製巢狀結構（避免修改原資料）
# ─────────────────────────────────────────────────────────────
def deep_copy(structure):
    """
    遞迴深層複製一個巢狀 List/Dict 結構。
    Python 的 copy.deepcopy() 也是用類似原理實作。

    三種情況：
    - Dict → 建立新 dict，對每個 value 遞迴複製
    - List → 建立新 list，對每個元素遞迴複製
    - 其他（int, str 等）→ 直接回傳（不可變物件）

    為什麼需要 deep copy？
      d2 = d1             → d1 和 d2 指向同一個 dict（淺拷貝）
      d2 = d1.copy()      → 只有第一層是新的，內層還是同一個（淺拷貝）
      d2 = deep_copy(d1)  → 每一層都是新的（深拷貝）
    """
    if isinstance(structure, dict):
        new_dict = {}
        for key, val in structure.items():
            new_dict[key] = deep_copy(val)
        return new_dict
    elif isinstance(structure, list):
        return [deep_copy(item) for item in structure]
    else:
        return structure


# ─────────────────────────────────────────────────────────────
# 6. 轉換結構：抽出所有團隊的簡表
# ─────────────────────────────────────────────────────────────
def extract_teams_table(node):
    """
    從組織樹中取出所有 team 的扁平列表，
    每個 team 轉換成 dict 包含 部門、團隊名、人數、負責人。

    這是典型的「樹轉表格」操作。
    """
    rows = []
    dept_name = node.get("name", "")

    if "teams" in node:
        for team in node["teams"]:
            rows.append({
                "department": dept_name,
                "team": team["name"],
                "members": team["members"],
                "lead": team["lead"]
            })

    if "departments" in node:
        for dept in node["departments"]:
            rows.extend(extract_teams_table(dept))

    return rows


# ─────────────────────────────────────────────────────────────
# 主程式測試
# ─────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print("=== 組織架構圖 ===")
    print_org_chart(org_tree)

    print("\n=== 各項統計 ===")
    print(f"總人數（含各級）：{count_total_employees(org_tree)}")
    print(f"所有團隊負責人：{list_all_leads(org_tree)}")
    print(f"預算 > 250 的部門：{find_high_budget_depts(org_tree)}")

    print("\n=== 團隊簡表 ===")
    table = extract_teams_table(org_tree)
    for row in table:
        print(f"  {row['department']} → {row['team']}: {row['members']}人 (lead: {row['lead']})")

    print("\n=== 深層複製測試 ===")
    copied = deep_copy(org_tree)
    copied["departments"][0]["budget"] = 999
    print(f"原結構研發部預算：{org_tree['departments'][0]['budget']}")
    print(f"複製結構研發部預算：{copied['departments'][0]['budget']}")
    print("兩者獨立，互不影響 ✓")
