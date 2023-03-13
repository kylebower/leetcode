# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # flip two lists
        l1 = self.flipList(l1)
        l2 = self.flipList(l2)
        print(l1)
        print(l2)
        
        # sum up list
        dummy = ListNode()
        ans = dummy
        carry_one = 0
        while l1 or l2:
            # compute node val
            nodeVal = carry_one
            if l1:
                nodeVal += l1.val
            if l2:
                nodeVal += l2.val
                
            if nodeVal >= 10:
                carry_one = 1
                nodeVal -= 10
            else:
                carry_one = 0
                
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
            # update answer
            ans.next = ListNode(nodeVal)
            ans = ans.next
        
        if carry_one:            
            ans.next = ListNode(1)
            ans = ans.next
            
        # return flipped list
        return self.flipList(dummy.next)
    
    def flipList(self, head):
        
        # base case
        if not head or not head.next:
            return head
        
        # flip list
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
            
        return pre
    