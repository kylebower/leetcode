# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # base case: if length is 0 or 1, return head
        if not head or not head.next:
            return head
        
        # reverse the list
        reversed_list = None
        while head:
            temp = head.next
            head.next = reversed_list
            reversed_list = head
            head = temp
            
        # return result
        return reversed_list
        