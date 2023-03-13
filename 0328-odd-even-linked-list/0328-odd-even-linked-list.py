# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # base case
        if not head or not head.next:
            return head
        
        # define two pointers
        odd = head
        even = head.next
        eHead = even
        
        while even and even.next:
            
            odd.next = odd.next.next
            even.next = even.next.next
            
            odd = odd.next
            even = even.next
        
        odd.next = eHead
        
        return head
    