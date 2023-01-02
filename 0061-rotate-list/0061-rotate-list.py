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
        
        # reduce k by mod length of list
        n = find_length(head)
        k = k % n
        
        # rotate k times
        for _ in range(k):
            head = rotate(head)
            
        # return list rotated to the right by k places
        return head

def rotate(head):
    pre = head
    cur = head.next
    while cur.next:
        pre = pre.next
        cur = cur.next
    pre.next = None
    cur.next = head
    return cur

def find_length(head):
    n = 0
    while head:
        head = head.next
        n += 1
    return n