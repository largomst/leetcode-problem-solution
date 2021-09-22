#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#

# @lc code=start


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10 ** 4+10**3
        self.slots = [None]*self.size

    def add(self, key: int) -> None:
        if not self.contains(key):
            hash = self._hash(key)
            while self.slots[hash] and self.slots[hash] != key:
                hash = self._rehash(hash)
            self.slots[hash] = key

    def remove(self, key: int) -> None:
        if self.contains(key):
            hash = self._hash(key)
            while self.slots[hash] and self.slots[hash] != key:
                hash = self._rehash(hash)
            self.slots[hash] = None

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.slots

    def _hash(self, key: int) -> int:
        return key % self.size

    def _rehash(self, old_hash: int) -> int:
        return (old_hash+1) % self.size

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end
