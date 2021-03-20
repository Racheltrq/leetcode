# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        
        
        carry = 0
        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + carry
            carry = 0
            if sum > 9:
                carry += 1
                sum -= 10
            l1.val = sum
            l1 = l1.next
            l2 = l2.next
        
        if l1 is None:
            while l2 is not None:
                sum = carry + l2.val
                carry = 0
                if sum > 9:
                    carry += 1
                    sum -= 10
                l1 = p1
                while l1.next is not None:
                    l1 = l1.next
                l1.next = ListNode(sum)
                l1 = l1.next
                l2 = l2.next
                
            
            
        
        elif l2 is None:
            while l1 is not None:
                sum = l1.val + carry
                carry = 0
                if sum > 9:
                    carry += 1
                    sum -= 10
                l1.val = sum
                
                l1 = l1.next
        
        if carry == 1:
            p2 = p1
            while p2.next is not None:
                p2 = p2.next
            p2.next = ListNode(1)
        return p1