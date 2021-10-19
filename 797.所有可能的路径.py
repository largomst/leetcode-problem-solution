#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []

        def traverse(graph, s, path):
            path.append(s)
            if s == n-1:
                res.append(path[:])
                path.pop()
                return
            for v in graph[s]:
                traverse(graph, v, path)
            path.pop()

        path = []
        traverse(graph, 0, path)
        return res


# @lc code=end
