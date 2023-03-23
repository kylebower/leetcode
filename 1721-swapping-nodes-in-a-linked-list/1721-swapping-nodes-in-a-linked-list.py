# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # base case
        if not head or not head.next:
            return head
        
        # find (k-1)^th node from start
        fast = head
        for i in range(k-1):
            fast = fast.next
        first = fast
        
        # find (k+1)^th node from end
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        # swap nodes
        temp = first.val
        first.val = slow.val
        slow.val = temp
        
        # return head of the linked list after swapping the values
        return head
    