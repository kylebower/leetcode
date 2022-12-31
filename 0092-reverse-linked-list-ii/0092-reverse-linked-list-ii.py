# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # base cases
        if head.next == None:
            return head
        if left == right:
            return head
        
        # define pre and cur pointer
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        cur = head
        
        # move pre and cur to left border
        for i in range(1,left):
            pre = pre.next
            cur = cur.next
        
        # reverse sublist
        num_connections = right - left
        nex = None
        for i in range(num_connections):
            nex = cur.next
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
        
        return dummy.next
