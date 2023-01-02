# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # base case: if list of length 0 or 1, return head
        if not head or not head.next:
            return head
        
        # swap every two adjacent nodes
        cur = head
        dummy = ListNode
        dummy.next = cur
        pre = dummy
        while cur and cur.next:
            nex = cur.next
            cur.next = nex.next
            pre.next = nex
            nex.next = cur
            pre = cur
            cur = pre.next
        
        # return list with nodes swapped in pairs
        return dummy.next
