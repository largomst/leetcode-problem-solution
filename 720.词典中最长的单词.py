#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#

# @lc code=start

from typing import Dict, List, Optional


class Trie:
    def __init__(self) -> None:
        self.next: Dict[str, Trie] = dict()
        self.isEnd: bool = False

    def searchPrefix(self, prefix: str) -> Optional['Trie']:
        node = self
        for ch in prefix:
            if not node.next.get(ch):
                return None
            node = node.next[ch]
        return node

    def insert(self, word: str):
        node = self
        for ch in word:
            if not node.next.get(ch):
                node.next[ch] = Trie()
            node = node.next[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        return node is not None


class Solution:
    def longestWord(self, words: List[str]) -> str:
        if not words:
            return ""

        trie = Trie()
        res = ""

        for word in words:
            trie.insert(word)

        for word in words:
            node = trie
            if len(word) > len(res) or (len(word) == len(res) and word < res):
                for ch in word:
                    cur = node.next.get(ch)
                    if cur.isEnd is False:
                        break
                    node = node.next[ch]
                else:
                    res = word

        return res


# @lc code=end
if __name__ == '__main__':
    r = Solution().longestWord(["w", "wo", "wor", "worl", "world"])
    print(r)
    assert r == 'world'
