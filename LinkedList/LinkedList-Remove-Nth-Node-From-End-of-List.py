# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        first_node = head
        if head.next is None and n == 1:
            return None
        count = 1
        while head.next is not None:
            head = head.next
            count += 1
        if n == count:
            return first_node.next
        ind = 1
        head = first_node
        while ind < count - n:
            head = head.next
            ind += 1
        if n == 1:
            head.next = None
            return first_node
        head.next = head.next.next
        return first_node
