"""
=============================================================================
【中階遞迴範例 1】二元樹遍歷（前序/中序/後序）
=============================================================================

【教學目標】
理解樹狀結構的遞迴本質，學會三種遍歷方式。

【觀念說明】
樹是「天然的遞迴資料結構」：
- 每個節點的左子樹和右子樹各自都是一棵樹
- 只是規模更小
- 空子樹（None）就是基底條件

三種遍歷方式：
  前序（Pre-order）：   root → 左子樹 → 右子樹    [根左右]
  中序（In-order）：    左子樹 → root → 右子樹    [左根右]
  後序（Post-order）：  左子樹 → 右子樹 → root    [左右根]

應用場景：
  前序：複製樹、序列化樹
  中序：二元搜尋樹的排序輸出（結果會是遞增的）
  後序：計算樹的高度、刪除樹

=============================================================================
"""

import sys
sys.setrecursionlimit(10000)


class TreeNode:
    """二元樹節點"""
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(arr, idx=0):
    """
    用陣列建立二元樹（層序順序，-1 代表 None）。

    arr = [1, 2, 3, 4, 5, -1, 6]
    對應的樹：
          1
         / \
        2   3
       / \   \
      4   5   6
    """
    if idx >= len(arr) or arr[idx] == -1:
        return None
    node = TreeNode(arr[idx])
    node.left = build_tree(arr, 2 * idx + 1)
    node.right = build_tree(arr, 2 * idx + 2)
    return node


def preorder(root):
    """前序遍歷：根 → 左 → 右"""
    if root is None:              # 基底條件：空節點
        return []
    result = [root.val]           # 先處理根節點
    result.extend(preorder(root.left))   # 再遞迴左子樹
    result.extend(preorder(root.right))  # 最後遞迴右子樹
    return result


def inorder(root):
    """中序遍歷：左 → 根 → 右"""
    if root is None:
        return []
    result = inorder(root.left)   # 先遞迴左子樹
    result.append(root.val)       # 再處理根節點
    result.extend(inorder(root.right))  # 最後遞迴右子樹
    return result


def postorder(root):
    """後序遍歷：左 → 右 → 根"""
    if root is None:
        return []
    result = postorder(root.left)  # 先遞迴左子樹
    result.extend(postorder(root.right))  # 再遞迴右子樹
    result.append(root.val)        # 最後處理根節點
    return result


def tree_height(root):
    """
    遞迴計算樹的高度（後序遍歷的應用）。
    高度定義：根節點到最遠葉節點的邊數。
    空樹高度 = -1，只有根節點高度 = 0。

    遞迴三要素：
    1. 基底條件：None → 回傳 -1
    2. 遞迴關係：height = 1 + max(左子樹高度, 右子樹高度)
    3. 收斂性：每次往子樹移動，最終到 None
    """
    if root is None:
        return -1
    left_h = tree_height(root.left)
    right_h = tree_height(root.right)
    return 1 + max(left_h, right_h)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, -1, 6]
    root = build_tree(arr)

    print("二元樹結構（陣列表示）：", arr)
    print(f"樹的高度：{tree_height(root)}")
    print(f"前序遍歷：{preorder(root)}")
    print(f"中序遍歷：{inorder(root)}")
    print(f"後序遍歷：{postorder(root)}")
