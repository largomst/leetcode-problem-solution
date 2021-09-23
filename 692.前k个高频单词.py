#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#
from unittest import TestCase, main
from typing import List
# @lc code=start

import heapq


class Node:
    def __init__(self, word, value) -> None:
        self.word = word
        self.value = value

    def __lt__(self, other: 'Node'):
        if self.value == other.value:
            return self.word > other.word
        else:
            return self.value < other.value


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = {}
        heap = []
        for word in words:
            if word in hashmap:
                hashmap[word] += 1
            else:
                hashmap[word] = 1
        for key, value in hashmap.items():
            heapq.heappush(heap, Node(key, value))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        while heap:
            result.append(heapq.heappop(heap).word)
        result.reverse()
        return result


# @lc code=end


class Test(TestCase):
    def test_node_lt(self):
        nodes = [Node('a', 10), Node('c', 20), Node('b', 20)]
        nodes.sort()
        assert nodes[0].word == 'a'
        assert nodes[1].word == 'c'
        assert nodes[2].word == 'b'

    def test_solution(self):
        l = ["i", "love", "leetcode", "i", "love", "coding"]
        r = Solution().topKFrequent(l, 2)
        assert ["i", "love"] == r


main()
