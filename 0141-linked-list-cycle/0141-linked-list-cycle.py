# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # define fast and slow pointers
        fast = head
        slow = head
        
        # use fast and slow pointers to find if there is a cycle
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # Return true if there is a cycle
                return True
        
        # Return false if no cycle found
        return False
