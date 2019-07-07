# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 确保l1.head.val <= l2.head.val
        if l1.val > l2.val:
            tmp = l1
            l1 = l2
            l2 = tmp
        cursor1,cursor2 = ListNode(0),ListNode(0)
        cursor1.next,cursor2.next = l1,l2

        while cursor1.next is not None and cursor2.next is not None:
            if cursor1.next.val > cursor2.next.val:
                next1 = cursor1.next
                next2 = cursor2.next
                cursor2.next = next2.next
                cursor1.next = next2
                next2.next = next1
            cursor1 = cursor1.next

        if cursor1.next is None and cursor2.next is not None:
            cursor1.next = cursor2.next
        return l1

# beats 99.99%, 相比之前代码，通过新建一个链表，简化操作
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        cursor = ListNode(0)
        result = cursor
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                cursor.next = l1
                l1 = l1.next
            else:
                cursor.next = l2
                l2 = l2.next
            cursor = cursor.next
        if l1 is None:
            cursor.next = l2
        else:
            cursor.next = l1

        return result.next