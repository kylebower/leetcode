# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head.next:
            return None
        
        # define pointers
        fast = head
        slow = head
        dummy = ListNode()
        dummy.next = head
        
        # iterate to find middle of list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            dummy = dummy.next
        
        # delete middle node
        dummy.next = dummy.next.next
        
        # return the head of the modified linked list
        return head
            