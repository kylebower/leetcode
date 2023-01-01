# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # base cases
        if head == None or head.next == None:
            return head
        if k == 1:
            return head
        
        # shift previous and current pointers into position
        dummy = ListNode
        dummy.next = head
        pre = dummy
        cur = head
        
        # reverse sublist
        while cur != None:
            enough_space = checkSpace(pre,k)
            if enough_space:
                pre = reverseK(pre,cur,k)
                cur = pre.next
            else:
                break
        
        # return the modified list
        return dummy.next

def checkSpace(pre,k):
    for _ in range(k):
        if pre.next == None:
            return False
        else:
            pre = pre.next
    return True

def reverseK(pre,cur,k):
    for _ in range(1,k):
        nex = cur.next
        cur.next = nex.next
        nex.next = pre.next
        pre.next = nex
    return cur