# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # reverse linked list
        head = self.reverse(head)
        
        # save max value that was passed
        max_so_far = 0
        
        # iterate to remove nodes
        dummy = ListNode()
        res = dummy
        
        while head:
            max_so_far = max(max_so_far, head.val)
            
            if head.val == max_so_far:
                temp = ListNode(head.val)
                dummy.next = temp
                dummy = dummy.next
            
            head = head.next
            
        # return head of the modified linked list
        return self.reverse(res.next)
        
    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
    