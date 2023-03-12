# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # flip second half of list
        head = self.flipSecondHalf(head)
        
        # find midpoint of list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # iterate to find max twin sum
        max_twin_sum = 0
        while slow:
            twin_sum = head.val + slow.val
            if twin_sum > max_twin_sum:
                max_twin_sum = twin_sum
            head = head.next
            slow = slow.next
        
        # return max twin sum
        return max_twin_sum
    
    def flipSecondHalf(self, head):
        
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = self.flipList(slow.next)
        return dummy.next
    
    def flipList(self, head):
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
            