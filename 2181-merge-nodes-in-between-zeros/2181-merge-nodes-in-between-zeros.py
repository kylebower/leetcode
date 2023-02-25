# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # define params
        dummy = ListNode(0)
        cur = dummy
        sum_so_far = 0
        
        # step to first non-zero element
        while head.next and head.val != 0:
            head = head.next
                
        # For every two consecutive 0's, merge all the nodes lying in
        # between them into a single node whose value is the sum of all the merged nodes
        while head:
            if head.val == 0:
                if sum_so_far != 0:
                    cur.next = ListNode(sum_so_far)
                    cur = cur.next
                sum_so_far = 0
            else:
                sum_so_far += head.val
            head = head.next        
        
        # Return the head of the modified linked list
        return dummy.next
        