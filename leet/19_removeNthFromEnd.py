# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre,post = head,head
        i = 0
        while i < n:
            if pre is None:
                return head
            pre = pre.next
            i+=1

        # 重点在于此，异常情况的归类与考虑
        if pre is None:
            return head.next
            
        while pre.next is not None:
            pre = pre.next
            post = post.next

        post.next = post.next.next
        return head
