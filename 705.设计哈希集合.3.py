#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#

# @lc code=start

class MyHashSet:

    def __init__(self):
        self.size = 10**6+1
        self.slots = [None]*self.size

    def add(self, key: int) -> None:
        self.slots[key] = True

    def remove(self, key: int) -> None:
        self.slots[key] = None

    def contains(self, key: int) -> bool:
        return self.slots[key] != None

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end
