# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # define pointers
        fast = head
        slow = head
        
        # use fast and slow pointers to find if there is a cycle
        cycle_found = False
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                cycle_found = True
                break
        
        # if cycle found return node where the cycle begins
        if cycle_found:
            # perform Floyd's alg
            pointer_1 = head
            pointer_2 = fast
            while pointer_1 != pointer_2:
                pointer_1 = pointer_1.next
                pointer_2 = pointer_2.next
            return pointer_1
        else:
            # return null if no cycle found
            return None
        