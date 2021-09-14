/*
 * @lc app=leetcode.cn id=141 lang=golang
 *
 * [141] 环形链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func hasCycle(head *ListNode) bool {
	visited := make(map[*ListNode]int)
	found := false
	if head == nil {
		return false
	}
	for cur := head; cur != nil; cur = cur.Next {
		_, prs := visited[cur]
		if prs {
			found = true
			break
		}
		visited[cur] = 0
	}
	return found
}

// @lc code=end
