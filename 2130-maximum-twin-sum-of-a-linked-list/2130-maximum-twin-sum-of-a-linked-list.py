# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # find midpoint of list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # flip second half of list
        flippedSecondHalf = self.flipList(slow)
        
        # iterate to find max twin sum
        max_twin_sum = 0
        while flippedSecondHalf:
            twin_sum = head.val + flippedSecondHalf.val
            if twin_sum > max_twin_sum:
                max_twin_sum = twin_sum
            head = head.next
            flippedSecondHalf = flippedSecondHalf.next
        
        # return max twin sum
        return max_twin_sum
    
    def flipList(self, head):
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
            