# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # base case
        if not head or not head.next or k == 0:
            return head
        
        # make circularly linked list and find length of list
        length_list = 0
        pre = None
        cur = head
        while(cur):
            pre = cur
            cur = cur.next
            length_list += 1
        cur = head
        pre.next = cur
        
        # reduce k by mod length of list
        k = k % length_list
        
        # find new head
        for _ in range(length_list-k):
            pre = cur
            cur = cur.next
            
        # remove connection
        pre.next = None
        
        # return new head
        return cur
