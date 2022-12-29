# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # define fast and slow pointers
        fast = head
        slow = head
        
        # move fast pointer ahead by n steps
        for i in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        # traverse linked list until fast reaches end
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        # skip removed node
        slow.next = slow.next.next
        
        # return head with nth node from the end of the list removed
        return head
            
        