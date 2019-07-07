# https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import queue
class Solution:
    # O(k*n) 的复杂度，超时
    def mergeKLists0(self, lists: List[ListNode]) -> ListNode:
        result = ListNode(0)
        dummy = result
        while True:
            minNode = None
            minIdx = -1
            for i in range(0,len(lists)):
                if minNode is None or lists[i] is not None and lists[i].val < minNode.val:
                    minNode = lists[i]
                    minIdx = i
            if minNode is None:
                break
            else:
                dummy.next = minNode
                dummy = dummy.next
                lists[minIdx] = lists[minIdx].next

        return result.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        result = ListNode(0)
        dummy = result
        priorityQueue = queue.PriorityQueue()
        h=[]
        for l in lists:
            if l is not None:
                # 这一行会报错，还不清楚为什么
                priorityQueue.put((l.val,l))

        while priorityQueue.empty():
            node = priorityQueue.get()
            dummy.next = node
            dummy = dummy.next
            node = node.next
            if node:
                priorityQueue.put((node.val,node))

        return result.next

head1= ListNode(1)
head1.next=ListNode(4)
head2 = ListNode(1)
head2.next = ListNode(3)
head3=ListNode(2)
head3.next = ListNode(6)
lists=[]
lists.append(head1)
lists.append(head2)
lists.append(head3)

s= Solution()
s.mergeKLists(lists)