#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#
import random


class MyHashSet0:

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


# @lc code=start

class Node:

    def __init__(self) -> None:
        self.val = None
        self.next = None

    def __contains__(self, val):
        cur = self
        while cur:
            if cur.val == val:
                return True
            cur = cur.next
        return False

    def add(self, val):
        new = Node()
        new.val = val
        new.next = self.next
        self.next = new

    def remove(self, val):
        prev = self
        cur = self.next
        while cur:
            if cur.val == val:
                prev.next = cur.next
                break
            prev = cur
            cur = cur.next

    def __repr__(self) -> str:
        l = []
        cur = self.next
        while cur:
            l.append(str(cur.val))
            cur = cur.next
        return '->' + '->'.join(l)


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10**4
        self.slots = []
        for _ in range(self.size):
            self.slots.append(Node())

    def add(self, key: int) -> None:
        if not self.contains(key):
            hash = self._hash(key)
            self.slots[hash].add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            hash = self._hash(key)
            self.slots[hash].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash = self._hash(key)
        return key in self.slots[hash]

    def _hash(self, key: int) -> int:
        return key % self.size

    def _rehash(self, old_hash: int) -> int:
        return (old_hash+1) % self.size

    def __repr__(self):
        l = []
        for i, node in enumerate(self.slots):
            l.append(f'{i}:{node}')
        return '\n'.join(l)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end


def genRandomOps():
    ops = []
    for i in range(100):
        ops.append(
            (random.choice(['add', 'contains', 'remove']), random.randint(0, 10)))
    return ops


# def comparar():
#     ops = genRandomOps()
#     h0 = MyHashSet0()
#     h1 = MyHashSet()
#     for i, (op, val) in enumerate(ops):
#         r0 = getattr(h0, op)(val)
#         r1 = getattr(h1, op)(val)
#         print(op, val)
#         print(h1)
#         time.sleep(2)
#         if r0 != r1:
#             print('Fcuk')
#             break
#         # print(f'\r{i/100:.2f}%', end='')
#     else:
#         print('Nice')


def comparar():
    ops = genRandomOps()
    h0 = MyHashSet0()
    h1 = MyHashSet()
    for i, (op, val) in enumerate(ops):
        r0 = getattr(h0, op)(val)
        r1 = getattr(h1, op)(val)
        if r0 != r1:
            print('Fcuk')
            break
        print(f'\r{i/99:.2f}%', end='')
    else:
        print('Nice')


comparar()
