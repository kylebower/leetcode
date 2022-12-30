# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # base case
        if head == None:
            return head
        
        # define current and previous pointers
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        
        # remove repeated nodes
        while cur != None:
            if cur.val == val:
                prev.next = cur.next
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
        
        # return the new head
        return dummy.next
