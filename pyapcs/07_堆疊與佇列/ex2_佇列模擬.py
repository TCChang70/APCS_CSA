"""
APCS 堆疊範例 2：佇列模擬（初級）

使用 deque 模擬排隊場景：
- arrive(name): 新客戶加入排隊
- serve(): 服務排頭客戶
- skip(name): 特定客戶離開隊伍

展示 deque 的雙端操作效率。
"""

from collections import deque


class QueueSystem:
    def __init__(self):
        self.q = deque()

    def arrive(self, name):
        self.q.append(name)
        print(f"  {name} 加入排隊")

    def serve(self):
        if not self.q:
            print("  沒有客戶在排隊")
            return None
        name = self.q.popleft()
        print(f"  正在服務 {name}")
        return name

    def skip(self, name):
        try:
            self.q.remove(name)
            print(f"  {name} 離開隊伍")
        except ValueError:
            print(f"  {name} 不在隊伍中")


if __name__ == '__main__':
    qs = QueueSystem()
    qs.arrive("Alice")
    qs.arrive("Bob")
    qs.arrive("Charlie")
    qs.serve()
    qs.arrive("David")
    qs.skip("Bob")
    qs.serve()
    qs.serve()
    qs.serve()
