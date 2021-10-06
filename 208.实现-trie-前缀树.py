#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start

class Trie:
    def __init__(self):
        self.isEnd = False
        self.next = [None]*26

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            # print(ch)
            ch = ord(ch)-ord('a')
            if not node.next[ch]:
                return None
            node = node.next[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch)-ord('a')
            if not node.next[ch]:
                node.next[ch] = Trie()
            node = node.next[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        return node is not None


# @lc code=end
if __name__ == '__main__':
    trie = Trie()
    trie.insert('aaaaa')
    trie.insert('goo')
    trie.insert('goog')
    assert trie.search('aaaaa')
    assert not trie.search('go')
    assert trie.startsWith('go')
    assert not trie.startsWith('gb')
