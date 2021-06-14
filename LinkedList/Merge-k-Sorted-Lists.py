# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        from heapq import heappush, heappop
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        myHeap = []
        for head in lists:
            while head != None:
                heapq.heappush(myHeap, head.val)
                head = head.next
        placeholderHead = curNode = ListNode(-1)
        while len(myHeap) > 0:
            curVal = heapq.heappop(myHeap)
            curNode.next = ListNode(curVal)
            curNode = curNode.next
        return placeholderHead.next