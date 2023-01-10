# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # dummy = ListNode()
        dummy = ListNode()
        n = dummy
        
        carry_one = 0
        while l1 or l2 or carry_one:
            v1 = 0
            v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            next_value = v1 + v2 + carry_one
            if next_value >= 10:
                carry_one = 1
                next_value -= 10
            else:
                carry_one = 0
            n.next = ListNode(next_value)
            n = n.next
        return dummy.next
